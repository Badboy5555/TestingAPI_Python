from jsonschema import validate

from models.account.base import BaseValidResponse


class Assertions:
    @staticmethod
    def assert_response_status_code(response: BaseValidResponse, expected_status_code: int):
        assert (
            response.status_code == expected_status_code
        ), f'Unexpected status code. Expected: {expected_status_code}, actual: {response.status_code} '

    @staticmethod
    def assert_response_valid_schema(response: BaseValidResponse, expected_schema: dict):
        assert (
            validate(instance=response.response_json, schema=expected_schema) is None
        ), f'Schema is not valid, valid schema: {expected_schema}'

    @staticmethod
    def assert_response_is_true(response: BaseValidResponse):
        assert (
            response.response_json is True
        ), f'Response "True "is expected, actual response is: {response.response_json}'

    @staticmethod
    def assert_response_is_false(response: BaseValidResponse):
        assert (
            response.response_json is False
        ), f'Response "True "is expected, actual response is: {response.response_json}'

    @staticmethod
    def assert_json_value_by_username(response: BaseValidResponse, expected_username: str):
        assert 'username' in response.response_json, 'Response doesn\'t have key "username".'
        assert response.response_json['username'] == expected_username, (
            f'Expected and actual usernames are not equal. '
            f'Expected: {expected_username}, actual: {response.response_json["username"]}.'
        )

    @staticmethod
    def assert_json_value_by_key(response: BaseValidResponse, expected_key, expected_value: str):
        assert expected_key in response.response_json, f'Response doesn\'t have key {expected_key}.'
        assert response.response_json[expected_key] == expected_value, (
            f'Expected and actual usernames are not equal. '
            f'Expected: {expected_value}, actual: {response.response_json[expected_key]}.'
        )

    @staticmethod
    def assert_valid_error_occur(response: BaseValidResponse, error_obj: dict):
        expected_code, expected_message = error_obj['code'], error_obj['message']

        actual_code = response.response_json['code']
        actual_message = response.response_json['message']

        assert actual_code == expected_code, (
            f'Message code is not valid. ' f'Actual_code: {actual_code} != {expected_code}.'
        )
        assert actual_message == expected_message, (
            f'Response message is not valid. ' f'Actual_message: {actual_message} != {expected_message}.'
        )
