from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    FILE_MUSIC_ROOT_DIRECTORY = Path('C:\\Users\\tjrwn\\Music')
