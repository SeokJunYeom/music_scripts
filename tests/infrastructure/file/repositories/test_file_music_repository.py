from types import GeneratorType

from infrastructure.file.repository.file_music_repository import FileMusicRepository


def test_get_all_musics(music_entities):
    repository = FileMusicRepository()
    musics = repository.get_all_musics()

    list_music_entities = list(music_entities)

    assert isinstance(musics, GeneratorType)
    for music in musics:
        assert music in list_music_entities
