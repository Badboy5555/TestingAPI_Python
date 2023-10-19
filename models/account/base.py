from pydantic import BaseModel


class BaseValidResponse:
    def __init__(self, status_code: int, response: dict):
        self.status_code = status_code
        self.response_json = response


class BaseErrorResponse(BaseModel):
    code: str = ''
    message: str = ''
