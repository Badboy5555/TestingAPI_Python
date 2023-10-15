from pydantic import BaseModel, Field


class ValidResponse(BaseModel):
    userId: str = Field(pattern="[0-9A-Za-z]{8}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{12}")
    username: str
    books: list


class ErrorResponse(BaseModel):
    code: str
    message: str



