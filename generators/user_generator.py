from faker import Faker
from models.account import User

Fake = Faker('en_US')
Faker.seed()


def generate_user():
    yield User(
        NAME=Fake.first_name(),
        PASSWORD=Fake.password(length=10, special_chars=True, digits=True,
                                upper_case=True, lower_case=True))

