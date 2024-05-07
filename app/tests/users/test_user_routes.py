# Test login and register pages for correct display
# The code below has been adapted from https://codecookies.xyz/flask-tutorial/v1/unit-testing and modified.
from werkzeug.security import generate_password_hash
from app.users.models import Author
from app.extensions.database import db

def test_show_registration_form(client):
    '''Test the registration page'''
    response = client.get('/register')
    assert response.status_code == 200
    assert b'Create Your Account Here' in response.data

def test_create_account(client):
    response = client.post('/register', data=dict(
        name='Test User',
        email='test@example.com',
        psw='password123',
        rpsw='password123'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'You have successfully created your account!' in response.data

def test_show_login_form(client):
    '''Test the login page'''
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_login(client):
    '''Test user login'''
    # Create a test user
    hashed_password = generate_password_hash('password123')
    new_user = Author(name='Test User', email='test@example.com', password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    # Test login with correct credentials
    response = client.post('/login', data=dict(
        email='test@example.com',
        psw='password123'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome!' in response.data

    # Test login with incorrect password
    response = client.post('/login', data=dict(
        email='test@example.com',
        psw='wrongpassword'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Incorrect email or password' in response.data

    # Test login with non-existing user
    response = client.post('/login', data=dict(
        email='nonexistent@example.com',
        psw='password123'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'User not found' in response.data

def test_login_success(client):
    '''Test success of login'''
    response = client.get('/welcome')
    assert response.status_code == 200
    assert b'Welcome!' in response.data

def test_logout(client):
    '''Test user logout'''
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Until next time!' in response.data