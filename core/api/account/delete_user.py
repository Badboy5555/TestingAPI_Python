from constants import Account_urls
from core.api.account.base import Base
from core.common.my_request import MyRequest
from models.models import ResponseModel


class DeleteUser(Base):
    url = Account_urls.DELETE_USER

    def __init__(self, headers, user_id, url=url):
        self.url = url + user_id
        self.headers = headers

    def delete_user(self) -> ResponseModel:
        response = MyRequest.delete(self.url, headers=self.headers)
        return ResponseModel(status_code=self.get_status_code(response), response=response.request.url)
