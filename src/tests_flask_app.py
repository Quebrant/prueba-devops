# import pytest

from app import app  # Flask instance of the API

"""Module providing a function for routing."""
def test_index_route():
    response = app.test_client().get('/status')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'OK'

"""Module providing a function testing landing."""
def test_landing():
    landing = app.test_client().get('/')
    html = landing.data.decode()

    assert landing.status_code == 200

    # Check text
    assert "Hello Docker" in html
    assert "It is currently " in html
