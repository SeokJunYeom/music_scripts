from functools import lru_cache

from settings.base import Settings


@lru_cache
def get_setting():
    return Settings()
