from core.api.account.create_user import CreateUser
from models.account.create_user import ValidResponse, ErrorResponse
from constants import ResponseErros

from core.common.assertions import Assertions


class TestAccountCreateUser:

    def test_valid_credentials(self, generate_valid_cred_for_user_creation):
        self.headers, self.user_data = generate_valid_cred_for_user_creation

        response = CreateUser(self.headers, self.user_data).create_user()

        Assertions.assert_response_status_code(response, 201)
        assert ValidResponse.model_validate(response.response_json)
        Assertions.assert_json_value_by_username(response, self.user_data['userName'])

    def test_double_valid_credentials(self, create_user_fix):
        # Create new random user
        self.headers, self.user_data, self.user_id = create_user_fix

        # Create user via same credentials
        response = CreateUser(self.headers, self.user_data).create_user()

        Assertions.assert_response_status_code(response, 406)
        assert ErrorResponse.model_validate(ResponseErros.USER_EXISTS), 'CreateUser exists'

    def test_invalid_password(self, generate_valid_cred_for_user_creation):
        self.headers, self.user_data = generate_valid_cred_for_user_creation
        self.user_data['password'] = '14'

        response = CreateUser(self.headers, self.user_data).create_user()

        Assertions.assert_response_status_code(response, 400)
        assert ErrorResponse.model_validate(ResponseErros.INVALID_PASSWORD), 'Invalid password was entered'

    def test_no_username(self, generate_valid_cred_for_user_creation):
        self.headers, self.user_data = generate_valid_cred_for_user_creation
        self.user_data['userName'] = ''

        response = CreateUser(self.headers, self.user_data).create_user()

        Assertions.assert_response_status_code(response, 400)
        assert ErrorResponse.model_validate(ResponseErros.EMPTY_USER_NAME_OR_PASSWORD), 'Username wasn\'t entered'