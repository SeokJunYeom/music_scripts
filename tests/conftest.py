from pathlib import Path

import pytest

from settings import settings as _settings
from domain.entity.music_entity import MusicEntity
from domain.vo.genre_vo import GenreVO
from domain.vo.duration_vo import DurationVO


@pytest.fixture(scope='session')
def settings():
    _settings.FILE_MUSIC_ROOT_DIRECTORY = _settings.BASE_DIR / Path('tests/infrastructure/file/mock_files')

    return _settings


@pytest.fixture(scope='session')
def music_entities(settings):
    root_dir = settings.FILE_MUSIC_ROOT_DIRECTORY

    with open(root_dir / Path("Pop/Michael Jackson/Thriller/Wanna Be Startin' Somethin'.cover.jpg"), 'rb') as f:
        cover1 = f.read()

    with open(root_dir / Path('Pop/Michael Jackson/Thriller/Baby Be Mine.cover.jpg'), 'rb') as f:
        cover2 = f.read()

    return [
        MusicEntity(path=root_dir / Path("Pop/Michael Jackson/Thriller/Wanna Be Startin' Somethin'.flac"),
                    track_number=1,
                    title="Wanna Be Startin' Somethin'",
                    cover=cover1,
                    album_artist='Michael Jackson',
                    genre=GenreVO.POP,
                    date=1982,
                    artist='Michael Jackson',
                    duration=DurationVO(value=363)),
        MusicEntity(path=root_dir / Path('Pop/Michael Jackson/Thriller/Baby Be Mine.flac'),
                    track_number=2,
                    title='Baby Be Mine',
                    cover=cover2,
                    album_artist='Michael Jackson',
                    genre=GenreVO.POP,
                    date=1982,
                    artist='Michael Jackson',
                    duration=DurationVO(value=260))
    ]
