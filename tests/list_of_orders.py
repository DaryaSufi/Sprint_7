import allure
import pytest
from constants import OrdeData
from helpers import place_an_order
from helpers import get_order

class TestListOfOrder:
    @allure.title("Проверка создания заказа с1 цветом, с 2-мя цветами, без цвета")
    @pytest.mark.parametrize(
        'body', [
            OrdeData.GREY,
            OrdeData.BLACK,
            OrdeData.BLACKGREY,
            OrdeData.NOCOLOR
        ])
    def test_place_an_order(self, body):
        response=place_an_order()
        assert response.status_code==201

    @allure.title("Проверка что при оформлении заказа тело ответа возвращает список заказов")
    def test_list_of_orders(self):
        list_of_orders = get_order()
        assert "orders" in list_of_orders.json()
        assert list_of_orders.status_code==200








