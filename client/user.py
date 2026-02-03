import requests
import allure
from helpers.helpers import UserDataGenerator
from data.urls import Urls

class UserClient:

    @staticmethod
    @allure.step("Создание нового пользователя")
    def create_user(user_data=None):
        if user_data is None:
            user_data = UserDataGenerator.generate_user_data()
        return requests.post(Urls.CREATE_USER, json=user_data)

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(email, password):
        return requests.post(Urls.LOGIN, json={"email": email, "password": password})

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(token):
        return requests.delete(Urls.DELETE_USER, headers={"Authorization": token})
