from core.api.account.get_user import GetUser
from models.account.get_user import ValidResponse, ErrorResponse
from constants import ResponseErros
from schemas.account.get_user_schema import user_exists_schema as get_user_user_exists_schema

from core.common.assertions import Assertions


class TestAccountGetUser:

    def test_user_exist(self, generate_token_fix):
        # Generate Bearer-token for created user
        self.headers, self.user_id, self.token = generate_token_fix

        # Get user
        self.headers.update({'Authorization': f'Bearer {self.token}'})

        response = GetUser(self.user_id, self.headers).get_user()

        Assertions.assert_response_status_code(response, 200)
        assert ValidResponse.model_validate(response.response_json)
        Assertions.assert_response_valid_schema(response, get_user_user_exists_schema)

