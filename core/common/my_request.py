import requests
import allure
from constants import Bases
from core.common.environments import ENV
from core.common.logger import Logger


class MyRequest:
    """ Just a wrapper for request """

    @staticmethod
    def get(url: str, headers: dict = None, data: dict = None, cookies: dict = None):
        return MyRequest._send_request(method='GET', url=url, headers=headers, data=data, cookies=cookies)

    @staticmethod
    def post(url: str, headers: dict = None, data: dict = None, cookies: dict = None):
        return MyRequest._send_request(method='POST', url=url, headers=headers, data=data, cookies=cookies)

    @staticmethod
    def put(url: str, headers: dict = None, data: dict = None, cookies: dict = None):
        return MyRequest._send_request(method='PUT', url=url, headers=headers, data=data, cookies=cookies)

    @staticmethod
    def delete(url: str, headers: dict = None, data: dict = None, cookies: dict = None):
        return MyRequest._send_request(method='DELETE', url=url, headers=headers, data=data, cookies=cookies)

    @staticmethod
    def _send_request(method: str, url: str, headers: dict, data: dict, cookies: dict = None) -> requests.Response:

        url = Bases.BASE_URL + url.replace('api_version', ENV.api_version)

        if headers is None:
            headers = {}

        if cookies is None:
            cookies = {}

        Logger.get_instance().log_request(method, url, headers, data, cookies)

        with allure.step(f'{method} request to {url}'):
            match method:
                case 'GET':
                    response = requests.get(url, params=data, headers=headers, cookies=cookies)
                case 'POST':
                    response = requests.post(url, json=data, headers=headers, cookies=cookies)
                case 'PUT':
                    response = requests.put(url, json=data, headers=headers, cookies=cookies)
                case 'DELETE':
                    response = requests.delete(url, headers=headers, cookies=cookies)
                case _:
                    Logger.get_instance().logger.critical(f'Bad HTTP method "{method}" was received', exc_info=True)
                    raise Exception(f'Bad HTTP method "{method}" was received')
        Logger.get_instance().log_response(response)
        return response
