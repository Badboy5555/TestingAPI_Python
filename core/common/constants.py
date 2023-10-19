class Bases:
    BASE_URL = 'https://demoqa.com'


class Account_urls:
    AUTHORIZE_USER = '/Account/API_VERSION/Authorized'
    GENERATE_TOKEN = '/Account/API_VERSION/GenerateToken'
    CREATE_USER = '/Account/API_VERSION/User'
    DELETE_USER = '/Account/API_VERSION/User/'
    GET_USER = '/Account/API_VERSION/User/'


class ResponseErrors:
    USER_EXISTS = {"code": "1204", "message": "User exists!"}  # status code 406
    USER_NOT_FOUND = {"code": "1207", "message": "User not found!"}  # status code 401
    INVALID_PASSWORD = {
        "code": "1300",
        "message": "Passwords must have at least one non alphanumeric character, one digit ("
        "'0'-'9'),"
        " one uppercase ('A'-'Z'), one lowercase ('a'-'z'), "
        "one special character and Password must be eight characters or longer.",
    }
    # status code 400
    EMPTY_USER_NAME_OR_PASSWORD = {"code": "1200", "message": "UserName and Password required."}  # status code 400
    USER_NOT_AUTHORIZED = {"code": "1200", "message": "User not authorized!"}  # status code 401
    USER_ID_NOT_CORRECT = {"code": "1207", "message": "User Id not correct!"}
