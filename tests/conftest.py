import pytest
from helpers import register_new_courier_and_return_login_password
import allure
from helpers import courier_login
from helpers import delete_courier

@allure.step("Создаём курьера")
@pytest.fixture()
def create_and_delete_courier():
    courier = register_new_courier_and_return_login_password()
    courier_id = courier_login(courier[0], courier[1])
    yield courier
    delete_courier(courier_id)

@allure.step("Создаём курьера без логина")
@pytest.fixture()
def create_and_deleete_courier_without_login():
    response, login_pass = register_new_courier_and_return_login_password()
    login_pass[0] = ""
    yield response, login_pass
    courier_id = courier_login(login_pass[0], login_pass[1])
    delete_courier(courier_id)

@allure.step("Создаём курьера без пароля")
@pytest.fixture()
def create_and_deleete_courier_without_password():
    response, login_pass = register_new_courier_and_return_login_password()
    login_pass[1] = ""
    yield response, login_pass
    courier_id = courier_login(login_pass[0], login_pass[1])
    delete_courier(courier_id)

@allure.step("Создаём курьера без имени")
@pytest.fixture()
def create_courier_without_first_name():
    response, login_pass = register_new_courier_and_return_login_password()
    login_pass[2] = ""
    yield response, login_pass
    courier_id = courier_login(login_pass[0], login_pass[1])
    delete_courier(courier_id)

