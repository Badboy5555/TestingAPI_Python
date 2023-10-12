import logging


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
        current_data = f'\n--Request data--\n'
        current_data += f'Method: {method}\n'
        current_data += f'Url: {url}\n'
        current_data += f'Headers: {headers}\n'
        current_data += f'Data: {data}\n'
        current_data += f'Cookies: {cookies}\n'
        current_data += f'--End request data--'

        self.logger.info(current_data)

    def log_response(self, response):
        current_data = f'\n--Response data--\n'
        current_data += f'Satus code: {response.status_code}\n'
        current_data += f'Data: {response.text}\n'
        current_data += f'Headers: {dict(response.headers)}\n'
        current_data += f'Cookies: {dict(response.cookies)}\n'
        current_data += f'--End response data--'

        self.logger.info(current_data)

    def clean_log_file(self, file=path):
        open(file, 'w').close()

