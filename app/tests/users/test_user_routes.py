# Test login and register pages for correct display

def test_register_display(client):
    response = client.get('/register')
    assert response.status_code == 200

def test_register_display(client):
    response = client.get('/login')
    assert response.status_code == 200