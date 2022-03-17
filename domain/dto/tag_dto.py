from pydantic import BaseModel


class TagDTO(BaseModel):
    disc_number: int = 0
    track_number: int = 0
    title: str = ''
    cover: bytes = b''
    album_artist: str = ''
    genre: str = ''
    date: int = 0
    artist: str = ''
    duration: int = 0
