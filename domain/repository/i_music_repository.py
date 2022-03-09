import abc
from typing import List

from domain.entity.music_entity import MusicEntity


class IMusicRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_all_musics(self) -> List[MusicEntity]:
        raise NotImplemented
