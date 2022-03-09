from typing import List, Optional

from pydantic import BaseModel

from domain.entities.track_entity import TrackEntity


class DiscEntity(BaseModel):
    disc_number: Optional[int] = None
    tracks: List[TrackEntity] = []
