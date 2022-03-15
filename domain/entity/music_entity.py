from typing import Optional
from pathlib import Path

from pydantic import BaseModel

from domain.vo.genre_vo import GenreVO
from domain.vo.duration_vo import DurationVO


class MusicEntity(BaseModel):
    path: Path = Path()
    body: bytes = b''
    disc_number: int = 0
    track_number: int = 0
    title: str = ''
    cover: bytes = b''
    album_artist: str = ''
    genre: Optional[GenreVO] = None
    date: int = 0
    artist: str = ''
    duration: DurationVO = DurationVO(value=0)
