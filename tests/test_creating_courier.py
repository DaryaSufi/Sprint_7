import requests
import allure
from constants import URL

class TestCreateCourier:
    @allure.title("Проверка успешного создания курьера")
    def test_create_courier(self, create_and_delete_courier):
        response,_= create_and_delete_courier
        response_json = response.json()
        assert response.status_code == 201
        assert response_json.get("ok") is True

    @allure.title("Проверка невозможности создания двух одинаковых курьеров")
    def test_create_two_identical_couriers(self, create_and_delete_courier):
        _,login_pass = create_and_delete_courier
        response = requests.post(f"{URL.scooter_url}{URL.courier_url}",
                                 data={"login": login_pass[0], "password": login_pass[1], "firstName": login_pass[2]})
        response_json = response.json()
        assert response.status_code == 409
        assert response_json.get("message") == "Этот логин уже используется"

    @allure.title("Проверка невозможности создания курьера без логина")
    def test_create_courier_without_login(self, create_and_deleete_courier_without_login):
        response,login_pass = create_and_deleete_courier_without_login
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка невозможности создания курьера без пароля")
    def test_test_create_courier_without_password(self, create_and_deleete_courier_without_password):
        response,login_pass = create_and_deleete_courier_without_password
        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка возможности создания курьера без имени")
    def test_test_create_courier_without_password(self, create_courier_without_first_name):
        response, login_pass = create_courier_without_first_name
        assert response.status_code == 201
        assert response.json().get("ok") is True








