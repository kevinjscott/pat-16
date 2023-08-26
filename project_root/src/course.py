```python
from openai_wrapper import OpenAIQueryHandler

class Course:
    def __init__(self, openai_handler: OpenAIQueryHandler):
        self.openai_handler = openai_handler

    def extract_course_info(self, page_text):
        system_prompt = """
        Given the following web page text, extract the golf course name, city, and state.
        """
        course_info = self.openai_handler.chat(system_prompt, page_text)
        return course_info

    def extract_course_rating(self, page_text):
        system_prompt = """
        Given the following web page text, extract the course rating.
        """
        course_rating = self.openai_handler.chat(system_prompt, page_text)
        return course_rating

    def check_player_scores(self, player_scores, course_rating):
        if sum(player_scores) <= (course_rating * 2) + 15:
            return True
        return False
```