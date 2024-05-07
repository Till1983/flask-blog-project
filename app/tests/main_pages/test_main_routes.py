# Testing the routes of "main_pages" for correct display
# The code below has been adapted from examples at https://codecookies.xyz/flask-tutorial/v1/unit-testing

def test_index_display(client):
    '''Test the correct display of the index page'''
    index_urls = ["/", "/index", "/home"]

    for url in index_urls:
        response = client.get(url)
        assert response.status_code == 200

def test_about_display(client):
    '''Test the correct display of the about page'''
    response = client.get('/about')
    assert response.status_code == 200

def test_contact_display(client):
    '''Test the correct display of the contact page'''
    response = client.get('/contact')
    assert response.status_code == 200