import sys
sys.path.insert(0, '/Users/arturzhdan/lab_nulp_python/')

from models.clip import Clip
from models.film import Film
from models.abstract import Video
from decorators.log_class_method import log_class_method
from decorators.measure_time import measure_time


class VideoManager:
    def __init__(self, videos = None):
        if videos is None:
            videos = []
        self.videos = videos

    def __len__(self):
        return len(self.videos)

    def __getitem__(self, index):
        return self.videos[index]

    def __iter__(self):
        return iter(self.videos)

    def add_video(self, video: Video):
        self.videos.append(video)

    def do_something_results(self):
        return [video.get_current_rating() for video in self.videos]

    def enumerated_videos(self):
        return list(enumerate(self.videos))

    def zip_videos_ratings(self):
        return list(zip(self.videos, self.do_something_results()))

    @log_class_method
    @measure_time
    def check_condition(self, condition):
        results = [condition(video) for video in self.videos]
        return {"all": all(results), "any": any(results)}

def main():
    manager = VideoManager()
    film1 = Film("Film1", "Director1", 2021, {'comedy', 'action'},-4.5)
    film2 = Film("Film2", "Director2", 2022, {'comedy', 'action'},3.7)
    clip1 = Clip("Song1", "Artist1", 1000,{'comedy', 'action'}, 50000, "Song1", "Artist1", 1000, 50000)
    clip2 = Clip("Song2", "Artist2", 2000, {'comedy', 'action'},45000, "Song2", "Artist2", 2000, 45000)

    manager.add_video(film1)
    manager.add_video(film2)
    manager.add_video(clip1)
    manager.add_video(clip2)

    print("Results of do_something (get_current_rating):", manager.do_something_results())
    print("\nEnumerated videos:", manager.enumerated_videos())
    print("\nZipped videos and ratings:", manager.zip_videos_ratings())
    print("\nAttributes of type str for first video:", manager[0].get_attributes_of_type(str))
    print("\nCheck if all videos have rating greater than 4.0:", manager.check_condition(lambda video: video.get_current_rating() > 4.0))

if __name__ == "__main__":
    main()