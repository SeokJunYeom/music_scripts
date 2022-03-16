import abc
from typing import List
from pathlib import Path

from domain.entity.music_entity import MusicEntity


class IMusicRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, path: Path) -> MusicEntity:
        raise NotImplemented

    @abc.abstractmethod
    def get_all(self) -> List[MusicEntity]:
        raise NotImplemented
