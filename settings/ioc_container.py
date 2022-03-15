import os

import inject

from settings.config import BaseConfig, LocalConfig, TestConfig


def local_bind(binder):
    binder.bind_to_provider(BaseConfig, LocalConfig)


def test_bind(binder):
    binder.bind_to_provider(BaseConfig, TestConfig)


def initialize_ioc():
    environment = os.environ.get('PROJECT_ENV')

    if environment == 'test':
        inject.clear_and_configure(lambda binder: test_bind(binder))
    else:
        inject.configure(lambda binder: local_bind(binder))
