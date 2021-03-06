import shutil
from typing import List
from pathlib import Path

import pytest

from settings import config
from domain.entity.music_entity import MusicEntity
from domain.vo.genre_vo import GenreVO
from domain.vo.duration_vo import DurationVO
from tests.album_covers import cover1, cover2


@pytest.fixture(scope='session')
def mock_music_entity() -> MusicEntity:
    root_dir = config.MUSIC_DIR

    with open(root_dir / Path("Pop/Michael Jackson/Thriller/Wanna Be Startin' Somethin'.flac"), 'rb') as f:
        body = f.read()

    return MusicEntity(path=root_dir / Path("Pop/Michael Jackson/Thriller/Wanna Be Startin' Somethin'.flac"),
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
    root_dir = config.MUSIC_DIR

    with open(root_dir / Path("Pop/Michael Jackson/Thriller/Wanna Be Startin' Somethin'.flac"), 'rb') as f:
        body1 = f.read()

    with open(root_dir / Path('Pop/Michael Jackson/Thriller/Baby Be Mine.flac'), 'rb') as f:
        body2 = f.read()

    return [
        MusicEntity(path=root_dir / Path("Pop/Michael Jackson/Thriller/Wanna Be Startin' Somethin'.flac"),
                    body=body1,
                    track_number=1,
                    title="Wanna Be Startin' Somethin'",
                    cover=cover1,
                    album_artist='Michael Jackson',
                    genre=GenreVO.POP,
                    date=1982,
                    artist='Michael Jackson',
                    duration=DurationVO(value=363)),
        MusicEntity(path=root_dir / Path('Pop/Michael Jackson/Thriller/Baby Be Mine.flac'),
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


@pytest.fixture(scope='session')
def tmp_music_dir():
    return config.MUSIC_DIR.parent / Path('tmp')


def pytest_sessionfinish(session, exitstatus):
    shutil.rmtree(config.MUSIC_DIR.parent / Path('tmp'))
