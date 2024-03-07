" importamos lo necesario "
# import pytest

from app import app  # Flask instance of the API


def test_index_route():
    " testeamos la respuesta del cliente "
    response = app.test_client().get('/status')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'OK'


def test_landing():
    " Nos aseguramos de que llegue "
    landing = app.test_client().get('/')
    html = landing.data.decode()

    assert landing.status_code == 200

    # Check text
    assert "Hello Docker" in html
    assert "It is currently " in html
