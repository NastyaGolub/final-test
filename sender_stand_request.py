import configuration
import requests
import data

def post_new_order():
    response = requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER_PATH,
                         json=data.order_body.copy(),
                         headers=data.headers.copy())
    return response

def get_order(track):
    response = requests.get(configuration.URL_SERVICE + configuration.NEW_ORDER_PATH + "?t=" + str(track))

    return response
