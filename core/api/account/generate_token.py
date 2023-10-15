from constants import Account_urls
from core.api.account.base import Base
from core.common.my_request import MyRequest
from models.models import ResponseModel


class GenerateToken(Base):
    url = Account_urls.GENERATE_TOKEN

    def __init__(self, headers, body, url=url):
        self.url = url
        self.headers = headers
        self.body = body

    def generate_token(self) -> ResponseModel:
        response = MyRequest.post(self.url, self.headers, self.body)
        return ResponseModel(status_code=self.get_status_code(response), response=self.get_json(response))
