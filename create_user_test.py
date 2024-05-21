import sender_stand_request
import test_functions
import data


# Prueba negative 1
def test_create_user_2_letter_in_first_name_get_success_response():
    test_functions.positive_assert('Aa')


def test_create_user_15_letter_in_first_name_get_success_response():
    test_functions.positive_assert('Aaaaaaa aaaaaaaa')


# Prueba negative 3
def test_create_user_1_letter_in_first_name_get_error_response():
    test_functions.negative_assert_symbol('A')


# Prueba negative 4
def test_create_user_16_letter_in_first_name_get_error_response():
    test_functions.negative_assert_symbol('Аааааааааааааааа')


# Prueba negative 5
def test_create_user_has_space_in_first_name_get_error_response():
    test_functions.negative_assert_symbol('А Aаа')


# Prueba negative 6
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    test_functions.negative_assert_symbol("\№%@\,")


# Prueba negative 7
def test_create_user_has_number_in_first_name_get_error_response():
    test_functions.negative_assert_symbol("123")


# Prueba negative 8
def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    test_functions.negative_assert_no_firstname(user_body)


# Prueba negative 9
def test_create_user_empty_first_name_get_error_response():
    user_body = test_functions.get_user_body("")
    test_functions.negative_assert_no_firstname(user_body)

# Prueba negative 10
def test_create_user_number_type_first_name_get_error_response():
    user_body = test_functions.get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    print(response.status_code)
