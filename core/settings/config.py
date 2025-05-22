from enum import Enum


class Users(Enum):
    USERNAME = 'admin'
    PASSWORD = 'password123'

class Timeouts(Enum):
    TIMEOUT = 5

class ID(Enum):
    TESTID = 1