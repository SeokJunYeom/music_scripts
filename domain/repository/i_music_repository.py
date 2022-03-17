import abc
from typing import List
from pathlib import Path

from domain.entity.music_entity import MusicEntity
from domain.dto.tag_dto import TagDTO


class IMusicRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, path: Path) -> MusicEntity:
        raise NotImplemented

    @abc.abstractmethod
    def get_all(self) -> List[MusicEntity]:
        raise NotImplemented

    @abc.abstractmethod
    def convert_tags(self, music_entity: MusicEntity, tag_dto: TagDTO) -> MusicEntity:
        raise NotImplemented
