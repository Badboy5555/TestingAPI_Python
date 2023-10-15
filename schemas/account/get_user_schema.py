user_exists_schema = {
    "type": "object",
    "properties": {
        "userId": {
            "type": "string",
            "pattern": "[0-9A-Za-z]{8}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{12}"},
        "username": {"type": "string"},
        "books": {"type": ["array", "null"], "anyof":[{"type":"object"}]}
    },
    "required": ["userId", "username", "books"],
    "additionalProperties": False
}

