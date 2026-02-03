import pytest
from helpers.helpers import UserDataGenerator
from client.user import UserClient

@pytest.fixture(scope="function")
def create_and_delete_user():
    user_data = UserDataGenerator.generate_user_data()
    response = UserClient.create_user(user_data)
    response.raise_for_status()
    token = response.json().get("accessToken")
    yield user_data["email"], user_data["password"], token
    if token:
        UserClient.delete_user(token)

@pytest.fixture(scope="function")
def delete_user():
    tokens = []
    yield tokens
    for token in tokens:
        UserClient.delete_user(token)
