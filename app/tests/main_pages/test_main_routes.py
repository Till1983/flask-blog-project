# Testing the routes of "main_pages" for correct display

def test_index_display(client):
    '''tests the index page'''
    index_urls = ["/", "/index", "/home"]

    for url in index_urls:
        response = client.get(url)
        assert response.status_code == 200

def test_about_display(client):
    '''tests the about page'''
    response = client.get('/about')
    assert response.status_code == 200

def test_contact_display(client):
    '''tests the contact page'''
    response = client.get('/contact')
    assert response.status_code == 200