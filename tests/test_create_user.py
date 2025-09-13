import allure
import pytest
from client.user import UserClient
from helpers.helpers import UserDataGenerator
from data.messages import MessageError


class TestUser:

    @allure.title("Создание уникального пользователя")
    @allure.description("Создаём нового пользователя через API и проверяем ответ")
    def test_create_unique_user(self, delete_user):
        user_data = UserDataGenerator.generate_user_data()

        with allure.step("Создаём пользователя"):
            response = UserClient.create_user(user_data)

        assert response.status_code == 200, f"Неверный код: {response.text}"
        assert response.json().get("success") is True
        assert response.json()["user"]["email"] == user_data["email"]
        token = response.json()['accessToken']
        delete_user.append(token)

    @allure.title("Ошибка при создании пользователя с уже существующим email")
    @allure.description("Нельзя создать двух одинаковых пользователей — ответ 403 и сообщение об ошибке")
    def test_create_duplicate_user(self, delete_user):
        user_data = UserDataGenerator.generate_user_data()
        UserClient.create_user(user_data)

        with allure.step("Пробуем создать того же пользователя ещё раз"):
            response = UserClient.create_user(user_data)

        assert response.status_code == 403
        assert response.json().get("success") is False
        assert response.json().get("message") == MessageError.USER_ALREADY_EXISTS

    @allure.title("Ошибка при создании пользователя без обязательного поля")
    @allure.description("Если убрать email, password или name — ответ 403 и сообщение об ошибке")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_required_field(self, missing_field):
        user_data = UserDataGenerator.generate_user_data()
        data = user_data.copy()
        data.pop(missing_field)

        with allure.step(f"Создание пользователя без поля {missing_field}"):
            response = UserClient.create_user(data)

        assert response.status_code == 403
        assert response.json().get("success") is False
        assert response.json().get("message") == MessageError.EMPTY_FIELDS
