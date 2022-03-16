import os
from pathlib import Path
from typing import Generator, Optional

import inject
import mutagen

from settings.config import BaseConfig
from domain.repository.i_music_repository import IMusicRepository
from domain.entity.music_entity import MusicEntity
from domain.vo.duration_vo import DurationVO


class FileMusicRepository(IMusicRepository):

    @inject.autoparams()
    def __init__(self, config: BaseConfig):
        self.config = config

    def get_all(self) -> Generator[MusicEntity, None, None]:

        def make_music_entity_from_file_system():
            for root, dirs, files in os.walk(self.config.FILE_MUSIC_ROOT_DIRECTORY, topdown=False):
                if len(files) > 0:
                    for file in files:
                        path = Path(root) / Path(file)
                        music_entity = self.get(path)
                        if music_entity is not None:
                            yield music_entity

        return make_music_entity_from_file_system()

    def get(self, path) -> Optional[MusicEntity]:
        audio = mutagen.File(path)

        if audio is None:
            return None

        with open(path, 'rb') as f:
            body = f.read()

        return MusicEntity(
            path=path.relative_to(self.config.FILE_MUSIC_ROOT_DIRECTORY),
            body=body,
            disc_number=self._get_mutagen_tag(audio, 'discnumber', int),
            track_number=self._get_mutagen_tag(audio, 'tracknumber', int),
            title=self._get_mutagen_tag(audio, 'title', str),
            cover=audio.pictures.pop().data,
            album_artist=self._get_mutagen_tag(audio, 'albumartist', str),
            genre=self._get_mutagen_tag(audio, 'genre', str, default=None),
            date=self._get_mutagen_tag(audio, 'date', int),
            artist=self._get_mutagen_tag(audio, 'artist', str),
            duration=DurationVO(value=int(audio.info.length))
        )

    def _get_mutagen_tag(self, audio, tag: str, value_type: type, **kwargs):
        if _tag := audio.tags.get(tag):
            return value_type(_tag.pop())
        return kwargs['default'] if 'default' in kwargs else value_type()

