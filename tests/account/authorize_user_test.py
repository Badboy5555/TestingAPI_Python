from core.api.account.authorize_user import AuthorizeUser

from core.common.assertions import Assertions


class TestAccountAuthorized:

    def test_user_authorized(self, generate_token_fix):
        # Create new random user
        self.headers, self.user_data, self.user_id, self.token = generate_token_fix

        # Authorize
        response = AuthorizeUser(self.headers, self.user_data).authorise_user()

        Assertions.assert_response_status_code(response, 200)
        Assertions.assert_response_is_true(response)
