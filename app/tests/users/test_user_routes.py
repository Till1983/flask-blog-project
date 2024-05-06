# Test login and register pages for correct display
# The code below has been adapted from https://codecookies.xyz/flask-tutorial/v1/unit-testing and modified.
from werkzeug.security import generate_password_hash

def test_show_registration_form(client):
    '''Test the registration page'''
    response = client.get('/register')
    assert response.status_code == 200, "Expected status code 200, but got {}".format(response.status_code)
    assert b'Create an account' in response.data, "Expected 'Create an account' in response data, but it was not found"

def test_show_login_form(client):
    '''Test the login page'''
    response = client.get('/login')
    assert response.status_code == 200, "Expected status code 200, but got {}".format(response.status_code)
    assert b'Log in' in response.data, "Expected 'Log in' in response data, but it was not found"

def test_create_account(client):
    '''Test user registration'''
    data = {
        'name': 'Test User',
        'email': 'test@example.com',
        'psw': 'password123',
        'rpsw': 'password123'
    }
    response = client.post('/register', data=data, follow_redirects=True)
    assert response.status_code == 200, "Expected status code 200, but got {}".format(response.status_code)
    assert b'You have successfully created your account!' in response.data, "Registration success message not found in response data"

def test_login(client):
    '''Test user login'''
    data = {
        'email': 'newie@email.com',
        'psw': 'password6'
    }
    response = client.post('/login', data=data, follow_redirects=True)
    assert response.status_code == 200, "Expected status code 200, but got {}".format(response.status_code)

def test_logout(client):
    '''Test user logout'''
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200, "Expected status code 200, but got {}".format(response.status_code)
    assert b'Until next time!' in response.data, "Logout success message not found in response data"
