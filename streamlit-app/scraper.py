import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

def is_valid_url(url, base_domain):
    """Check if URL belongs to the same domain"""
    parsed = urlparse(url)
    return (parsed.netloc == base_domain or not parsed.netloc) and \
           not url.startswith(('mailto:', 'tel:', 'javascript:'))

def scrape_website(base_url, max_depth=1, delay=2.0, timeout=10):
    """Universal scraper that handles all websites"""
    visited = set()
    to_visit = [(base_url, 0)]
    scraped_data = []
    base_domain = urlparse(base_url).netloc
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept-Language': 'en-US,en;q=0.5'
    }

    while to_visit and len(scraped_data) < 50:  # Safety limit
        url, depth = to_visit.pop(0)
        
        if url in visited or depth > max_depth:
            continue
            
        try:
            time.sleep(max(0.5, delay))  # Minimum 0.5s delay
            
            response = requests.get(url, headers=headers, timeout=timeout)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove unwanted elements
            for element in soup(["script", "style", "nav", "footer", "iframe", "svg"]):
                element.decompose()
                
            # Extract content
            title = soup.title.string if soup.title else 'No Title'
            text = soup.get_text(separator='\n', strip=True)[:100000]  # Limit size
            
            scraped_data.append({
                'url': url,
                'title': title,
                'content': text
            })
            
            visited.add(url)
            
            # Handle subpages
            if depth < max_depth:
                for link in soup.find_all('a', href=True):
                    absolute_url = urljoin(base_url, link['href'].split('#')[0])
                    if (absolute_url.startswith(('http://', 'https://')) and
                        is_valid_url(absolute_url, base_domain) and
                        absolute_url not in visited):
                        to_visit.append((absolute_url, depth + 1))
                        
        except Exception as e:
            print(f"Error scraping {url}: {str(e)}")
            continue
            
    return scraped_data
