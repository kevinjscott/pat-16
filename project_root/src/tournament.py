```python
from src.openai_wrapper import OpenAIQueryHandler
from src.page_scraper import PageScraper
from src.extractor import Extractor

class Tournament:
    def __init__(self, url):
        self.url = url
        self.openai = OpenAIQueryHandler()
        self.scraper = PageScraper()
        self.extractor = Extractor(self.openai.api_key, self.openai)
        self.tournament_data = None

    def get_tournament_data(self):
        if not self.tournament_data:
            page_text = self.scraper.scrape_event_page(self.url)
            self.tournament_data = self.extractor.extract_data(page_text, {"link": self.url})
        return self.tournament_data

    def get_players_and_teams(self):
        system_prompt = """
        Consider the following web page text. Extract the names of all players and their associated teams.
        """
        players_and_teams = self.openai.chat(system_prompt, self.tournament_data)
        return players_and_teams

    def get_course_info(self):
        system_prompt = """
        Consider the following web page text. Extract the golf course, city, and state for the tournament.
        """
        course_info = self.openai.chat(system_prompt, self.tournament_data)
        return course_info
```