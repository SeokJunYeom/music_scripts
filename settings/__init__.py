from functools import lru_cache

from settings.base import Settings


@lru_cache
def _get_setting():
    return Settings()


settings = _get_setting()
