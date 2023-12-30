# Голуб Анастасия, 12-я когорта Финальный проект. Инеженер по тестированию плюс

import sender_stand_request

def test_get_order_by_track():
    # Cоздается новый заказ
    response = sender_stand_request.post_new_order()

    assert response.status_code == 201
    assert response.json()["track"] != ""

    track = response.json()["track"]
    # Получается заказ по трекеру
    response_order_by_track = sender_stand_request.get_order(track)
    assert response_order_by_track.status_code == 200
