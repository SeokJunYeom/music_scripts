from settings import config
from infrastructure.file.repository.file_storage_repository import FileStorageRepository


def test_save_music(mock_music_entity):
    FileStorageRepository().save(mock_music_entity)

    assert (config.FILE_STORAGE_ROOT_DIRECTORY / mock_music_entity.path).is_file()
