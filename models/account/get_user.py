from pydantic import BaseModel, Field


class ValidResponse(BaseModel):
    userID: str = Field(pattern="[0-9A-Za-z]{8}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{12}")
    username: str
    status: str
    books: str


class ErrorResponse(BaseModel):
    code: str
    message: str



