from app.users.models import Author
from app.blogposts.models import Article
import pytest
from datetime import datetime


@pytest.fixture
def sample_author():
    return Author(name='John Doe', email='john@example.com', password='password123')

def test_author_creation(sample_author):
    assert sample_author.name == 'John Doe'
    assert sample_author.email == 'john@example.com'
    assert sample_author.password == 'password123'  


@pytest.fixture
def sample_article(sample_author):
    return Article(
        title='Test Article',
        content='Lorem ipsum dolor sit amet',
        author=sample_author,
        date=datetime.utcnow()
    )

def test_article_creation(sample_article, sample_author):
    assert sample_article.title == 'Test Article'
    assert sample_article.content == 'Lorem ipsum dolor sit amet'
    assert sample_article.author == sample_author
    assert isinstance(sample_article.date, datetime)
