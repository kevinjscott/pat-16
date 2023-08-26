```python
import json
from datetime import datetime
from openai_wrapper import OpenAIQueryHandler

class Extractor:

    def __init__(self):
        self.openai = OpenAIQueryHandler()

    def extract_data(self, page_data, player):
        interim_data = self.extract_data_step_1(page_data, player)
        interim_data = self.extract_data_step_2(interim_data, player)
        return interim_data

    def extract_data_step_1(self, page_data, player):
        basic_prompt = """
        Consider the following web page text. Exclude any categories or tags mentioned in the text then extract the following info:
        Player name
        Associated team (college)
        Golf course
        City
        State
        """

        extracted_data = self.openai.chat(basic_prompt, "link_to_player: " + player['link'] + " \\n" + "Today's Date: " + datetime.now().strftime('%Y-%m-%d') + " \\n" + json.dumps(player) + " \\n" + page_data)
        return extracted_data

    def extract_data_step_2(self, step_1_results, player):
        system_prompt = """
        Always return only JSON: player_name, team, golf_course, city, state
        No talk. Just do.
        """

        extracted_data = self.openai.chat(system_prompt, step_1_results, "gpt-3.5-turbo")

        try:
            extracted_data = json.loads(extracted_data)
            return extracted_data
        except json.JSONDecodeError:
            return None
```