import os
from pathlib import Path

from pydantic import BaseSettings


class BaseConfig(BaseSettings):
    BASEDIR: str = ''
    FILE_MUSIC_ROOT_DIRECTORY: Path = Path()
    FILE_STORAGE_ROOT_DIRECTORY: Path = Path()


class LocalConfig(BaseConfig):
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

    if _FILE_MUSIC_ROOT_DIRECTORY := os.environ.get('FILE_MUSIC_ROOT_DIRECTORY'):
        pass
    elif user_profile := os.environ.get('USERPROFILE'):
        _FILE_MUSIC_ROOT_DIRECTORY = Path(user_profile) / Path('music')
    else:
        _FILE_MUSIC_ROOT_DIRECTORY = ''

    FILE_MUSIC_ROOT_DIRECTORY = _FILE_MUSIC_ROOT_DIRECTORY

    # FILE_STORAGE_ROOT_DIRECTORY = os.environ.get('FILE_MUSIC_ROOT_DIRECTORY', '')


class TestConfig(BaseConfig):
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent / Path('tests')
    FILE_MUSIC_ROOT_DIRECTORY = BASE_DIR / Path('mock_files')
    FILE_STORAGE_ROOT_DIRECTORY = BASE_DIR / Path('tmp')
