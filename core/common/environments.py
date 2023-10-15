import os

from pydantic import BaseModel, Field
from core.common.logger import Logger


# class Environ:
#     """ Returns needed api version for testing """
#
#     def __init__(self):
#         self.api_version = self._get_env_api_version()
#
#     @staticmethod
#     def _get_env_api_version():
#         default_api_version = 'v1'
#         try:
#             return os.environ['api_version']
#         except KeyError:
#             Logger.get_instance().logger.info(f'No api_version was passed -> '
#                                               f'used default api version: {default_api_version}')
#             return default_api_version

# ENV = Environ()

class Environ(BaseModel):
    """ Returns needed api version for testing """
    api_version: str = Field('v1', env='api_version')

    @staticmethod
    def get_env_api_version():
        api_version = Environ().api_version
        if api_version != 'v1':
            return api_version
        Logger.get_instance().logger.info(f'No api_version was passed -> '
                                          f'used default api version: {api_version}')
        return api_version

