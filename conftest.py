import pytest
from helpers import register_new_courier_and_return_login_password
import allure
from helpers import courier_login
from helpers import delete_courier

@allure.step("Создаём курьера")
@pytest.fixture()
def create_and_delete_courier():
    courier = register_new_courier_and_return_login_password()
    with allure.step("Получаем id для последующего удаления"):
        courier_id = courier_login(courier["login"], courier["password"]).json()["id"]
    yield courier
    delete_courier(courier_id)

