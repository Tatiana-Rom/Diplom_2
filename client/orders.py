import requests
import allure
from data.urls import Urls

class OrderClient:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(order_data, token=None):
        headers = {"Authorization": token} if token else {}
        return requests.post(Urls.CREATE_ORDER, json=order_data, headers=headers)

    @staticmethod
    @allure.step("Получение заказов пользователя")
    def get_orders(token):
        return requests.get(Urls.GET_ORDERS, headers={"Authorization": token})
