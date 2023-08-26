class Player:
    def __init__(self, name, team, scores):
        self.name = name
        self.team = team
        self.scores = scores
        self.social_media = {}

    def calculate_score(self, course_rating):
        total_score = sum(self.scores)
        pat_score = (course_rating * 2) + 15
        return total_score <= pat_score

    def set_social_media(self, social_media):
        self.social_media = social_media

    def get_data(self):
        return {
            "name": self.name,
            "team": self.team,
            "scores": self.scores,
            "social_media": self.social_media
        }