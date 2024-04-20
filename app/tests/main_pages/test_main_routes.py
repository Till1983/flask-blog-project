# Testing the routes of "main_pages" for correct display

def test_index_display(client):
    index_urls = ["/", "/index", "/home"]

    for url in index_urls:
        response = client.get(url)
        assert response.status_code == 200

def test_about_display(client):
    response = client.get('/about')
    assert response.status_code == 200

def test_contact_display(client):
    response = client.get('/contact')
    assert response.status_code == 200