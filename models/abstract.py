import sys
sys.path.insert(0, '/Users/arturzhdan/lab_nulp_python/')

from abc import ABC, abstractmethod
from decorators.exceptions_logger import logged, NegativeRatingException

class Video(ABC):
    def __init__(self, title, director, year, tags, rating):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating
        self.tags = tags

    @staticmethod
    def get_instance():
        if not Video.__instance:
            Video.__instance = Video()
        return Video.__instance

    @abstractmethod
    @logged(NegativeRatingException, 'file')
    def get_current_rating(self):
        if self.rating < 0:
            raise NegativeRatingException("Rating cannot be negative")
        return self.rating
    
    def get_attributes_of_type(self, attr_type):
        return {k: v for k, v in self.__dict__.items() if isinstance(v, attr_type)}

    def __iter__(self):
        return iter(self.tags)

    def __str__(self):
        return f"Title: {self.title}, Director: {self.director}, Year: {self.year}"
