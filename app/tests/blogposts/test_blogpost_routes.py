# Testing blogpost routes for correct display
# The code below has been adapted from examples at https://codecookies.xyz/flask-tutorial/v1/unit-testing

def test_post_display(client):
    response = client.get('/posts')
    assert response.status_code == 200