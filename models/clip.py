from models.abstract import Video

class Clip(Video):
    def __init__(self, title, director, year, tags,rating, song_title, artist, likes, views):
        super().__init__(title, director, year, tags, rating)
        self.song_title = song_title
        self.artist = artist
        self.likes = likes
        self.views = views


    def get_current_rating(self):
        return self.likes / self.views if self.views else 0

    def __str__(self):
        return super().__str__() + f", Type: Clip, Song: {self.song_title}, Artist: {self.artist}, Likes: {self.likes}, Views: {self.views}"
