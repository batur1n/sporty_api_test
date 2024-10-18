import requests
import pytest

BASE_URL = "https://poetrydb.org"

def test_get_random_poem():
    response = requests.get(f"{BASE_URL}/poem/random")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert 'title' in data
    assert 'author' in data
    assert 'lines' in data
    assert data['lines']

def test_get_poems_by_author():
    response = requests.get(f"{BASE_URL}/author/Emily%20Dickinson")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for poem in data:
        assert 'title' in poem
        assert 'author' in poem
        assert 'lines' in poem

def test_invalid_author_request():
    response = requests.get(f"{BASE_URL}/author/NonexistentAuthor")
    assert response.status_code == 404
    data = response.json()
    assert 'error' in data

def test_get_poems_by_title():
    response = requests.get(f"{BASE_URL}/title/Hope")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for poem in data:
        assert 'title' in poem
        assert 'author' in poem
        assert 'lines' in poem

def test_invalid_title_request():
    response = requests.get(f"{BASE_URL}/title/NonexistentTitle")
    assert response.status_code == 404
    data = response.json()
    assert 'error' in data
