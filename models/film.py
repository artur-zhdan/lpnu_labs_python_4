from models.abstract import Video

class Film(Video):
    def __init__(self, title, director, year, tags,rating):
        super().__init__(title, director, year, tags, rating)

    def get_current_rating(self):
        return super().get_current_rating()

    def __str__(self):
        return super().__str__() + ", Type: Film"
