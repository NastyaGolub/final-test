# Голуб Анастасия, 12-я когорта Финальный проект. Инеженер по тестированию плюс

import sender_stand_request

sendOrder = sender_stand_request.post_new_order()

assert sendOrder.status_code == 201
assert sendOrder.json()["track"] != ""

track = sendOrder.json()["track"]

getOrder = sender_stand_request.get_order(track)

assert getOrder.status_code == 200

print("passed")