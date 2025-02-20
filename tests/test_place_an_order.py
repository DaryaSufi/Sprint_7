import allure
import pytest
from constants import OrdeData
from helpers import place_an_order

class TestPlaceAnOrder:
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
        assert "track" in response.json()