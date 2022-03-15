from infrastructure.file.repository.file_storage_repository import FileStorageRepository


def test_save_new_music():
    FileStorageRepository().save()
