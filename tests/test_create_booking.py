import allure


@allure.feature('Test Create Booking')
@allure.story('Test data after create booking')
def test_data_after_create_booking(api_client, generate_random_booking_data):
    booking_data = generate_random_booking_data
    response = api_client.create_booking(booking_data=booking_data)
    assert response == booking_data, f'Expected similar response but got {response}'