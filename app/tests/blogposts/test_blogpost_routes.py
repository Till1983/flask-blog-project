from app.blogposts.models import Article
from app.extensions.database import db

def test_post_display(client):
    """Test if the posts route displays correctly."""
    response = client.get('/posts')
    assert response.status_code == 200
    assert b'Blog Posts' in response.data
    assert 'Content-Type' in response.headers
    assert 'text/html' in response.headers['Content-Type']


def test_get_create_post(client):
    """Test the GET request to create a post route."""
    response = client.get('/create-post')
    assert response.status_code == 302
    assert 'Location' in response.headers
    assert response.headers['Location'] == '/login'

    with client:
        client.post('/login', data={'username': 'your_username', 'password': 'your_password'})
        response = client.get('/create-post')
        assert response.status_code == 302
        assert 'Location' in response.headers


def test_post_create_post(client):
    """Test the POST request to create a post route."""
    response = client.post('/create-post', data={'title': 'Test Post', 'blogpost': 'Test content'})
    assert response.status_code == 302
    assert 'Location' in response.headers
    assert response.headers['Location'] == '/login'


def test_check_login_status(client):
    """Test the login status for different routes."""
    response = client.get('/posts')
    assert response.status_code == 200
    assert 'Content-Type' in response.headers

    response = client.get('/create-post')
    assert response.status_code == 302
    assert 'Location' in response.headers
    assert response.headers['Location'] == '/login'

    with client:
        client.post('/login', data={'username': 'your_username', 'password': 'your_password'})
        response = client.get('/create-post')
        assert response.status_code == 302
        assert 'Location' in response.headers


def test_view_post(client):
    """Test the GET request to view a post route"""
    # Create a test article first
    test_article = Article(
        title="Test Post",
        content="Test Content",
        author_id=1  # Make sure this user exists in your test database
    )
    db.session.add(test_article)
    db.session.commit()

    # Now test viewing the post
    response = client.get(f'/post/{test_article.id}')
    assert response.status_code == 200  # Expecting a successful response

    non_existing_post_id = 999
    response = client.get(f'/post/{non_existing_post_id}')
    assert response.status_code == 404
    assert 'Content-Type' in response.headers


def test_edit_post_get(client):
    """Test the GET request to edit a post route"""
    existing_post_id = 1  
    response = client.get(f'/edit-post/{existing_post_id}')
    assert response.status_code == 302
    assert 'Location' in response.headers
    assert response.headers['Location'] == '/login'


def test_edit_post_post(client):
    """Test the POST request to edit a post route"""
    existing_post_id = 1
    response = client.post(f'/edit-post/{existing_post_id}', 
                         data={'title': 'Updated Title', 'content': 'Updated Content'})
    assert response.status_code == 302
    assert 'Location' in response.headers
    assert response.headers['Location'] == '/login'


def test_delete_post(client):
    """Test the DELETE request to delete a post"""
    existing_post_id = 1
    response = client.get(f'/delete-post/{existing_post_id}')
    assert response.status_code == 302
    assert 'Location' in response.headers
    assert response.headers['Location'] == '/login'
