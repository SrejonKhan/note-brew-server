import pytest
from app.models import User
from app import create_app 
from app.configs.config import TestingConfig

@pytest.fixture(scope="module")
def new_user():
    user = User("TestName", "test@example.com", "strongpassword")
    return user

@pytest.fixture(scope="module")
def test_client():
    app = create_app(TestingConfig)
    
    with app.test_client() as testing_client:
        yield testing_client