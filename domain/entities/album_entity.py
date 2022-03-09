from typing import List
from datetime import date

from pydantic import BaseModel

from domain.entities.disc_entity import DiscEntity
from domain.enums.genre_enum import Genre


class AlbumEntity(BaseModel):
    discs: List[DiscEntity]
    cover: bytes
    album_artist: str
    duration: int
    date: date
    genre: Genre
