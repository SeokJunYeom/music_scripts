from infrastructure.file.repository.file_music_repository import FileMusicRepository


def test_get_all_musics(music_entities):
    repository = FileMusicRepository()
    musics = repository.get_all_musics()

    for music in musics:
        assert music in music_entities
