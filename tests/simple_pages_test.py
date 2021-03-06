"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/flask">Flask</a>' in response.data
    assert b'<a class="nav-link" href="/deployment">Deployment</a>' in response.data
    assert b'<a class="nav-link" href="/glossary">Glossary</a>' in response.data
    assert b'<a class="nav-link" href="/aaa">AAA</a>' in response.data
    assert b'<a class="nav-link" href="/oops">OOPs</a>' in response.data
    assert b'<a class="nav-link" href="/solid">SOLID</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index Page" in response.data

def test_request_git(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_docker(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_flask(client):
    """This makes the index page"""
    response = client.get("/flask")
    assert response.status_code == 200
    assert b"Flask" in response.data

def test_request_deployment(client):
    """This makes the index page"""
    response = client.get("/deployment")
    assert response.status_code == 200
    assert b"Deployment" in response.data

def test_request_glossary(client):
    """This makes the index page"""
    response = client.get("/glossary")
    assert response.status_code == 200
    assert b"Glossary" in response.data

def test_request_aaa(client):
    """This makes the index page"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b"AAA" in response.data

def test_request_oops(client):
    """This makes the index page"""
    response = client.get("/oops")
    assert response.status_code == 200
    assert b"OOPs" in response.data

def test_request_solid(client):
    """This makes the index page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"SOLID" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
