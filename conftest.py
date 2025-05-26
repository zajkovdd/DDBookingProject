import pytest

from faker import Faker
from core.clients.api_client import APIClient
from datetime import datetime, timedelta


@pytest.fixture(scope='session')
def api_client():
    client = APIClient()
    client.auth()
    return client

@pytest.fixture()
def booking_dates():
    today = datetime.today()
    checkin_date = today + timedelta(days = 10)
    checkout_date = checkin_date + timedelta(days = 5)
    return {
        'checkin': checkin_date.strftime('%Y-%m-%d'),
        'checkout': checkout_date.strftime('%Y-%m-%d')
    }

@pytest.fixture()
def generate_random_booking_data(booking_dates):
    faker = Faker()
    firstname = faker.first_name()
    lastname = faker.last_name()
    totalprice = faker.random_number(digits=3)
    depositpaid = faker.boolean()
    additionalneeds = faker.sentence()

    data = {
        'firstname': firstname,
        'lastname': lastname,
        'totalprice': totalprice,
        'depositpaid': depositpaid,
        'booking_date': booking_dates,
        'additionalneeds': additionalneeds
    }

    return data
