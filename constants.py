class URL:
    scooter_url = "https://qa-scooter.praktikum-services.ru"
    login_url = "/api/v1/courier/login"
    courier_url = "/api/v1/courier"
    courier_delete_url = "/api/v1/courier/"
    create_order_url  = "/api/v1/orders"
    orders_list_url = "/api/v1/orders"
    get_order_url = "/api/v1/orders"

class OrdeData:
    BLACK =  {
        "firstName": "Goku",
        "lastName": "Son",
        "address": "West City, 42 Capsule Corp",
        "metroStation": 12,
        "phone": "+7 977 777 77 77",
        "rentTime": 24,
        "deliveryDate": "2023-12-31",
        "comment": "Senzu beans delivery",
        "color": ["BLACK"]
    }

    GREY = {
    "firstName": "Ivan",
    "lastName": "Petrov",
    "address": "Moscow, Lenina str. 15-25",
    "metroStation": 5,
    "phone": "+7 495 222 33 44",
    "rentTime": 1,
    "deliveryDate": "2023-08-01",
    "comment": "Please call before delivery",
    "color": ["GREY"]
}

    BLACKGREY = {
    "firstName": "Homer",
    "lastName": "Simpson",
    "address": "Springfield, Evergreen Terrace 742",
    "metroStation": 7,
    "phone": "+7 800 DONUTS",
    "rentTime": 99,
    "deliveryDate": "2023-07-12",
    "comment": "D'oh! Need more donuts!",
    "color": ["BLACK", "GREY"]
}

    NOCOLOR =  {
     "firstName":"Aio",
     "lastName":"Yashiro",
     "address":"Higashi Ward, Tsukuba, Ibaraki Prefecture, Japan",
     "metroStation":"8",
     "phone" :" +81 80-4772-3327",
     "rentTime" : 3,
     "deliverydate":"2023-11-28",
     "comment":"Благодарю за заказ!",
     "color": [""]
}