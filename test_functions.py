import sender_stand_request
import data


def get_user_body(first_name): # solo cambia el nombre(Katharina) con el nombre de prueba(123)
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body


# Prueba negative 1 a 2
def positive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    print(user_response.status_code)
    assert user_response.json()["authToken"] != ""
    print(user_response.json())
    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1


# Prueba negative 3 a 7
def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    print(response.status_code)
    assert response.json()["code"] == 400
    print(response.status_code)


# Prueba negative 8 y 9
def negative_assert_no_firstname(user_body):
    # user_body = get_user_body(user_body)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    print(response.status_code)
    assert response.json()["code"] == 400



