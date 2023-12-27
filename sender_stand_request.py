import configuration
import requests
import data

def post_new_order():
    response = requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER_PATH,
                         json=data.order_body.copy(),
                         headers=data.headers.copy())

    assert response.status_code == 201
    assert response.json()["track"] != ""

    return response.json()["track"]

def get_order(orderId):
    response = requests.get(configuration.URL_SERVICE + configuration.NEW_ORDER_PATH + "?t=" + str(orderId))

    assert response.status_code == 200

    return response.json()
