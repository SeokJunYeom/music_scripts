from pydantic import BaseModel


class TrackEntity(BaseModel):
    track_number: int
    title: str
    artist: str
    duration: int
