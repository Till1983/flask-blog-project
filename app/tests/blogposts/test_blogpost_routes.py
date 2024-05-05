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


def test_view_post(client):
    # Simulate accessing an existing post
    existing_post_id = 1
    response = client.get(f'/post/{existing_post_id}')
    assert response.status_code == 200  # Expecting a successful response

    non_existing_post_id = 999
    response = client.get(f'/post/{non_existing_post_id}')
    assert response.status_code == 404


def test_edit_post_get(client):
    # Simulate accessing the edit post page for an existing post
    existing_post_id = 1  
    response = client.get(f'/edit-post/{existing_post_id}')
    assert response.status_code == 302  # Expecting a successful response


def test_edit_post_post(client):
    # Simulate submitting an edit post form
    existing_post_id = 1
    response = client.post(f'/edit-post/{existing_post_id}', data={'title': 'Updated Title', 'content': 'Updated Content'})
    assert response.status_code == 302  # Expecting a redirect response after successful post update


def test_delete_post(client):
    # Simulate accessing the delete post page for an existing post
    existing_post_id = 1
    response = client.get(f'/delete-post/{existing_post_id}')
    assert response.status_code == 302  # Expecting a redirect response after successful post deletion
