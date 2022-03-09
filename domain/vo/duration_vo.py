from pydantic import BaseModel


class DurationVO(BaseModel):
    value: int

    @property
    def string(self) -> str:
        if self.value >= 3600:
            return f'{self.value // 3600}:{self.value % 3600 // 60:02}:{self.value % 60:02}'
        elif self.value >= 60:
            return f'{self.value // 60}:{self.value % 60:02}'
        return str(self.value)

