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

    def get_all_musics(self) -> Generator[MusicEntity, None, None]:

        def make_music_entity_from_file_system():
            for root, dirs, files in os.walk(self.config.FILE_MUSIC_ROOT_DIRECTORY, topdown=False):
                if len(files) > 0:
                    for file in files:
                        path = Path(root) / Path(file)
                        music_entity = self._make_music_entity_with_mutagen(path)
                        if music_entity is not None:
                            yield music_entity

        return make_music_entity_from_file_system()

    def _make_music_entity_with_mutagen(self, path) -> Optional[MusicEntity]:
        audio = mutagen.File(path)

        if audio is None:
            return None

        with open(path, 'rb') as f:
            body = f.read()

        return MusicEntity(
            path=path,
            body=body,
            disc_number=int(audio.tags['discnumber'].pop()) if audio.tags.get('discnumber') else 0,
            track_number=int(audio.tags['tracknumber'].pop()) if audio.tags.get('tracknumber') else 0,
            title=audio.tags['title'].pop() if audio.tags.get('title') else '',
            cover=audio.pictures.pop().data,
            album_artist=audio.tags['albumartist'].pop() if audio.tags.get('albumartist') else '',
            genre=audio.tags['genre'].pop() if audio.tags.get('genre') else None,
            date=int(audio.tags['date'].pop()) if audio.tags.get('date') else 0,
            artist=audio.tags['artist'].pop() if audio.tags.get('artist') else '',
            duration=DurationVO(value=int(audio.info.length))
        )
