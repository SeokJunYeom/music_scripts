import os
from functools import lru_cache

from settings.base import Settings, TestSettings


@lru_cache
def _get_setting():
    env = os.environ.get('PROJECT_ENV')
    if env == 'test':
        print('asd')
        return TestSettings()
    return Settings()


settings = _get_setting()
