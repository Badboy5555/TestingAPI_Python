import json


class ResponseModel:
    def __init__(self, status_code: int, response: json):
        self.status_code = status_code
        self.response_json = response
