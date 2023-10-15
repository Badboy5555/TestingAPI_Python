import json
from core.common.logger import Logger


class Base:
    def get_status_code(self, response):
        return response.status_code

    def get_json(self, response):
        try:
            return response.json()
        except json.JSONDecodeError:
            Logger.get_instance().logger.critical(f'Can\'t convert response to JSON format {response.text}',
                                                  exc_info=True)
            raise Exception('Can\'t convert response to JSON format')