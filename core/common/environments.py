import os
from core.common.logger import Logger


class Environ:
    """ Returns needed api version for testing """

    def __init__(self):
        self.api_version = self._get_env_api_version()

    @staticmethod
    def _get_env_api_version():
        default_api_version = 'v1'
        try:
            return os.environ['api_version']
        except KeyError:
            Logger.get_instance().logger.info(f'No api_version was passed -> '
                                              f'used default api version: {default_api_version}')
            return default_api_version


ENV = Environ()
