# Testing blogpost routes for correct display

def test_post_display(client):
    response = client.get('/posts')
    assert response.status_code == 200