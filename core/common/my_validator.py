from pydantic import ValidationError

from core.common.logger import Logger
from models.account.base import BaseValidResponse


class MyValidator:
    """Just a wrapper for pydantic model_validate method"""

    @staticmethod
    def validate(response_json: BaseValidResponse, valid_response, error_response):
        try:
            if not valid_response.model_validate(response_json):
                error_response.model_validate(response_json)
        except ValidationError:
            Logger.get_instance().logger.critical(f'Response schema is not valid {response_json}', exc_info=True)
            raise Exception('Response schema is not valid')

    @staticmethod
    def validate_empty_or_bool(response_json: BaseValidResponse, valid_response, error_response):
        """Validate authorize and delete handles"""
        try:
            if type(response_json) is not bool or response_json:
                error_response.model_validate(response_json)
        except ValidationError:
            Logger.get_instance().logger.critical(f'Response schema is not valid {response_json}', exc_info=True)
            raise Exception('Response schema is not valid')
