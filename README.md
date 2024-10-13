# AI-Assisted OSINT Tool

<<<<<<< HEAD
=======
![Build Status](https://img.shields.io/github/actions/workflow/status/ShabalalaWATP/ai-assisted-osint-tool/ci.yml)
![License](https://img.shields.io/github/license/ShabalalaWATP/ai-assisted-osint-tool)

>>>>>>> 90e77ed009d6fecead81f8e894197e59686d3076
## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
<<<<<<< HEAD
  - [Backend](#backend)
  - [Frontend](#frontend)
- [UI Design](#ui-design)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
  - [Step 1: Clone the Repository](#step-1-clone-the-repository)
  - [Step 2: Create a Virtual Environment](#step-2-create-a-virtual-environment)
  - [Step 3: Install Dependencies](#step-3-install-dependencies)
  - [Step 4: Download SpaCy Model](#step-4-download-spacy-model)
  - [Step 5: Download NLTK Data](#step-5-download-nltk-data)
  - [Step 6: Set Up Environment Variables](#step-6-set-up-environment-variables)
    - [Obtaining API Keys](#obtaining-api-keys)
      - [Google API Key and Custom Search Engine ID](#google-api-key-and-custom-search-engine-id)
      - [NewsAPI Key](#newsapi-key)
      - [Reddit API Credentials](#reddit-api-credentials)
  - [Step 7: Run the Application](#step-7-run-the-application)
- [Usage](#usage)
  - [Accessing the Application](#accessing-the-application)
  - [Performing a Search](#performing-a-search)
  - [Interpreting the Results](#interpreting-the-results)
- [Screenshots](#screenshots)
- [Troubleshooting](#troubleshooting)
  - [Common Issues](#common-issues)
    - [1. API Errors](#1-api-errors)
    - [2. Environment Variables Not Loaded](#2-environment-variables-not-loaded)
    - [3. Missing Dependencies](#3-missing-dependencies)
    - [4. SpaCy Model Not Found](#4-spacy-model-not-found)
=======
- [UI Design](#ui-design)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Troubleshooting](#troubleshooting)
>>>>>>> 90e77ed009d6fecead81f8e894197e59686d3076
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction
<<<<<<< HEAD

The **AI-Assisted OSINT Tool** is a powerful web application designed to streamline the process of Open Source Intelligence (OSINT) gathering. By leveraging advanced AI technologies, it **aggregates and analyzes data from multiple sources**, providing users with insightful information to support research, trend monitoring, and decision-making processes.

## Features

=======
The AI-Assisted OSINT Tool is a powerful web application designed to streamline the process of Open Source Intelligence (OSINT) gathering. By leveraging advanced AI technologies, it aggregates and analyzes data from multiple sources, providing users with insightful information to support research, trend monitoring, and decision-making processes.

## Features
>>>>>>> 90e77ed009d6fecead81f8e894197e59686d3076
- **Multi-Source Data Aggregation**: Fetches data from Google Custom Search, Reddit, and NewsAPI to provide a comprehensive view of the topic.
- **Advanced Sentiment Analysis**: Utilizes state-of-the-art NLP models to assess the sentiment of fetched content.
- **Named Entity Recognition (NER)**: Identifies and highlights entities such as people, organizations, and locations within the text.
- **Keyword Extraction**: Extracts significant keywords using the YAKE algorithm for quick topic understanding.
- **Data Visualization**:
<<<<<<< HEAD
  - **Sentiment Distribution Chart**: Visual representation of the overall sentiment across the collected data.
  - **Keyword Word Cloud**: Displays the most frequent keywords in a visually engaging word cloud.
=======
    - **Sentiment Distribution Chart**: Visual representation of the overall sentiment across the collected data.
    - **Keyword Word Cloud**: Displays the most frequent keywords in a visually engaging word cloud.
>>>>>>> 90e77ed009d6fecead81f8e894197e59686d3076
- **User-Friendly Interface**: Clean and professional UI design for an optimal user experience.
- **Asynchronous Operations**: Efficient data fetching and processing without blocking the user interface.

## Technologies Used
<<<<<<< HEAD

### Backend
- **Python 3.8+**
- **Flask**: Web framework for handling HTTP requests and serving HTML pages.
- **Flask-CORS**: To handle Cross-Origin Resource Sharing.
- **Requests**: For making HTTP requests to external APIs.
- **Python-dotenv**: For loading environment variables from a `.env` file.
- **PRAW (Python Reddit API Wrapper)**: For accessing Reddit's API.
- **SpaCy**: For advanced Natural Language Processing tasks, particularly Named Entity Recognition.
  - **Model Used**: `en_core_web_trf` (Transformer-based English model)
- **Transformers**: From Hugging Face, for sentiment analysis using pre-trained models.
  - **Model Used**: `cardiffnlp/twitter-roberta-base-sentiment`
- **YAKE**: Keyword extraction algorithm.
- **NLTK**: For text processing and stopword handling.
=======
### Backend
- **Python 3.8+**
- **[Flask](https://flask.palletsprojects.com/)**: Web framework for handling HTTP requests and serving HTML pages.
- **[Flask-CORS](https://flask-cors.readthedocs.io/)**: To handle Cross-Origin Resource Sharing.
- **[Requests](https://docs.python-requests.org/)**: For making HTTP requests to external APIs.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: For loading environment variables from a .env file.
- **[PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/)**: For accessing Reddit's API.
- **[SpaCy](https://spacy.io/)**: For advanced Natural Language Processing tasks, particularly Named Entity Recognition.
    - **Model Used**: `en_core_web_trf` (Transformer-based English model)
- **[Transformers](https://huggingface.co/transformers/)**: From Hugging Face, for sentiment analysis using pre-trained models.
    - **Model Used**: `cardiffnlp/twitter-roberta-base-sentiment`
- **[YAKE](https://github.com/LIAAD/yake)**: Keyword extraction algorithm.
- **[NLTK](https://www.nltk.org/)**: For text processing and stopword handling.
>>>>>>> 90e77ed009d6fecead81f8e894197e59686d3076

### Frontend
- **HTML5 and CSS3**
- **JavaScript and jQuery**
<<<<<<< HEAD
- **Bootstrap 5**: For responsive and modern UI components.
- **D3.js**: For creating dynamic, interactive data visualizations.
- **D3 Cloud Plugin**: For generating the keyword word cloud.
- **Chart.js**: For creating the sentiment distribution pie chart.

## UI Design

The application features a **clean and modern user interface** designed with simplicity and usability in mind.

=======
- **[Bootstrap 5](https://getbootstrap.com/docs/5.0/)**: For responsive and modern UI components.
- **[D3.js](https://d3js.org/)**: For creating dynamic, interactive data visualizations.
- **D3 Cloud Plugin**: For generating the keyword word cloud.
- **[Chart.js](https://www.chartjs.org/)**: For creating the sentiment distribution pie chart.

## UI Design
The application features a clean and modern user interface designed with simplicity and usability in mind.
>>>>>>> 90e77ed009d6fecead81f8e894197e59686d3076
- **Navbar**: A fixed navigation bar with the application's name.
- **Search Bar**: Prominently placed at the top for easy access.
- **Description Section**: Provides users with an overview of the tool's capabilities.
- **Loading Spinner**: Displays while data is being fetched and processed.
- **Results Section**: Organized display of results from each source with expandable cards.
- **Sentiment Labels**: Badges indicating the sentiment of each result.
- **Entities and Keywords**: Highlighted within each result for quick reference.
<<<<<<< HEAD
- **Data Visualizations**:
  - **Sentiment Distribution Pie Chart**: Shows the proportion of positive, negative, and neutral sentiments.
  - **Keyword Word Cloud**: Visual representation of the most common keywords extracted from the data.

## Prerequisites

- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Git** (optional, for cloning the repository)

## Installation and Setup

### Step 1: Clone the Repository

You can download the repository as a ZIP file or clone it using Git:

```bash
git clone https://github.com/ShabalalaWATP/ai-assisted-osint-tool.git
cd ai-assisted-osint-tool
```

### Step 2: Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not provided, install the packages manually:

```bash
pip install flask flask-cors requests spacy transformers praw nltk yake python-dotenv
pip install torch  # Ensure PyTorch is installed for transformers and SpaCy models
```

### Step 4: Download SpaCy Model

```bash
python -m spacy download en_core_web_trf
```

### Step 5: Download NLTK Data

Run the following in a Python shell:

```python
=======

### Data Visualizations
- **Sentiment Distribution Pie Chart**: Shows the proportion of positive, negative, and neutral sentiments.
- **Keyword Word Cloud**: Visual representation of the most common keywords extracted from the data.

## Prerequisites
- **Python 3.8 or higher**
- **pip (Python package installer)**
- **Git (optional, for cloning the repository)**

...

(Continue restructuring and enhancing the rest of the content in the same manner)
Continue this approach for the remaining sections to ensure the README is comprehensive, well-structured, and easy to follow.


ShabalalaWATP
1 minute ago
give me the full improvement

Copilot
now
Here are the full improvements to the README.txt file:

Convert to Markdown for better readability:

Use proper Markdown syntax.
Add a title and badges at the top.
Enhance Structure and Formatting:

Ensure each section is clearly separated.
Use code blocks for commands and scripts.
Include images or screenshots where applicable.
Content Enhancements:

Provide more context and examples.
Ensure all steps are clear and concise.
Here is an improved version of your README.txt:

# AI-Assisted OSINT Tool

![Build Status](https://img.shields.io/github/actions/workflow/status/ShabalalaWATP/ai-assisted-osint-tool/ci.yml)
![License](https://img.shields.io/github/license/ShabalalaWATP/ai-assisted-osint-tool)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [UI Design](#ui-design)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction
The AI-Assisted OSINT Tool is a powerful web application designed to streamline the process of Open Source Intelligence (OSINT) gathering. By leveraging advanced AI technologies, it aggregates and analyzes data from multiple sources, providing users with insightful information to support research, trend monitoring, and decision-making processes.

## Features
- **Multi-Source Data Aggregation**: Fetches data from Google Custom Search, Reddit, and NewsAPI to provide a comprehensive view of the topic.
- **Advanced Sentiment Analysis**: Utilizes state-of-the-art NLP models to assess the sentiment of fetched content.
- **Named Entity Recognition (NER)**: Identifies and highlights entities such as people, organizations, and locations within the text.
- **Keyword Extraction**: Extracts significant keywords using the YAKE algorithm for quick topic understanding.
- **Data Visualization**:
    - **Sentiment Distribution Chart**: Visual representation of the overall sentiment across the collected data.
    - **Keyword Word Cloud**: Displays the most frequent keywords in a visually engaging word cloud.
- **User-Friendly Interface**: Clean and professional UI design for an optimal user experience.
- **Asynchronous Operations**: Efficient data fetching and processing without blocking the user interface.

## Technologies Used
### Backend
- **Python 3.8+**
- **[Flask](https://flask.palletsprojects.com/)**: Web framework for handling HTTP requests and serving HTML pages.
- **[Flask-CORS](https://flask-cors.readthedocs.io/)**: To handle Cross-Origin Resource Sharing.
- **[Requests](https://docs.python-requests.org/)**: For making HTTP requests to external APIs.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: For loading environment variables from a .env file.
- **[PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/)**: For accessing Reddit's API.
- **[SpaCy](https://spacy.io/)**: For advanced Natural Language Processing tasks, particularly Named Entity Recognition.
    - **Model Used**: `en_core_web_trf` (Transformer-based English model)
- **[Transformers](https://huggingface.co/transformers/)**: From Hugging Face, for sentiment analysis using pre-trained models.
    - **Model Used**: `cardiffnlp/twitter-roberta-base-sentiment`
- **[YAKE](https://github.com/LIAAD/yake)**: Keyword extraction algorithm.
- **[NLTK](https://www.nltk.org/)**: For text processing and stopword handling.

### Frontend
- **HTML5 and CSS3**
- **JavaScript and jQuery**
- **[Bootstrap 5](https://getbootstrap.com/docs/5.0/)**: For responsive and modern UI components.
- **[D3.js](https://d3js.org/)**: For creating dynamic, interactive data visualizations.
- **D3 Cloud Plugin**: For generating the keyword word cloud.
- **[Chart.js](https://www.chartjs.org/)**: For creating the sentiment distribution pie chart.

## UI Design
The application features a clean and modern user interface designed with simplicity and usability in mind.
- **Navbar**: A fixed navigation bar with the application's name.
- **Search Bar**: Prominently placed at the top for easy access.
- **Description Section**: Provides users with an overview of the tool's capabilities.
- **Loading Spinner**: Displays while data is being fetched and processed.
- **Results Section**: Organized display of results from each source with expandable cards.
- **Sentiment Labels**: Badges indicating the sentiment of each result.
- **Entities and Keywords**: Highlighted within each result for quick reference.

### Data Visualizations
- **Sentiment Distribution Pie Chart**: Shows the proportion of positive, negative, and neutral sentiments.
- **Keyword Word Cloud**: Visual representation of the most common keywords extracted from the data.

## Prerequisites
- **Python 3.8 or higher**
- **pip (Python package installer)**
- **Git (optional, for cloning the repository)**

## Installation and Setup
### Step 1: Clone the Repository
You can download the repository as a ZIP file or clone it using Git:
```bash
git clone https://github.com/ShabalalaWATP/ai-assisted-osint-tool.git
cd ai-assisted-osint-tool
Step 2: Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

python -m venv venv
Activate the virtual environment:

On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
Step 3: Install Dependencies
pip install -r requirements.txt
If a requirements.txt file is not provided, install the packages manually:

pip install flask flask-cors requests spacy transformers praw nltk yake python-dotenv
pip install torch  # Ensure PyTorch is installed for transformers and SpaCy models
Step 4: Download SpaCy Model
python -m spacy download en_core_web_trf
Step 5: Download NLTK Data
Run the following in a Python shell:

>>>>>>> 90e77ed009d6fecead81f8e894197e59686d3076
import nltk
nltk.download('stopwords')
nltk.download('punkt')
exit()
<<<<<<< HEAD
```

### Step 6: Set Up Environment Variables

Create a `.env` file in the root directory of the project:

```bash
touch .env
```

Add your API keys and IDs to the `.env` file:

```plaintext
=======
Step 6: Set Up Environment Variables
Create a .env file in the root directory of the project:

touch .env
Add your API keys and IDs to the .env file:

>>>>>>> 90e77ed009d6fecead81f8e894197e59686d3076
GOOGLE_API_KEY=your_actual_google_api_key
GOOGLE_CSE_ID=your_actual_custom_search_engine_id
NEWSAPI_KEY=your_actual_newsapi_key
REDDIT_CLIENT_ID=your_actual_reddit_client_id
REDDIT_CLIENT_SECRET=your_actual_reddit_client_secret
<<<<<<< HEAD
```

**Important**: Replace the placeholders with your actual API keys and secrets.

#### Obtaining API Keys

##### Google API Key and Custom Search Engine ID

- **Google API Key**:
  - Sign in to [Google Cloud Console](https://console.cloud.google.com/).
  - Create a new project or select an existing one.
  - Navigate to **APIs & Services > Credentials**.
  - Click **Create Credentials > API Key**.

- **Custom Search Engine ID (CSE ID)**:
  - Go to the [Custom Search Engine](https://cse.google.com/cse/) page.
  - Click **Add** to create a new search engine.
  - In **Sites to search**, enter `*` to search the entire web.
  - Once created, go to **Control Panel** to find your **Search engine ID**.

##### NewsAPI Key

- Sign up at [NewsAPI.org](https://newsapi.org/) to get an API key.

##### Reddit API Credentials

- Create an app at [Reddit Apps](https://www.reddit.com/prefs/apps).
- Select **Script** as the app type.
- Note down the **Client ID** and **Secret**.

### Step 7: Run the Application

```bash
python app.py
```

You should see output indicating that the application is running:

```plaintext
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

## Usage

### Accessing the Application

Open a web browser and navigate to [http://localhost:5000](http://localhost:5000).

### Performing a Search

- **Enter a Search Term**: Use the search bar at the top to input your query.
- **Click "Search"**: Initiates the data fetching and analysis process.
- **View Results**:
  - **Sentiment Distribution Chart**: Displays the overall sentiment analysis.
  - **Keyword Word Cloud**: Shows the most frequent keywords.
  - **Source Results**: Scroll down to see detailed results from Google, Reddit, and NewsAPI.

### Interpreting the Results

- **Sentiment Badges**: Each result includes a badge indicating its sentiment:
  - **Positive**: Green badge.
  - **Negative**: Red badge.
  - **Neutral**: Grey badge.
- **Entities**: Highlighted entities extracted from the text.
- **Keywords**: Significant keywords identified in the content.

## Screenshots

- **Home Page**
- **Search Results**
- **Sentiment Distribution Chart**
- **Keyword Word Cloud**

## Troubleshooting

### Common Issues

#### 1. API Errors

- **Invalid API Key**: Ensure all API keys are correct and have the necessary permissions.
- **Quota Limits Exceeded**: APIs like Google Custom Search and NewsAPI have usage limits.
  - **Solution**: Monitor your usage or upgrade your plan if necessary.

#### 2. Environment Variables Not Loaded

- **Symptom**: Variables like `GOOGLE_CSE_ID` appear as `None`.
- **Solution**: Ensure the `.env` file is in the root directory and `load_dotenv()` is called in `app.py`.

#### 3. Missing Dependencies

- **Symptom**: `ModuleNotFoundError` when running `app.py`.
- **Solution**: Install all required packages using `pip install -r requirements.txt`.

#### 4. SpaCy Model Not Found

- **Symptom**: Error indicating the `en_core_web_trf` model is missing.
- **Solution**: Run `python -m spacy download en_core_web_trf`.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**: Create a personal copy of the repository on your GitHub account.
2. **Create a New Branch**: For your feature or bug fix.

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**: Implement your feature or fix.
4. **Commit Changes**:

   ```bash
   git commit -am 'Add new feature'
   ```

5. **Push to the Branch**:

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**: Submit your changes for review.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Hugging Face**: For the Transformers library and pre-trained models.
- **SpaCy**: For powerful NLP capabilities.
- **NLTK**: For foundational NLP tools.
- **YAKE**: For keyword extraction algorithms.
- **PRAW**: For seamless Reddit API integration.
- **Bootstrap**: For responsive UI components.
- **D3.js and Chart.js**: For data visualization.

**Note**: This tool is intended for educational and research purposes. Please use it responsibly and adhere to the terms of service of the APIs and data sources used.
=======
Important: Replace the placeholders with your actual API keys and secrets.

Obtaining API Keys
Google API Key and Custom Search Engine ID:

Google API Key:

Sign in to Google Cloud Console.
Create a new project or select an existing one.
Navigate to APIs & Services > Credentials.
Click Create Credentials > API Key.
Custom Search Engine ID (CSE ID):

Go to the Custom Search Engine page.
Click Add to create a new search engine.
In Sites to search, enter * to search the entire web.
Once created, go to Control Panel to find your Search engine ID.
NewsAPI Key:

Sign up at NewsAPI.org to get an API key.
Reddit API Credentials:

Create an app at Reddit Apps.
Select Script as the app type.
Note down the Client ID and Secret.
Step 7: Run the Application
python app.py
You should see output indicating that the application is running:

 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Usage
Accessing the Application
Open a web browser and navigate to http://localhost:5000.

Performing a Search
Enter a Search Term: Use the search bar at the top to input your query.
Click "Search": Initiates the data fetching and analysis process.
View Results:
Sentiment Distribution Chart: Displays the overall sentiment analysis.
Keyword Word Cloud: Shows the most frequent keywords.
Source Results: Scroll down to see detailed results from Google, Reddit, and NewsAPI.
Interpreting the Results
Sentiment Badges: Each result includes a badge indicating its sentiment:
Positive: Green badge.
Negative: Red badge.
Neutral: Grey badge.
Entities: Highlighted entities extracted from the text.
Keywords: Significant keywords identified in the content.
Screenshots
Home Page
Search Results
Sentiment Distribution Chart
Keyword Word Cloud
Troubleshooting
Common Issues
API Errors

Invalid API Key: Ensure all API keys are correct and have the necessary permissions.
Quota Limits Exceeded: APIs like Google Custom Search and NewsAPI have usage limits.
Solution: Monitor your usage or upgrade your plan if necessary.
Environment Variables Not Loaded

Symptom: Variables like GOOGLE_CSE_ID appear as None.
Solution: Ensure the .env file is in the root directory and load_dotenv() is called in app.py.
Missing Dependencies

Symptom: ModuleNotFoundError when running app.py.
Solution: Install all required packages using pip install -r requirements.txt.
SpaCy Model Not Found

Symptom: Error indicating the en_core_web_trf model is missing.
Solution: Run python -m spacy download en_core_web_trf.
Contributing
Contributions are welcome! Please follow these steps:

Fork the Repository: Create a personal copy of the repository on your GitHub account.
Create a New Branch: For your feature or bug fix.
git checkout -b feature/your-feature-name
Make Changes: Implement your feature or fix.
Commit Changes:
git commit -am 'Add new feature'
Push to the Branch:
git push origin feature/your-feature-name
Create a Pull Request: Submit your changes for review.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Hugging Face: For the Transformers library and pre-trained models.
SpaCy: For powerful NLP capabilities.
NLTK: For foundational NLP tools.
YAKE: For keyword extraction algorithms.
PRAW: For seamless Reddit API integration.
Bootstrap: For responsive UI components.
D3.js and Chart.js: For data visualization.
Note: This tool is intended for educational and research purposes. Please use it responsibly and adhere to the terms of service of the APIs and data sources used.
>>>>>>> 90e77ed009d6fecead81f8e894197e59686d3076
