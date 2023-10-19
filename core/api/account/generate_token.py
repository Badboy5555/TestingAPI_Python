from core.api.account.base import Base
from core.common.constants import Account_urls
from core.common.my_request import MyRequest
from core.common.my_validator import MyValidator
from models.account.base import BaseValidResponse
from models.account.generate_token import ErrorResponse, ValidResponse


class GenerateToken(Base):
    url = Account_urls.GENERATE_TOKEN

    def __init__(self, headers, body, url=url):
        self.url = url
        self.headers = headers
        self.body = body

    def generate_token(self) -> BaseValidResponse:
        response = MyRequest.post(self.url, self.headers, self.body)
        response_json = self.get_json(response)

        MyValidator.validate(response_json, ValidResponse, ErrorResponse)

        return BaseValidResponse(status_code=self.get_status_code(response), response=response_json)
