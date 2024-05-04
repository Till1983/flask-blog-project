# Testing blogpost routes for correct display
# The code below has been adapted from examples at https://codecookies.xyz/flask-tutorial/v1/unit-testing

def test_post_display(client):
    response = client.get('/posts')
    assert response.status_code == 200

def test_get_create_post(client):
    response = client.get('/create-post')
    assert response.status_code == 302
    assert 'Location' in response.headers

    with client:
        client.post('/login', data={'username': 'your_username', 'password': 'your_password'})
        response = client.get('/create-post')
        assert response.status_code == 302


def test_post_create_post(client):
    # Simulate a POST request to create a post
    response = client.post('/create-post', data={'title': 'Test Post', 'blogpost': 'Test content'})
    assert response.status_code == 302

def test_check_login_status(client):
    # Simulate a request to an endpoint that doesn't require authentication
    response = client.get('/posts')
    assert response.status_code == 200  # Assuming posts endpoint doesn't require authentication

    # Simulate a request to an endpoint that requires authentication without logging in
    response = client.get('/create-post')
    assert response.status_code == 302
    assert response.headers['Location'] == '/login'  # Assuming it redirects to the login form

    # Simulate a request to an endpoint that requires authentication after logging in
    with client:
        client.post('/login', data={'username': 'your_username', 'password': 'your_password'})
        response = client.get('/create-post')
        assert response.status_code == 302  # Assuming it allows access after logging in
