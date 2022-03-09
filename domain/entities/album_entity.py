from typing import List, Optional
from datetime import date

from pydantic import BaseModel

from domain.entities.disc_entity import DiscEntity
from domain.enums.genre_enum import Genre


class AlbumEntity(BaseModel):
    discs: List[DiscEntity] = []
    cover: bytes = b''
    album_artist: str = ''
    duration: int = 0
    date: Optional[date] = None
    genre: Optional[Genre] = None
