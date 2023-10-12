import json
from core.logger import Logger
from core.my_request import Myrequest
from models.models import ResponseModel


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


class CreateUser(Base):

    def __init__(self, url, headers, body):
        self.url = url
        self.headers = headers
        self.body = body

    def create_user(self) -> ResponseModel:
        response = Myrequest.post(self.url, self.headers, self.body)
        return ResponseModel(status_code=self.get_status_code(response), response=self.get_json(response))


class GenerateToken(Base):

    def __init__(self, url, headers, body):
        self.url = url
        self.headers = headers
        self.body = body

    def generate_token(self) -> ResponseModel:
        response = Myrequest.post(self.url, self.headers, self.body)
        return ResponseModel(status_code=self.get_status_code(response), response=self.get_json(response))


class AuthorizeUser(Base):

    def __init__(self, url, headers, body):
        self.url = url
        self.headers = headers
        self.body = body

    def authorise_user(self) -> ResponseModel:
        response = Myrequest.post(self.url, self.headers, self.body)
        return ResponseModel(status_code=self.get_status_code(response), response=self.get_json(response))


class GetUser(Base):

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get_user(self) -> ResponseModel:
        response = Myrequest.get(self.url, headers=self.headers)
        return ResponseModel(status_code=self.get_status_code(response), response=self.get_json(response))


class DeleteUser(Base):

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def delete_user(self) -> ResponseModel:
        response = Myrequest.delete(self.url, headers=self.headers)
        return ResponseModel(status_code=self.get_status_code(response), response=response.request.url)
