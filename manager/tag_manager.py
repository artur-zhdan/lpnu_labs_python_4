import sys
sys.path.insert(0, '/Users/arturzhdan/lab_nulp_python/')

from manager.video_manager import VideoManager
from models.abstract import Video
from models.clip import Clip
from models.film import Film
from decorators.log_class_method import log_class_method
from decorators.measure_time import measure_time

class TagsManager:
    def __init__(self, video_manager: VideoManager):
        self.video_manager = video_manager
        self.tags = [tag for video in video_manager for tag in video]

    def __len__(self):
        return len(self.tags)

    def __getitem__(self, index):
        return self.tags[index]

    def __iter__(self):
        return iter(self.tags)
    

if __name__ == "__main__":
    video1 = Film('Film1', 'Director1', 2001, {'comedy', 'action'}, 1)
    video2 = Clip('Clip1', 'Director2', 2002, {'music', 'pop'}, 2, 'Song1', 'Artist1', 1000, 50000)

    video_manager = VideoManager([video1, video2])
    tags_manager = TagsManager(video_manager)

    for tag in tags_manager:
        print(tag)