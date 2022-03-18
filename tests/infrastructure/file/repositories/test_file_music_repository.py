from types import GeneratorType
from pathlib import Path

from settings import config
from domain.dto.tag_dto import TagDTO
from domain.entity.music_entity import MusicEntity
from infrastructure.file.repository.file_music_repository import FileMusicRepository


def test_check_type_music_entities():
    repository = FileMusicRepository()
    music_entities = repository.get_all()

    assert isinstance(music_entities, GeneratorType)


def test_get_all_musics_when_success(mock_music_entities):
    repository = FileMusicRepository()
    music_entities = repository.get_all()

    for music_entity in music_entities:
        assert music_entity in mock_music_entities


def test_get_all_musics_when_fail(mock_music_entities):
    repository = FileMusicRepository()
    music_entities = repository.get_all()

    count = 0
    total = 0

    for music_entity in music_entities:
        total += 1
        if music_entity not in mock_music_entities[1:]:
            count += 1

    assert count >= 1
    assert total != count


def test_get_music(mock_music_entity):
    repository = FileMusicRepository()
    music_entity = repository.get(mock_music_entity.path)

    assert music_entity == mock_music_entity


def test_convert_title_tag(mock_music_entity):
    title = ' \\  / :   * ?? "<*>:  '
    tag_dto = TagDTO(title=title)
    repository = FileMusicRepository()
    music_entity = repository.convert_tags(mock_music_entity, tag_dto)

    assert music_entity.title == title
    assert music_entity.path.name == '＼／： ＊？？”＜＊＞： '


def test_convert_filename():
    title = ' \\  / :   * ?? "<*>:  '
    repository = FileMusicRepository()
    music_entity = repository.convert_path_safely_on_os(MusicEntity(title=title))

    assert music_entity.path.name == '＼／： ＊？？”＜＊＞： '


def test_convert_filename_tag_when_deleted_space():
    title = '\\/:*??"<*>:'
    repository = FileMusicRepository()
    music_entity = repository.convert_path_safely_on_os(MusicEntity(title=title))

    assert music_entity.path.name == '＼／：＊？？”＜＊＞：'


def test_save_music(mock_music_entity, tmp_music_dir):
    music_entity = FileMusicRepository().save(mock_music_entity, target=tmp_music_dir)

    assert music_entity.path.is_file()
