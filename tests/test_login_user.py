import pytest
import allure
from client.user import UserClient
from helpers.helpers import UserDataGenerator
from data.messages import MessageError


@allure.feature("API: Пользователь")
class TestUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        user_body = UserDataGenerator.generate_user_data()

        with allure.step("Отправляем запрос на регистрацию уникального пользователя"):
            response = UserClient.create_user(user_body)

        assert response.status_code == 200
        assert response.json().get("success") is True
        assert response.json().get("user").get("email") == user_body["email"]
        assert response.json().get("user").get("name") == user_body["name"]
        assert "accessToken" in response.json()

    @allure.title("Нельзя создать пользователя с уже существующим email")
    def test_create_duplicate_user(self):
        user_body = UserDataGenerator.generate_user_data()
        UserClient.create_user(user_body)  # первый раз

        with allure.step("Пробуем создать того же пользователя ещё раз"):
            response = UserClient.create_user(user_body)

        assert response.status_code == 403
        assert response.json().get("success") is False
        assert response.json().get("message") == MessageError.USER_ALREADY_EXISTS

    @allure.title("Нельзя создать пользователя без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field(self, missing_field):
        user_body = UserDataGenerator.generate_user_data()
        user_body.pop(missing_field)

        with allure.step(f"Создание пользователя без поля {missing_field}"):
            response = UserClient.create_user(user_body)

        assert response.status_code == 403
        assert response.json().get("success") is False
        assert response.json().get("message") == MessageError.EMPTY_FIELDS
