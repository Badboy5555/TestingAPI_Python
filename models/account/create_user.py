from pydantic import BaseModel, Field
from faker import Faker
from typing import Optional

Fake = Faker('en_US')
Faker.seed()


class GenerateUser(BaseModel):
    userName: str = None
    password: str = None

    @staticmethod
    def generate_user():
        name = Fake.first_name()
        password = Fake.password(length=10, special_chars=True, digits=True,
                                 upper_case=True, lower_case=True)
        return GenerateUser(userName=name, password=password).model_dump()


class ValidResponse(BaseModel):
    userID: str = Field(pattern="[0-9A-Za-z]{8}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{12}")
    username: str
    Optional[list] = None


class ErrorResponse(BaseModel):
    code: str
    message: str
