import string

import allure

from pydantic import ValidationError
from core.models.booking import BookingResponse


@allure.feature('Test creating booking')
@allure.story('Positive: creating booking with custom data')
def test_create_booking_with_custom_data(api_client):
    booking_data = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2025-02-01",
            "checkout" : "2025-02-10"
        },
        "additionalneeds" : "Breakfast"
    }
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature('Test creating booking')
@allure.story('Positive: creating booking with random data')
def test_create_booking_with_random_data(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature('Test creating booking')
@allure.story('Positive: creating booking without optional data')
def test_create_booking_without_optional_data(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    booking_data['additionalneeds'] = None
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']

@allure.feature('Test creating booking')
@allure.story('Positive: creating booking with zero total price')
def test_create_booking_with_zero_total_price(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    booking_data['totalprice'] = 0
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature('Test creating booking')
@allure.story('Positive: creating booking with very big total price')
def test_create_booking_with_very_big_total_price(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    booking_data['totalprice'] = 10**10
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature('Test creating booking')
@allure.story('Positive: creating booking with same date in checkin and checkout')
def test_create_booking_with_same_date_in_checkin_and_checkout(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    booking_data['bookingdates']['checkin'] = booking_data['bookingdates']['checkout']
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature('Test creating booking')
@allure.story('Positive: creating booking with special characters')
def test_create_booking_with_special_characters(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    booking_data['firstname'] = '=!@#$%^&*()_+'
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature('Test creating booking')
@allure.story('Negative: creating booking with huge total price')
def test_create_booking_with_huge_total_price(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    booking_data['totalprice'] = 10**100
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature('Test creating booking')
@allure.story('Negative: creating booking without required field')
def test_create_booking_without_required_field(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    booking_data['firstname'] = None
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

@allure.feature('Test creating booking')
@allure.story('Negative: creating booking without required field checkin')
def test_create_booking_without_required_field_checkin(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    booking_data['bookingdates']['checkin'] = None
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

@allure.feature('Test creating booking')
@allure.story('Negative: creating booking with wrong date format in checkin') # TODO API его само переделывает в нужный формат
def test_create_booking_with_wrong_date_format_in_checkin(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    booking_data['bookingdates']['checkin'] = '12.12.1999'
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature('Test creating booking')
@allure.story('Negative: creating booking with checkout before checkin') # TODO Должна быть ошибка, но ее нет :)))
def test_create_booking_with_checkout_before_checkin(api_client, generate_random_booking_data):

    def swap_values(dictionary, key1, key2): # TODO Куда-то нужно вынести это?
        if key1 in dictionary and key2 in dictionary:
            dictionary[key1], dictionary[key2] = dictionary[key2], dictionary[key1]

    booking_data = generate_random_booking_data
    swap_values(booking_data['bookingdates'], 'checkin', 'checkout')
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

@allure.feature('Test creating booking')
@allure.story('Negative: creating booking with negative total price') # TODO Должна быть ошибка, но ее нет :)))
def test_create_booking_with_negative_total_price(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    booking_data['totalprice'] = -100
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

@allure.feature('Test creating booking')
@allure.story('Negative: creating booking with total price as string(number)') # TODO API его само переделывает в нужный формат, но отправляли мы строку
def test_create_booking_with_total_price_as_string_num(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    booking_data['totalprice'] = '100'
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature('Test creating booking')
@allure.story('Negative: creating booking with total price as string(not number)')
def test_create_booking_with_total_price_as_string_not_num(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    booking_data['totalprice'] = 'hundred'
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature('Test creating booking')
@allure.story('Negative: creating booking with not valid depositpaid') # TODO API его само переделывает в нужный формат, но отправляли мы строку
def test_create_booking_with_not_valid_deposidpaid(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    booking_data['depositpaid'] = 'yes'
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']

@allure.feature('Test creating booking')
@allure.story('Negative: creating booking with empty booking_data')
def test_create_booking_with_empty_booking_data(api_client):
    booking_data = {}
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

@allure.feature('Test creating booking')
@allure.story('Negative: creating booking with extra field') # TODO API его просто не добавило
def test_create_booking_with_extra_field(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    booking_data['extrafield'] = 'smth'
    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f'Response validation failed: {e}')

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']
    assert response['booking']['extrafield'] == booking_data['extrafield']
