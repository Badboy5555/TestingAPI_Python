from core.api.account.delete_user import DeleteUser

from core.common.assertions import Assertions


class TestAccountDeleteUser:

     def test_user_exist(self, generate_token_fix):
        # Create new random user
        self.headers, self.user_data, self.user_id, self.token = generate_token_fix

        # Delete user
        response = DeleteUser(self.headers, self.user_id).delete_user()
        print(response.response_json, response.status_code)
        Assertions.assert_response_status_code(response, 200)
