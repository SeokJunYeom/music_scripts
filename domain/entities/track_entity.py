from pydantic import BaseModel


class TrackEntity(BaseModel):
    track_number: int = 0
    title: str = ''
    artist: str = ''
    duration: int = 0

    def get_duration_string(self) -> str:
        if self.duration >= 3600:
            return f'{self.duration // 3600}:{self.duration % 3600 // 60:02}:{self.duration % 60}'

        elif self.duration >= 60:
            return f'{self.duration // 60}:{self.duration % 60:02}'

        return str(self.duration)
