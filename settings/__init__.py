from functools import lru_cache

import inject

from settings.ioc_container import initialize_ioc
from settings.config import BaseConfig


initialize_ioc()


@lru_cache()
def get_current_config():
    return inject.instance(BaseConfig)


config = get_current_config()
