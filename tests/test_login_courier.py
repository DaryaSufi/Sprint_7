import allure
from helpers import generate_courier_data
from helpers import courier_login
from helpers import register_new_courier_and_return_login_password

class TestLoginCourier:
    @allure.title("Проверка успешной авторизации курьера")
    def test_courier_login(self):
        courier_data = register_new_courier_and_return_login_password()
        courier = courier_login(courier_data[0], courier_data[1])
        assert courier.status_code == 200

    @allure.title("Проверка невозможности авторизации курьера без логина")
    def test_courier_login_without_login(self):
        courier_data = register_new_courier_and_return_login_password()
        courier = courier_login('', courier_data[1])
        assert courier.status_code == 400

    @allure.title("Проверка невозможности авторизации курьера без пароля")
    def test_courier_login_without_password(self):
        courier_data = register_new_courier_and_return_login_password()
        courier = courier_login(courier_data[0], '')
        assert courier.status_code == 400

    @allure.title("Проверка невозможности авторизации курьера с несуществующими данными")
    def test_courier_login_without_real_datas(self):
        courier_data=generate_courier_data()
        courier = courier_login(courier_data["login"], courier_data["password"])
        assert courier.status_code == 404

    @allure.title("Проверка возврата id при авторизации курьера")
    def test_courier_login_returns_id(self):
        courier_data = register_new_courier_and_return_login_password()
        courier = courier_login(courier_data[0], courier_data[1])
        assert "id" in courier.json()



