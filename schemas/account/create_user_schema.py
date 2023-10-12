schema = {
    "type": "object",
    "properties": {
        "userID": {
            "type": "string",
            "pattern": "[0-9A-Za-z]{8}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{4}-[0-9A-Za-z]{12}"},
        "username": {"type": "string"},
        "books": {"type": "array"}
    },
    "required": ["userID", "username", "books"],
    "additionalProperties": False
}