import requests
from bs4 import BeautifulSoup

def get_news_headlines():
    url = "https://www.bbc.com/news"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # BBC News headline selectors (may need updating if site changes)
        headlines = soup.select('h2[data-testid="card-headline"]')[:10]
        
        print("Top 10 News Headlines from BBC News:")
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline.text.strip()}")
            
    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
    except Exception as e:
        print(f"Error parsing news: {e}")

if __name__ == "__main__":
    get_news_headlines()