from domain.entities.track_entity import TrackEntity


def test_change_unit_of_duration_when_highest_unit_is_second():
    seconds = 1
    duration_string = '1'

    track_entity = TrackEntity(duration=seconds)

    assert duration_string == track_entity.get_duration_string()


def test_change_unit_of_duration_when_highest_unit_is_minute():
    seconds = 60*4 + 7
    duration_string = '4:07'

    track_entity = TrackEntity(duration=seconds)

    assert duration_string == track_entity.get_duration_string()


def test_change_unit_of_duration_when_highest_unit_is_hour():
    seconds = 60**2*3 + 60*8 + 52
    duration_string = '3:08:52'

    track_entity = TrackEntity(duration=seconds)

    assert duration_string == track_entity.get_duration_string()

