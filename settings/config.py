import os
from pathlib import Path

from pydantic import BaseSettings


class BaseConfig(BaseSettings):
    BASE_DIR: Path = ''
    MUSIC_DIR: Path = Path()


class LocalConfig(BaseConfig):
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

    if _FILE_MUSIC_DIR := os.environ.get('FILE_MUSIC_ROOT_DIRECTORY'):
        pass
    elif user_profile := os.environ.get('USERPROFILE'):
        _FILE_MUSIC_DIR = Path(user_profile) / Path('music')
    else:
        _FILE_MUSIC_DIR = ''

    MUSIC_DIR = _FILE_MUSIC_DIR


class TestConfig(BaseConfig):
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent / Path('tests')
    MUSIC_DIR = BASE_DIR / Path('mock_files')
