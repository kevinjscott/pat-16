```python
import requests
from bs4 import BeautifulSoup

def is_visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif isinstance(element, Comment):
        return False
    return True

class PageScraper:
    def __init__(self):
        pass

    def scrape_event_page(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get all the text from the soup and filter out non-visible elements
        texts = soup.findAll(text=True)
        visible_texts = filter(is_visible, texts)

        return " ".join(t.strip() for t in visible_texts)
```