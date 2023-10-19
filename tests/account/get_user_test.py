from core.api.account.get_user import GetUser
from core.common.assertions import Assertions
from core.common.constants import ResponseErrors


class TestAccountGetUser:
    def test_user_exists(self, generate_token_fix):
        """
        1. Try to get existing user
         1.1. Create user via valid credentials
         1.2. Get not existing user via existing user_id
        2. Check status code is 200
        3. Check response
        """

        # Generate Bearer-token for created user
        self.headers, self.user_data, self.user_id, self.token = generate_token_fix

        # Get user
        self.headers.update({'Authorization': f'Bearer {self.token}'})

        response = GetUser(self.headers, self.user_id).get_user()

        Assertions.assert_response_status_code(response, 200)

    def test_user_not_exists(self, generate_token_fix):
        """
        1. Try to get not existing user
         1.1. Create user via valid credentials
         1.2. Get not existing user via not existing user_id
        2. Check status code is 401
        3. Check response
        """

        # Generate Bearer-token for created user
        self.headers, self.user_data, self.user_id, self.token = generate_token_fix

        # Get user
        self.headers.update({'Authorization': f'Bearer {self.token}'})
        self.user_id = 'not_valid_user_id'

        response = GetUser(self.headers, self.user_id).get_user()

        Assertions.assert_response_status_code(response, 401)
        Assertions.assert_valid_error_occur(response, ResponseErrors.USER_NOT_AUTHORIZED)
