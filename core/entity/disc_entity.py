from typing import List, Optional

from pydantic import BaseModel

from core.entity.track_entity import TrackEntity


class DiscEntity(BaseModel):
    disc_number: Optional[int, None] = None
    tracks: List[TrackEntity]
