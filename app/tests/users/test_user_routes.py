# Test login and register pages for correct display
# The code below has been adapted from https://codecookies.xyz/flask-tutorial/v1/unit-testing and modified.

def test_show_registration_form(client):
    '''tests the register page'''
    response = client.get('/register')
    assert response.status_code == 200

def test_show_login_form(client):
    '''tests the login page'''
    response = client.get('/login')
    assert response.status_code == 200