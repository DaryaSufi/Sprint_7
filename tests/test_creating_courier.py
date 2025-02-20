import requests
import allure
from helpers import register_new_courier_and_return_login_password
from constants import URL
from helpers import generate_courier_data

class TestCreateCourier:
    @allure.title("Проверка успешного создания курьера")
    def test_create_courier(self):
        courier=register_new_courier_and_return_login_password()
        assert courier.status_code == 201
        assert courier.json().get("ok") is True

    @allure.title("Проверка невозможности создания двух одинаковых курьеров")
    def test_create_two_identical_couriers(self):
        test_data = register_new_courier_and_return_login_password()
        response = requests.post(f"{URL.scooter_url}{URL.courier_url}",
                                 data={"login": test_data[0], "password": test_data[1], "firstName": test_data[2]})
        response_json = response.json()
        assert response.status_code == 409

    @allure.title("Проверка невозможности создания курьера без логина")
    def test_create_courier_without_login(self):
        test_data=generate_courier_data()
        payload = {
            "login": "",
            "password": test_data["password"],
            "first_name": test_data["first_name"],
        }
        response=requests.post(f"{URL.scooter_url}{URL.courier_url}", data=payload)
        assert response.status_code == 400

    @allure.title("Проверка невозможности создания курьера без пароля")
    def test_test_create_courier_without_password(self):
        test_data = generate_courier_data()
        payload = {
            "login": test_data["login"],
            "password": "",
            "first_name": test_data["first_name"],
        }
        response = requests.post(f"{URL.scooter_url}{URL.courier_url}", data=payload)
        assert response.status_code == 400

    @allure.title("Проверка невозможности создания курьера без имени")
    def test_test_create_courier_without_password(self):
        test_data = generate_courier_data()
        payload = {
            "login": test_data["login"],
            "password": test_data["password"],
            "first_name": "",
        }
        response = requests.post(f"{URL.scooter_url}{URL.courier_url}", data=payload)
        assert response.status_code == 400








