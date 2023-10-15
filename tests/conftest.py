import pytest
import os

from models.account.create_user import GenerateUser
from core.api.account.create_user import CreateUser
from core.api.account.generate_token import GenerateToken
from core.common.assertions import Assertions
from core.common.logger import Logger


@pytest.fixture(scope='function', autouse=True)
def start_mess():
    Logger.get_instance().logger.info(f'Start testing for {os.environ.get("PYTEST_CURRENT_TEST")}')
    yield
    Logger.get_instance().logger.info(f'Finish testing for {os.environ.get("PYTEST_CURRENT_TEST")}')


@pytest.fixture
def generate_valid_cred_for_user_creation():
    """ Generate valid credential for user creation"""
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    user_data = GenerateUser.generate_user()
    return headers, user_data


@pytest.fixture
def create_user_fix(generate_valid_cred_for_user_creation):
    """ Create new random user """
    headers, user_data = generate_valid_cred_for_user_creation

    response = CreateUser(headers, user_data).create_user()
    Assertions.assert_response_status_code(response, 201)

    user_id = response.response_json['userID']

    return headers, user_data, user_id


@pytest.fixture
def generate_token_fix(create_user_fix):
    """ Generate Bearer-token for created user """
    headers, user_data, user_id = create_user_fix

    response = GenerateToken(headers, user_data).generate_token()
    Assertions.assert_response_status_code(response, 200)

    token = response.response_json['token']
    return headers, user_data, user_id, token

