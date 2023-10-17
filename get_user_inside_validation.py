from constants import Account_urls
from core.api.account.base import Base
from core.common.my_request import MyRequest
from models.models import ResponseModel
from models.account.get_user import ValidResponse, ErrorResponse
from pydantic import ValidationError
from core.common.logger import Logger

class GetUser(Base):
    url = Account_urls.GET_USER

    def __init__(self, headers, user_id, url=url):
        self.url = url + user_id
        self.headers = headers

    def get_user(self) -> ResponseModel:
        response = MyRequest.get(self.url, headers=self.headers)
        
        self.response_json = self.get_json(response)
        try:
            if not ValidResponse.model_validate(self.response_json):
                ErrorResponse.model_validate(self.response_json)
        except ValidationError:
            Logger.get_instance().logger.critical(f'Response schema is not valid {self.response_json}',
                                                  exc_info=True)
            raise Exception('Response schema is not valid')
                
        return ResponseModel(status_code=self.get_status_code(response), response=self.response_json)

