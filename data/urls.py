class Urls:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

    CREATE_USER = f"{BASE_URL}/api/auth/register"
    LOGIN = f"{BASE_URL}/api/auth/login"
    DELETE_USER = f"{BASE_URL}/api/auth/user"
    CREATE_ORDER = f"{BASE_URL}/api/orders"
    GET_ORDERS = f"{BASE_URL}/api/orders"