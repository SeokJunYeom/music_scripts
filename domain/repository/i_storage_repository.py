import abc

from domain.entity.music_entity import MusicEntity


class IStorageRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def save(self, music: MusicEntity):
        raise NotImplemented
