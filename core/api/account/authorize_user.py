from core.api.account.base import Base
from core.common.constants import Account_urls
from core.common.my_request import MyRequest
from core.common.my_validator import MyValidator
from models.account.authorize_user import ValidResponse
from models.account.base import BaseErrorResponse, BaseValidResponse


class AuthorizeUser(Base):
    url = Account_urls.AUTHORIZE_USER

    def __init__(self, headers, body, url=url):
        self.url = url
        self.headers = headers
        self.body = body

    def authorize_user(self) -> BaseValidResponse:
        response = MyRequest.post(self.url, self.headers, self.body)
        response_json = self.get_json(response)

        MyValidator.validate_empty_or_bool(response_json, ValidResponse, BaseErrorResponse)

        return BaseValidResponse(status_code=self.get_status_code(response), response=response_json)
