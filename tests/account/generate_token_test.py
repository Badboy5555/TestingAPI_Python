from core.api.account.generate_token import GenerateToken
from core.common.assertions import Assertions


class TestAccountGenerateToken:
    def test_user_exists(self, create_user_fix):
        """
        1. Try to generate token for existing user
         1.1. Create user via valid credentials
         1.2. Generate token for not existing user via not existing userName
        2. Check status code is 200
        3. Check response
        """

        # Create new random user
        self.headers, self.user_data, self.user_id = create_user_fix

        # Generate Bearer-token for created user
        response = GenerateToken(self.headers, self.user_data).generate_token()

        Assertions.assert_response_status_code(response, 200)

    def test_user_not_exists(self, create_user_fix):
        """
        1. Try to generate token for not existing user
         1.1. Create user via valid credentials
         1.2. Generate token for not existing user via not existing userName
        2. Check status code is 400
        3. Check response
        """

        # Create new random user
        self.headers, self.user_data, self.user_id = create_user_fix
        self.user_data['userName'] = '198nme'

        # Generate Bearer-token for created user
        response = GenerateToken(self.headers, self.user_data).generate_token()

        Assertions.assert_response_status_code(response, 400)  # ручка возвращает 200
