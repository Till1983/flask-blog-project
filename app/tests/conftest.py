import pytest
from app.app import create_app
from os import environ

@pytest.fixture
def client():
    environ['DATABASE_URL'] = 'sqlite://'
    app = create_app()

    with app.app_context():
        yield app.test_client()