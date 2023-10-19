from core.api.account.delete_user import DeleteUser
from core.common.assertions import Assertions
from core.common.constants import ResponseErrors


class TestAccountDeleteUser:
    def test_user_exists(self, generate_token_fix):
        """
        1. Try to delete existing user
        2. Check status code is 200
        3. Check response
        """

        # Create new random user
        self.headers, self.user_data, self.user_id, self.token = generate_token_fix
        # Delete user
        response = DeleteUser(self.headers, self.user_id).delete_user()

        Assertions.assert_response_status_code(response, 200)

    def test_user_not_exists(self):
        """
        1. Try to delete not existing user
        2. Check status code is 401
        3. Check response
        """

        # Create some data
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        self.user_id = 'not_valid_user_id'

        # Delete user
        response = DeleteUser(self.headers, self.user_id).delete_user()

        Assertions.assert_response_status_code(response, 401)
        Assertions.assert_valid_error_occur(response, ResponseErrors.USER_NOT_AUTHORIZED)
