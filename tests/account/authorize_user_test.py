from core.api.account.authorize_user import AuthorizeUser
from core.common.assertions import Assertions


class TestAccountAuthorized:
    def test_user_authorized(self, generate_token_fix):
        """
        1. Try to authorize via user with Bearer-token
        2. Check status code is 200
        3. Check response
        """
        # Create new random user
        self.headers, self.user_data, self.user_id, self.token = generate_token_fix

        # Authorize
        response = AuthorizeUser(self.headers, self.user_data).authorize_user()

        Assertions.assert_response_status_code(response, 200)
        Assertions.assert_response_is_true(response)

    def test_user_not_authorized(self, generate_token_fix):
        """
        1. Try to authorize via user without Bearer-token
        2. Check status code is 200
        3. Check response
        """
        # Create new random user
        self.headers, self.user_data, self.user_id, self.token = generate_token_fix
        self.token = 'not_valid_token' ''
        # Authorize
        response = AuthorizeUser(self.headers, self.user_data).authorize_user()

        Assertions.assert_response_status_code(response, 200)
        Assertions.assert_response_is_false(response)
