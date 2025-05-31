import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    # Check for form fields and text in the response HTMLs
    assert b"Enter Age and Experience" in response.data
    assert b"Age:" in response.data
    assert b"Experience:" in response.data

def test_predict(client):
    # Assuming your /predict expects form data POST, adjust if JSON
    data = {
        'age': '30',
        'experience': '5'
    }
    response = client.post('/predict', data=data)
    assert response.status_code == 200
    # The response should include "Predicted Salary:" text with a dollar amount
    assert b"Predicted Salary:" in response.data
    assert b"$" in response.data
