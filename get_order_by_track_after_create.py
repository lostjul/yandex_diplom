import sender_stand_request


# Пахомова Юлия Петровна, 20 когорта. Финальный проект. Инженер по тестированию плюс
def test_assert_status_success():
    order_track = sender_stand_request.post_order_create().json()["track"]
    request = sender_stand_request.get_order_by_track(order_track)
    assert request.status_code == 200
