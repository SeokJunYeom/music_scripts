from typing import Optional
from datetime import date

from pydantic import BaseModel

from domain.vo.genre_vo import GenreVO
from domain.vo.duration_vo import DurationVO


class MusicEntity(BaseModel):
    disc_number: int = 0
    track_number: int = 0
    title: str = ''
    cover: bytes = b''
    album_artist: str = ''
    genre: Optional[GenreVO] = None
    date: Optional[date] = None
    artist: str = ''
    duration: DurationVO = DurationVO(value=0)
