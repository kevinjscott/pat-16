```python
import json

class ResultsCompiler:

    def __init__(self):
        self.results = []

    def add_result(self, player, course, tournament, social_media):
        result = {
            "player": player.get_details(),
            "course": course.get_details(),
            "tournament": tournament.get_details(),
            "social_media": social_media
        }
        self.results.append(result)

    def compile_results(self):
        return self.results

    def save_results(self, filename="results.json"):
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=4)

    def load_results(self, filename="results.json"):
        with open(filename, 'r') as f:
            self.results = json.load(f)
```