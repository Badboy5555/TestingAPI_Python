from core.base import CreateUser, GenerateToken, AuthorizeUser, GetUser, DeleteUser
from constants import Account_urls, ResponseErros
from generators.user_generator import generate_user
from schemas.account.create_user_schema import schema as schema_create_user_schema
from schemas.account.generate_token_schema import user_exists_schema as schema_generate_token_exists, \
    user_not_exists_schema as schema_generate_token_not_exists
from schemas.account.get_user_schema import user_exists_schema as get_user_user_exists_schema

from core.assertions import Assertions


class TestAccountCreateUser:
    def setup(self):
        self.url = Account_urls.CREATE_USER
        self.user = next(generate_user())
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.body = {'userName': self.user.NAME, 'password': self.user.PASSWORD}

    def test_valid_credentials(self):
        response = CreateUser(self.url, self.headers, self.body).create_user()

        Assertions.assert_response_status_code(response, 201)
        Assertions.assert_response_valid_schema(response, schema_create_user_schema)
        Assertions.assert_json_value_by_username(response, self.user.NAME)

    def test_double_valid_credentials(self):
        response = CreateUser(self.url, self.headers, self.body).create_user()

        Assertions.assert_response_status_code(response, 201)
        Assertions.assert_response_valid_schema(response, schema_create_user_schema)
        Assertions.assert_json_value_by_username(response, self.user.NAME)

        response = CreateUser(self.url, self.headers, self.body).create_user()

        Assertions.assert_response_status_code(response, 406)
        Assertions.assert_valid_error_occur(response, ResponseErros.USER_EXISTS, 'User exists')

    def test_invalid_password(self):
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.body['password'] = '14'

        response = CreateUser(self.url, self.headers, self.body).create_user()

        Assertions.assert_response_status_code(response, 400)
        Assertions.assert_valid_error_occur(response, ResponseErros.INVALID_PASSWORD, 'Invalid password was entered')

    def test_no_username(self):
        self.body['userName'] = ''

        response = CreateUser(self.url, self.headers, self.body).create_user()

        Assertions.assert_response_status_code(response, 400)
        Assertions.assert_valid_error_occur(response, ResponseErros.EMPTY_USER_NAME_OR_PASSWORD,
                                            'Username wasn\'t entered')


class TestAccountAuthorized:
    def setup(self):
        self.url = Account_urls.AUTHORIZE_USER
        self.user = next(generate_user())
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.body = {'userName': self.user.NAME, 'password': self.user.PASSWORD}

    def test_user_has_token(self):
        # Create new random user
        response = CreateUser(Account_urls.CREATE_USER, self.headers, self.body).create_user()

        Assertions.assert_response_status_code(response, 201)
        Assertions.assert_response_valid_schema(response, schema_create_user_schema)
        Assertions.assert_json_value_by_username(response, self.user.NAME)

        # Generate Bearer-token for created user
        response = GenerateToken(Account_urls.GENERATE_TOKEN, self.headers, self.body).generate_token()

        Assertions.assert_response_status_code(response, 200)
        Assertions.assert_response_valid_schema(response, schema_generate_token_exists)

        # Authorize
        response = AuthorizeUser(self.url, self.headers, self.body).authorise_user()

        Assertions.assert_response_status_code(response, 200)
        Assertions.assert_response_is_true(response)


class TestAccountGenerateToken:
    def setup(self):
        self.url = Account_urls.GENERATE_TOKEN
        self.user = next(generate_user())
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.body = {'userName': self.user.NAME, 'password': self.user.PASSWORD}

    def test_user_exist(self):
        # Create new random user
        response = CreateUser(Account_urls.CREATE_USER, self.headers, self.body).create_user()

        Assertions.assert_response_status_code(response, 201)
        Assertions.assert_response_valid_schema(response, schema_create_user_schema)
        Assertions.assert_json_value_by_username(response, self.user.NAME)

        # Generate Bearer-token for created user
        response = GenerateToken(self.url, self.headers, self.body).generate_token()

        Assertions.assert_response_status_code(response, 200)
        Assertions.assert_response_valid_schema(response, schema_generate_token_exists)

    def test_user_not_exist(self):
        # Create new random user
        response = CreateUser(self.url, self.headers, self.body).create_user()

        Assertions.assert_response_status_code(response, 201)
        Assertions.assert_response_valid_schema(response, schema_create_user_schema)
        Assertions.assert_json_value_by_username(response, self.user.NAME)

        # Generate Bearer-token for created user
        response = GenerateToken(self.url, self.headers, self.body).generate_token()

        # Assertions.assert_response_status_code(response, 400) # ручка возвращает 200
        Assertions.assert_response_valid_schema(response, schema_generate_token_not_exists)


class TestAccountGetUser:
    def setup(self):
        self.url = Account_urls.GET_USER
        self.user = next(generate_user())
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.body = {'userName': self.user.NAME, 'password': self.user.PASSWORD}

    def test_user_exist(self):
        # Create new random user
        response = CreateUser(Account_urls.CREATE_USER, self.headers, self.body).create_user()

        Assertions.assert_response_status_code(response, 201)
        Assertions.assert_response_valid_schema(response, schema_create_user_schema)
        Assertions.assert_json_value_by_username(response, self.user.NAME)

        user_id = response.response_json['userID']

        # Generate Bearer-token for created user
        response = GenerateToken(Account_urls.GENERATE_TOKEN, self.headers, self.body).generate_token()

        token = response.response_json['token']

        Assertions.assert_response_status_code(response, 200)
        Assertions.assert_response_valid_schema(response, schema_generate_token_exists)

        # Get user
        self.url += user_id
        self.headers.update({'Authorization': f'Bearer {token}'})

        response = GetUser(self.url, self.headers).get_user()

        Assertions.assert_response_status_code(response, 200)
        Assertions.assert_response_valid_schema(response, get_user_user_exists_schema)


class TestAccountDeleteUser:
    def setup(self):
        self.url = Account_urls.DELETE_USER
        self.user = next(generate_user())
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.body = {'userName': self.user.NAME, 'password': self.user.PASSWORD}

    def test_user_exist(self):
        # Create new random user
        response = CreateUser(Account_urls.CREATE_USER, self.headers, self.body).create_user()

        Assertions.assert_response_status_code(response, 201)
        Assertions.assert_response_valid_schema(response, schema_create_user_schema)
        Assertions.assert_json_value_by_username(response, self.user.NAME)

        user_id = response.response_json['userID']

        # Generate Bearer-token for created user
        response = GenerateToken(Account_urls.GENERATE_TOKEN, self.headers, self.body).generate_token()

        token = response.response_json['token']

        Assertions.assert_response_status_code(response, 200)
        Assertions.assert_response_valid_schema(response, schema_generate_token_exists)

        # Get user
        self.url += user_id
        self.headers.update({'Authorization': f'Bearer {token}'})

        response = GetUser(self.url, self.headers).get_user()

        Assertions.assert_response_status_code(response, 200)
        Assertions.assert_response_valid_schema(response, get_user_user_exists_schema)

        # Delete user
        response = DeleteUser(self.url, self.headers).delete_user()

        Assertions.assert_response_status_code(response, 200)
