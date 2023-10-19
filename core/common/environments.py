# from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from core.common.logger import Logger


# class Environ(BaseSettings):
class Environ(BaseSettings):
    """Returns needed api version for testing"""

    API_VERSION: str = 'v1'
    model_config = SettingsConfigDict(env_file='../../cfg.env', env_file_encoding='utf-8')

    @staticmethod
    def get_env_api_version() -> str:
        API_VERSION = Environ().API_VERSION
        if API_VERSION != 'v1':
            return API_VERSION
        Logger.get_instance().logger.info(f'No api_version was passed -> ' f'used default api version: {API_VERSION}')
        return API_VERSION


Env = Environ()
