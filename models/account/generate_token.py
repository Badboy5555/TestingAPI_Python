from pydantic import BaseModel, Field


class ValidResponse(BaseModel):
    token: str = Field(pattern=r"[a-zA-z0-9.-_]")
    expires: str
    status: str = "Success"
    result: str = "CreateUser authorized successfully."


class ErrorResponse(BaseModel):
    token: None
    expires: None
    status: str = 'Failed'
    result: str = 'CreateUser authorization failed.'
