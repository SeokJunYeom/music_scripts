from domain.entity.music_entity import MusicEntity
from domain.vo.duration_vo import DurationVO


def test_music_entity_duration_field():
    music_entity = MusicEntity(duration=DurationVO(value=10))

    assert music_entity.duration.string == '10'
