from types import GeneratorType

from infrastructure.file.repository.file_music_repository import FileMusicRepository


def test_check_type_music_entities():
    repository = FileMusicRepository()
    musics = repository.get_all_musics()

    assert isinstance(musics, GeneratorType)


def test_get_all_musics_when_success(music_entities):
    repository = FileMusicRepository()
    musics = repository.get_all_musics()
    list_music_entities = list(music_entities)

    for music in musics:
        assert music in list_music_entities


def test_get_all_musics_when_fail(music_entities):
    repository = FileMusicRepository()
    musics = repository.get_all_musics()
    list_music_entities = list(music_entities)
    list_music_entities.pop()

    count = 0

    for music in musics:
        if music not in list_music_entities:
            count += 1

    assert count >= 1
