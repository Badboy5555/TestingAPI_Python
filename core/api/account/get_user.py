from constants import Account_urls
from core.api.account.base import Base
from core.common.my_request import MyRequest
from models.models import ResponseModel


class GetUser(Base):
    url = Account_urls.GET_USER

    def __init__(self, headers, user_id, url=url):
        self.url = url + user_id
        self.headers = headers

    def get_user(self) -> ResponseModel:
        response = MyRequest.get(self.url, headers=self.headers)
        return ResponseModel(status_code=self.get_status_code(response), response=self.get_json(response))

