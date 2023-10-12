user_exists_schema = {
    "type": "object",
    "properties": {
        "token": {
            "type": "string",
            "pattern": "[a-zA-z0-9.\-_]"},
        "expires": {"type": "string"},
        "status": {"type": "string", "const": "Success"},
        "result": {"type": "string", "const": "User authorized successfully."}
    },
    "required": ["token", "expires", "status", "result"],
    "additionalProperties": False
}

user_not_exists_schema = {
    "type": "object",
    "properties": {
        "token": {"type": "null"},
        "expires": {"type": "null"},
        "status": {"type": "string", "const": "Failed"},
        "result": {"type": "string", "const": "User authorization failed."}
    },
    "required": ["token", "expires", "status", "result"],
    "additionalProperties": False
}

