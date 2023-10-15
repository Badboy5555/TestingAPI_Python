from core.api.account.generate_token import GenerateToken
from constants import ResponseErros
from models.account.generate_token import ErrorResponse, ValidResponse

from core.common.assertions import Assertions


class TestAccountGenerateToken:

    def test_user_exist(self, create_user_fix):
        # Create new random user
        self.headers, self.user_data, self.user_id = create_user_fix

        # Generate Bearer-token for created user
        response = GenerateToken(self.headers, self.user_data).generate_token()

        Assertions.assert_response_status_code(response, 200)
        assert ValidResponse.model_validate(response.response_json)

    def test_user_not_exist(self, create_user_fix):
        # Create new random user
        self.headers, self.user_data, self.user_id = create_user_fix
        self.user_data['userName'] = '198nme'

        # Generate Bearer-token for created user
        response = GenerateToken(self.headers, self.user_data).generate_token()

        assert ErrorResponse.model_validate(response.response_json)
        Assertions.assert_response_status_code(response, 400) # ручка возвращает 200


