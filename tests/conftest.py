from typing import List
from pathlib import Path

import pytest
import inject

from settings.config import BaseConfig
from settings.ioc_container import initialize_ioc
from domain.entity.music_entity import MusicEntity
from domain.vo.genre_vo import GenreVO
from domain.vo.duration_vo import DurationVO
from tests.album_covers import cover1, cover2


initialize_ioc()


@pytest.fixture(scope='session')
def mock_music_entity() -> MusicEntity:
    config = inject.instance(BaseConfig)
    root_dir = config.FILE_MUSIC_ROOT_DIRECTORY

    with open(root_dir / Path("Pop/Michael Jackson/Thriller/Wanna Be Startin' Somethin'.flac"), 'rb') as f:
        body = f.read()

    return MusicEntity(path=Path("Pop/Michael Jackson/Thriller/Wanna Be Startin' Somethin'.flac"),
                       body=body,
                       track_number=1,
                       title="Wanna Be Startin' Somethin'",
                       cover=cover1,
                       album_artist='Michael Jackson',
                       genre=GenreVO.POP,
                       date=1982,
                       artist='Michael Jackson',
                       duration=DurationVO(value=363))


@pytest.fixture(scope='session')
def mock_music_entities() -> List[MusicEntity]:
    config = inject.instance(BaseConfig)
    root_dir = config.FILE_MUSIC_ROOT_DIRECTORY

    with open(root_dir / Path("Pop/Michael Jackson/Thriller/Wanna Be Startin' Somethin'.flac"), 'rb') as f:
        body1 = f.read()

    with open(root_dir / Path('Pop/Michael Jackson/Thriller/Baby Be Mine.flac'), 'rb') as f:
        body2 = f.read()

    return [
        MusicEntity(path=Path("Pop/Michael Jackson/Thriller/Wanna Be Startin' Somethin'.flac"),
                    body=body1,
                    track_number=1,
                    title="Wanna Be Startin' Somethin'",
                    cover=cover1,
                    album_artist='Michael Jackson',
                    genre=GenreVO.POP,
                    date=1982,
                    artist='Michael Jackson',
                    duration=DurationVO(value=363)),
        MusicEntity(path=Path('Pop/Michael Jackson/Thriller/Baby Be Mine.flac'),
                    body=body2,
                    track_number=2,
                    title='Baby Be Mine',
                    cover=cover2,
                    album_artist='Michael Jackson',
                    genre=GenreVO.POP,
                    date=1982,
                    artist='Michael Jackson',
                    duration=DurationVO(value=260))
    ]
