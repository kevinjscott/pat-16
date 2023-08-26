```python
class ProgressPrinter:
    def __init__(self):
        pass

    def print_progress(self, message):
        print(message)

    def print_player_info(self, player):
        print(f"Player: {player.name}, Team: {player.team}")

    def print_tournament_info(self, tournament):
        print(f"Tournament: {tournament.name}, Location: {tournament.location}")

    def print_course_info(self, course):
        print(f"Course: {course.name}, Rating: {course.rating}")

    def print_pat_result(self, player, result):
        print(f"{player.name} has {'passed' if result else 'not passed'} the PAT.")

    def print_social_media_info(self, player):
        print(f"Instagram: {player.instagram}, Twitter: {player.twitter}, LinkedIn: {player.linkedin}")

    def print_compilation_result(self, result):
        print(f"Compilation Result: {result}")

    def print_openai_usage(self, openai_handler):
        total_tokens, total_cost = openai_handler.get_usage()
        print(f"OpenAI Usage - Total Tokens: {total_tokens}, Total Cost: {total_cost}")
```