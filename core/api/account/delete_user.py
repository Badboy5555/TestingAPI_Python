from core.api.account.base import Base
from core.common.constants import Account_urls
from core.common.my_request import MyRequest
from core.common.my_validator import MyValidator
from models.account.base import BaseErrorResponse, BaseValidResponse
from models.account.generate_token import ValidResponse


class DeleteUser(Base):
    url = Account_urls.DELETE_USER

    def __init__(self, headers, user_id, url=url):
        self.url = url + user_id
        self.headers = headers

    def delete_user(self) -> BaseValidResponse:
        response = MyRequest.delete(self.url, headers=self.headers)
        response_json = self.get_json(response)

        MyValidator.validate_empty_or_bool(response_json, ValidResponse, BaseErrorResponse)

        return BaseValidResponse(status_code=self.get_status_code(response), response=response_json)
