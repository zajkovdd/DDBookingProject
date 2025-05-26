import allure
import pytest
import requests


@allure.feature('Test ping')
@allure.story('Test connection')
def test_ping(api_client):
    status_code = api_client.ping()
    assert status_code == 201, f'Expected status code 201 but got {status_code}'

@allure.feature('Test ping')
@allure.story('Test server unavailability')
def test_ping_server_unavailable(api_client, mocker):
    mocker.patch.object(api_client.session,'get', side_effect=Exception('Server unavailable'))
    with pytest.raises(Exception, match='Server unavailable'):
        api_client.ping()

@allure.feature('Test ping')
@allure.story('Test wrong HTTP method')
def test_ping_wrong_method(api_client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 405
    mocker.patch.object(api_client.session,'get', return_value=mock_response)
    with pytest.raises(AssertionError, match='Expected status code 201 but got 405'):
        api_client.ping()

@allure.feature('Test ping')
@allure.story('Test server error')
def test_ping_internal_server_error(api_client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 500
    mocker.patch.object(api_client.session,'get', return_value=mock_response)
    with pytest.raises(AssertionError, match='Expected status code 201 but got 500'):
        api_client.ping()

@allure.feature('Test ping')
@allure.story('Test wrong URL')
def test_ping_not_found(api_client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 404
    mocker.patch.object(api_client.session,'get', return_value=mock_response)
    with pytest.raises(AssertionError, match='Expected status code 201 but got 404'):
        api_client.ping()

@allure.feature('Test ping')
@allure.story('Test connection with different success code')
def test_ping_success_different_code(api_client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mocker.patch.object(api_client.session,'get', return_value=mock_response)
    with pytest.raises(AssertionError, match='Expected status code 201 but got 200'):
        api_client.ping()

@allure.feature('Test ping')
@allure.story('Test timeout')
def test_ping_timeout(api_client, mocker):
    mocker.patch.object(api_client.session,'get', side_effect=requests.Timeout)
    with pytest.raises(requests.Timeout):
        api_client.ping()

@allure.feature('Test Create Booking')
@allure.story('Test status code')
def test_status_code_create_booking(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    status_code = api_client.create_booking(booking_data=booking_data).status_code
    assert status_code == 200, f'Expected status code 200 but got {status_code}'

@allure.feature('Test Create Booking')
@allure.story('Test data after create booking')
def test_data_after_create_booking(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    response = api_client.create_booking(booking_data=booking_data)
    assert response.json == booking_data, f'Expected similar response but got {response.json}'
