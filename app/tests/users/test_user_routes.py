# Test login and register pages for correct display

def test_register_display(client):
    '''tests the register page'''
    response = client.get('/register')
    assert response.status_code == 200

def test_register_display(client):
    '''tests the login page'''
    response = client.get('/login')
    assert response.status_code == 200