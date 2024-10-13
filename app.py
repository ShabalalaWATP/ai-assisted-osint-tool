import os
import re
import logging
import requests
import spacy
from datetime import datetime
from collections import Counter
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from transformers import pipeline
import praw
import nltk
import yake

# Download necessary NLTK data (you can comment these lines if already downloaded)
nltk.download('stopwords')
nltk.download('punkt')

# Initialize logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load API keys from environment variables
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID')
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')

# Initialize Reddit client
reddit = None
try:
    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent='osint_tool'
    )
    logger.info("Reddit instance initialized successfully")
except Exception as e:
    logger.error(f"Error initializing Reddit instance: {e}")

# Initialize sentiment analyzer
sentiment_analyzer = None
try:
    sentiment_analyzer = pipeline('sentiment-analysis', model='cardiffnlp/twitter-roberta-base-sentiment')
    logger.info("Advanced sentiment analyzer initialized successfully")
except Exception as e:
    logger.error(f"Error initializing sentiment analyzer: {e}")

# Load SpaCy model for NER
nlp = None
try:
    nlp = spacy.load('en_core_web_trf')
    logger.info("SpaCy transformer model loaded successfully")
except Exception as e:
    logger.error(f"Error loading SpaCy model: {e}")

# Initialize YAKE keyword extractor
kw_extractor = yake.KeywordExtractor(top=5, stopwords=None)

def get_sentiment_label(label):
    if label == 'LABEL_2':
        return "Positive"
    elif label == 'LABEL_0':
        return "Negative"
    else:
        return "Neutral"

def analyze_text(text):
    if sentiment_analyzer is None:
        sentiment_label = "Neutral"
        sentiment_score = 0.0
    else:
        # Limit text length to prevent errors
        text_to_analyze = text[:512]
        sentiment_result = sentiment_analyzer(text_to_analyze)[0]
        sentiment_label = get_sentiment_label(sentiment_result['label'])
        sentiment_score = sentiment_result['score']

    if nlp is None:
        entities = []
    else:
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Keyword extraction using YAKE
    keywords = kw_extractor.extract_keywords(text)
    keywords = [kw[0] for kw in keywords]

    return sentiment_label, sentiment_score, entities, keywords

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    google_results = search_google(query)
    reddit_results = search_reddit(query)
    newsapi_results = search_newsapi(query)

    # Combine all results for keywords
    all_results = google_results + reddit_results + newsapi_results
    keywords = extract_keywords(all_results)

    return jsonify({
        'google': google_results,
        'reddit': reddit_results,
        'newsapi': newsapi_results,
        'keywords': keywords
    })

def search_google(query):
    url = 'https://www.googleapis.com/customsearch/v1'
    all_items = []
    start_indices = [1, 11]  # Fetch results starting at 1 and 11
    for start_index in start_indices:
        params = {
            'key': GOOGLE_API_KEY,
            'cx': GOOGLE_CSE_ID,
            'q': query,
            'num': 10,  # Maximum allowed per request
            'start': start_index
        }
        response = None
        try:
            logger.debug(f"Making request to Google API with params: {params}")
            response = requests.get(url, params=params)
            response.raise_for_status()
            results = response.json()
            items = results.get('items', [])
            for item in items:
                snippet = item.get('snippet', '')
                sentiment_label, sentiment_score, entities, keywords = analyze_text(snippet)
                date = extract_date_from_snippet(snippet)
                all_items.append({
                    'source': 'Google',
                    'title': item.get('title'),
                    'link': item.get('link'),
                    'snippet': snippet,
                    'sentiment_score': sentiment_score,
                    'sentiment_label': sentiment_label,
                    'entities': entities,
                    'keywords': keywords,
                    'date': date
                })
        except requests.RequestException as e:
            error_message = str(e)
            if response is not None and response.content:
                try:
                    error_json = response.json()
                    error_message = error_json.get('error', {}).get('message', error_message)
                except ValueError:
                    pass
            logger.error(f"Error fetching data from Google Custom Search API: {error_message}")
            return [{'error': f'Error fetching data from Google Custom Search API: {error_message}'}]
    logger.info(f"Google search successful. Found {len(all_items)} results.")
    return all_items

def search_reddit(query):
    results = []
    if reddit is None:
        logger.error("Reddit instance not initialized. Skipping Reddit search.")
        return [{'error': 'Reddit search unavailable'}]
    try:
        for submission in reddit.subreddit('all').search(query, sort='new', limit=20):
            if not submission.over_18:
                sentiment_label, sentiment_score, entities, keywords = analyze_text(submission.title)
                results.append({
                    'source': 'Reddit',
                    'title': submission.title,
                    'score': submission.score,
                    'url': submission.url,
                    'created_utc': submission.created_utc,
                    'sentiment_score': sentiment_score,
                    'sentiment_label': sentiment_label,
                    'entities': entities,
                    'keywords': keywords,
                    'date': datetime.fromtimestamp(submission.created_utc)
                })
        logger.info(f"Reddit search successful. Found {len(results)} results.")
        return results
    except Exception as e:
        logger.error(f"Error fetching data from Reddit: {e}")
        return [{'error': f'Error fetching data from Reddit: {e}'}]

def search_newsapi(query):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'apiKey': NEWSAPI_KEY,
        'q': query,
        'language': 'en',
        'sortBy': 'publishedAt',
        'pageSize': 20
    }
    response = None
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        results = response.json()
        articles = results.get('articles', [])
        processed_articles = []
        for article in articles:
            content = article.get('content') or article.get('description') or ''
            publishedAt = article.get('publishedAt')
            if publishedAt:
                try:
                    publishedAt = datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ')
                except ValueError:
                    publishedAt = datetime.min
            else:
                publishedAt = datetime.min
            sentiment_label, sentiment_score, entities, keywords = analyze_text(content)
            processed_articles.append({
                'source': 'NewsAPI',
                'title': article.get('title'),
                'url': article.get('url'),
                'content': content,
                'sentiment_score': sentiment_score,
                'sentiment_label': sentiment_label,
                'entities': entities,
                'keywords': keywords,
                'publishedAt': publishedAt,
                'date': publishedAt
            })
        logger.info(f"NewsAPI search successful. Found {len(processed_articles)} results.")
        return processed_articles
    except requests.RequestException as e:
        error_message = str(e)
        if response is not None and response.content:
            try:
                error_json = response.json()
                error_message = error_json.get('message', error_message)
            except ValueError:
                pass
        logger.error(f"Error fetching data from NewsAPI: {error_message}")
        return [{'error': f'Error fetching data from NewsAPI: {error_message}'}]

def extract_date_from_snippet(snippet):
    date_patterns = [
        r'(\b\w+\s\d{1,2},\s\d{4}\b)',  # e.g., "Jan 1, 2023"
        r'(\b\d{1,2}\s\w+\s\d{4}\b)'    # e.g., "1 January 2023"
    ]
    for pattern in date_patterns:
        match = re.search(pattern, snippet)
        if match:
            try:
                return datetime.strptime(match.group(0), '%b %d, %Y')
            except ValueError:
                try:
                    return datetime.strptime(match.group(0), '%d %B %Y')
                except ValueError:
                    pass
    return datetime.min

def extract_keywords(results):
    keyword_list = []
    for item in results:
        keywords = item.get('keywords', [])
        keyword_list.extend(keywords)
    # Get the most common keywords
    most_common_keywords = Counter(keyword_list).most_common(50)
    keywords = [{'text': kw[0], 'size': kw[1]} for kw in most_common_keywords]
    return keywords

if __name__ == '__main__':
    app.run(debug=True)
