from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv
import certifi
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)

# NewsAPI configuration
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

def get_news_articles():
    """Fetch top news articles from NewsAPI"""
    try:
        params = {
            'apiKey': NEWS_API_KEY,
            'country': 'us',
            'category': 'general',
            'pageSize': 12
        }
        
        response = requests.get(NEWS_API_URL, params=params, verify=certifi.where())
        response.raise_for_status()
        data = response.json()
        
        articles = []
        for article in data.get('articles', []):
            # Format the published date
            published_date = None
            if article.get('publishedAt'):
                try:
                    date_obj = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
                    published_date = date_obj.strftime('%B %d, %Y')
                except:
                    published_date = article['publishedAt']
            
            articles.append({
                'title': article.get('title', 'No title available'),
                'description': article.get('description', 'No description available'),
                'url': article.get('url', '#'),
                'image_url': article.get('urlToImage', None),
                'source': article.get('source', {}).get('name', 'Unknown source'),
                'published_date': published_date
            })
        return articles
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return []

@app.route('/')
def index():
    """Render the main page with news articles"""
    articles = get_news_articles()
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True) 