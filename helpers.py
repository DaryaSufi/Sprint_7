import requests
import random
import string
from constants import URL

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f"{URL.scooter_url}{URL.courier_url}", data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass

def courier_login(login, password):
    payload = {"login": login, "password": password}
    response = requests.post(f"{URL.scooter_url}{URL.login_url}", data=payload)
    return response
def delete_courier(id):
    requests.delete(f"{URL.scooter_url}{URL.courier_delete_url}{id}")

def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
def generate_courier_data():

    # создаём словарь, чтобы метод мог его вернуть
    courier_data = {}
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    courier_data["login"] = login
    courier_data["password"] = password
    courier_data["first_name"] = first_name

    return courier_data

def regisster_new_courier():
    courier_data=generate_courier_data()
    response = requests.post(f"{URL.scooter_url}{URL.courier_url}", data=courier_data)
    return response
def place_an_order():
    body={}
    response = requests.post(f"{URL.scooter_url}{URL.create_order_url}", data=body)
    return response
def get_order():
    response=requests.get(f"{URL.scooter_url}{URL.get_order_url}")
    return response
