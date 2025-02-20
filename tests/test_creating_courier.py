import requests
import allure
from helpers import register_new_courier_and_return_login_password
from constants import URL
from helpers import generate_courier_data
from helpers import courier_login
from helpers import delete_courier

class TestCreateCourier:
    @allure.title("Проверка успешного создания курьера")
    def test_create_courier(self):
        test_data = generate_courier_data()
        payload = {
            "login": test_data["login"],
            "password": test_data["password"],
            "first_name": test_data["first_name"],
        }
        response = requests.post(f"{URL.scooter_url}{URL.courier_url}", data=payload)
        response_json = response.json()
        courier_id = courier_login(test_data["login"], test_data["password"])
        delete_courier(courier_id)
        assert response.status_code == 201
        assert response_json.get("ok") is True

    @allure.title("Проверка невозможности создания двух одинаковых курьеров")
    def test_create_two_identical_couriers(self):
        test_data = register_new_courier_and_return_login_password()
        response = requests.post(f"{URL.scooter_url}{URL.courier_url}",
                                 data={"login": test_data[0], "password": test_data[1], "firstName": test_data[2]})
        response_json = response.json()
        if response.status_code == 201:
            courier_id = courier_login(test_data[0],test_data[1])
            delete_courier(courier_id)
        assert response.status_code == 409
        assert response_json.get("message") == "Этот логин уже используется"

    @allure.title("Проверка невозможности создания курьера без логина")
    def test_create_courier_without_login(self):
        test_data=generate_courier_data()
        payload = {
            "login": "",
            "password": test_data["password"],
            "first_name": test_data["first_name"],
        }
        response=requests.post(f"{URL.scooter_url}{URL.courier_url}", data=payload)
        response_json = response.json()
        if response.status_code == 201:
            courier_id = courier_login(test_data["login"],test_data["password"])
            delete_courier(courier_id)
        assert response.status_code == 400
        assert response_json.get("message") == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка невозможности создания курьера без пароля")
    def test_test_create_courier_without_password(self):
        test_data = generate_courier_data()
        payload = {
            "login": test_data["login"],
            "password": "",
            "first_name": test_data["first_name"],
        }
        response = requests.post(f"{URL.scooter_url}{URL.courier_url}", data=payload)
        response_json = response.json()
        if response.status_code == 201:
            courier_id = courier_login(test_data["login"],test_data["password"])
            delete_courier(courier_id)
        assert response.status_code == 400
        assert response_json.get("message") == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка невозможности создания курьера без имени")
    def test_test_create_courier_without_password(self):
        test_data = generate_courier_data()
        payload = {
            "login": test_data["login"],
            "password": test_data["password"],
            "first_name": "",
        }
        response = requests.post(f"{URL.scooter_url}{URL.courier_url}", data=payload)
        response_json = response.json()
        if response.status_code == 201:
            courier_id = courier_login(test_data["login"],test_data["password"])
            delete_courier(courier_id)
        assert response.status_code == 400
        assert response_json.get("message") == "Недостаточно данных для создания учетной записи"








