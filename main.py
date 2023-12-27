# Голуб Анастасия, 12-я когорта Финальный проект. Инеженер по тестированию плюс

import sender_stand_request

orderId = sender_stand_request.post_new_order()
order = sender_stand_request.get_order(orderId)

print(order)
