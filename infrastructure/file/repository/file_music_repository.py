import os
from pathlib import Path
from typing import Generator, Optional

import mutagen

from domain.dto.tag_dto import TagDTO
from settings import config
from domain.repository.i_music_repository import IMusicRepository
from domain.entity.music_entity import MusicEntity
from domain.vo.duration_vo import DurationVO


class FileMusicRepository(IMusicRepository):

    def __init__(self, music_dir: Path = config.MUSIC_DIR):
        self.music_dir = music_dir

    def get_all(self) -> Generator[MusicEntity, None, None]:

        def make_music_entity_from_file_system():
            for root, dirs, files in os.walk(self.music_dir, topdown=False):
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
            path=path,
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

    def convert_tags(self, music_entity: MusicEntity, tag_dto: TagDTO) -> MusicEntity:
        for key, value in tag_dto:
            if key == 'duration':
                if music_entity.duration.value != value:
                    music_entity.duration = DurationVO(value=value)
            else:
                if getattr(music_entity, key, None) != value:
                    setattr(music_entity, key, value)

                    if key == 'title':
                        music_entity = self.convert_path_safely_on_os(music_entity)

        return music_entity

    def convert_path_safely_on_os(self, music_entity: MusicEntity) -> MusicEntity:
        title = music_entity.title

        symbol_map = {
            '\\': '＼',
            '/': '／',
            ':': '：',
            '*': '＊',
            '?': '？',
            '"': '”',
            '<': '＜',
            '>': '＞',
        }

        filename = title
        i = 0

        while i < len(filename):
            tmp = ''
            if filename[i] in symbol_map:
                if i > 0:
                    if filename[i-1] == ' ':
                        tmp += filename[:i-1]
                    else:
                        tmp += filename[:i]
                tmp += symbol_map[filename[i]]
                index_memory = len(tmp)
                if i < len(filename) - 1:
                    if i != len(filename) - 1 and filename[i+1] == ' ':
                        tmp += filename[i+2:]
                    else:
                        tmp += filename[i+1:]
                filename = tmp
                i = index_memory
            else:
                i += 1

        music_entity.path = music_entity.path.parent / filename

        return music_entity

    def save(self, music_entity: MusicEntity, target: Path) -> MusicEntity:
        path = target / music_entity.path.relative_to(self.music_dir)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'wb') as f:
            f.write(music_entity.body)
        music_entity.path = path

        return music_entity
