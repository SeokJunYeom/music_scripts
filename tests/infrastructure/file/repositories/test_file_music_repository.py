from types import GeneratorType
from pathlib import Path

from settings import config
from infrastructure.file.repository.file_music_repository import FileMusicRepository


def test_check_type_music_entities():
    repository = FileMusicRepository()
    music_entities = repository.get_all_musics()

    assert isinstance(music_entities, GeneratorType)


def test_get_all_musics_when_success(mock_music_entities):
    repository = FileMusicRepository()
    music_entities = repository.get_all_musics()

    for music_entity in music_entities:
        assert music_entity in mock_music_entities


def test_get_all_musics_when_fail(mock_music_entities):
    repository = FileMusicRepository()
    music_entities = repository.get_all_musics()

    count = 0
    total = 0

    for music_entity in music_entities:
        total += 1
        if music_entity not in mock_music_entities[1:]:
            count += 1

    assert count >= 1
    assert total != count


def test_get_music(mock_music_entity):
    root_dir = config.FILE_MUSIC_ROOT_DIRECTORY
    path = root_dir / Path("Pop/Michael Jackson/Thriller/Wanna Be Startin' Somethin'.flac")
    repository = FileMusicRepository()
    music_entity = repository.get_music(path)

    assert music_entity == mock_music_entity
