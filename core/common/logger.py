import logging

from requests import Response


class Logger:
    instance = None
    logger = None
    path = 'logger.log'

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel('INFO')

        handler = logging.FileHandler(self.path)
        handler.setLevel('INFO')

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s >>>> %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    def log_request(self, method: str, url: str, headers: dict, data: dict, cookies: dict):
        current_data = '\n--Request data--\n'
        current_data += f'Method: {method}\n'
        current_data += f'Url: {url}\n'
        current_data += f'Headers: {headers}\n'
        current_data += f'Data: {data}\n'
        current_data += f'Cookies: {cookies}\n'
        current_data += '--End request data--'

        self.logger.info(current_data)

    def log_response(self, response: Response):
        current_data = '\n--Response data--\n'
        current_data += f'Satus code: {response.status_code}\n'
        current_data += f'Data: {response.text}\n'
        current_data += f'Headers: {dict(response.headers)}\n'
        current_data += f'Cookies: {dict(response.cookies)}\n'
        current_data += '--End response data--'

        self.logger.info(current_data)

    @staticmethod
    def clean_log_file(file: str = path):
        open(file, 'w').close()
        Logger.get_instance().logger.info('Log was cleaned.')
