import allure
from client.orders import OrderClient
from data.ingredients import Ingredients
from data.messages import MessageError

@allure.suite("Создание заказов")
class TestCreateOrder:

    @allure.title("Создание заказа с ингредиентами и авторизацией")
    def test_create_order_with_ingredients(self, create_and_delete_user):
        email, password, token = create_and_delete_user

        response = OrderClient.create_order(Ingredients.VALID, token)
        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self):
        response = OrderClient.create_order(Ingredients.VALID)
        assert response.status_code == 401
        assert response.json().get("success") is False

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, create_and_delete_user):
        email, password, token = create_and_delete_user
        response = OrderClient.create_order({"ingredients": []}, token)
        assert response.status_code == 400
        assert response.json().get("success") is False
        assert response.json().get("message") == MessageError.EMPTY_INGREDIENTS

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredients(self, create_and_delete_user):
        email, password, token = create_and_delete_user
        response = OrderClient.create_order(Ingredients.INVALID, token)
        assert response.status_code == 500
