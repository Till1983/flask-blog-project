# Testing blogpost routes for correct display
# The code below has been adapted from examples at https://codecookies.xyz/flask-tutorial/v1/unit-testing

def test_post_display(client):
    """Test if the posts route displays correctly."""
    response = client.get('/posts')
    assert response.status_code == 200


def test_get_create_post(client):
    """Test the GET request to create a post route."""
    response = client.get('/create-post')
    assert response.status_code == 302
    assert 'Location' in response.headers

    with client:
        client.post('/login', data={'username': 'your_username', 'password': 'your_password'})
        response = client.get('/create-post')
        assert response.status_code == 302


def test_post_create_post(client):
    """Test the POST request to create a post route."""
    response = client.post('/create-post', data={'title': 'Test Post', 'blogpost': 'Test content'})
    assert response.status_code == 302


def test_check_login_status(client):
    """Test the login status for different routes."""
    # Simulate a request to an endpoint that doesn't require authentication
    response = client.get('/posts')
    assert response.status_code == 200

    # Simulate a request to an endpoint that requires authentication without logging in
    response = client.get('/create-post')
    assert response.status_code == 302
    assert response.headers['Location'] == '/login'

    # Simulate a request to an endpoint that requires authentication after logging in
    with client:
        client.post('/login', data={'username': 'your_username', 'password': 'your_password'})
        response = client.get('/create-post')
        assert response.status_code == 302


'''def test_view_post(client):
    """Test the POST request to view a post route"""
    existing_post_id = 1
    response = client.get(f'/post/{existing_post_id}')
    assert response.status_code == 200  # Expecting a successful response

    non_existing_post_id = 999
    response = client.get(f'/post/{non_existing_post_id}')
    assert response.status_code == 404'''


def test_edit_post_get(client):
    """Test the GET request to edit a post route"""
    existing_post_id = 1  
    response = client.get(f'/edit-post/{existing_post_id}')
    assert response.status_code == 302 


def test_edit_post_post(client):
    """Test the POST request to edit a post route"""
    existing_post_id = 1
    response = client.post(f'/edit-post/{existing_post_id}', data={'title': 'Updated Title', 'content': 'Updated Content'})
    assert response.status_code == 302


def test_delete_post(client):
    """Test the DELETE request to delete a post"""
    existing_post_id = 1
    response = client.get(f'/delete-post/{existing_post_id}')
    assert response.status_code == 302
