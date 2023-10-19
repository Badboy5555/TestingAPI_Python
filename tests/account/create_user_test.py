from core.api.account.create_user import CreateUser
from core.common.assertions import Assertions
from core.common.constants import ResponseErrors


class TestAccountCreateUser:
    def test_valid_credentials(self, generate_valid_cred_for_user_creation):
        """
        1. Try to create user via valid credentials
        2. Check status code is 201
        3. Check response
        """

        self.headers, self.user_data = generate_valid_cred_for_user_creation

        response = CreateUser(self.headers, self.user_data).create_user()

        Assertions.assert_response_status_code(response, 201)
        Assertions.assert_json_value_by_username(response, self.user_data['userName'])

    def test_double_valid_credentials(self, create_user_fix):
        """
        1. Try to create user via already used valid credentials
        2. Check status code is 406
        3. Check response
        """

        # Create new random user
        self.headers, self.user_data, self.user_id = create_user_fix

        # Create user via same credentials
        response = CreateUser(self.headers, self.user_data).create_user()

        Assertions.assert_response_status_code(response, 406)
        Assertions.assert_valid_error_occur(response, ResponseErrors.USER_EXISTS)

    def test_invalid_password(self, generate_valid_cred_for_user_creation):
        """
        1. Try to create user via invalid password
        2. Check status code is 400
        3. Check response
        """

        self.headers, self.user_data = generate_valid_cred_for_user_creation
        self.user_data['password'] = '14'

        response = CreateUser(self.headers, self.user_data).create_user()

        Assertions.assert_response_status_code(response, 400)
        Assertions.assert_valid_error_occur(response, ResponseErrors.INVALID_PASSWORD)

    def test_no_username(self, generate_valid_cred_for_user_creation):
        """
        1. Try to create user with no userName field
        2. Check status code is 400
        3. Check response
        """

        self.headers, self.user_data = generate_valid_cred_for_user_creation
        self.user_data['userName'] = ''

        response = CreateUser(self.headers, self.user_data).create_user()

        Assertions.assert_response_status_code(response, 400)
        Assertions.assert_valid_error_occur(response, ResponseErrors.EMPTY_USER_NAME_OR_PASSWORD)
