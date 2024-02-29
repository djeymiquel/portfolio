from main import app

# Create a test client
app.config['TESTING'] = True
client = app.test_client()

def test_base_route():
    response = client.get('/')
    assert response.status_code == 200
    assert b"Djey Miquel" in response.data 

def test_home_route():
    response = client.get('/home')
    assert response.status_code == 200
    assert b"Home" in response.data

def test_about_route():
    response = client.get('/about')
    assert response.status_code == 200
    assert b"About" in response.data

def test_contact_route():
    response = client.get('/contact')
    assert response.status_code == 200
    assert b"Contact" in response.data

def test_portfolio_route():
    response = client.get('/portfolio')
    assert response.status_code == 200
    assert b"Portfolio" in response.data

def test_skills_route():
    response = client.get('/skills')
    assert response.status_code == 200
    assert b"Skills" in response.data

def test_certificates_route():
    response = client.get('/certificates')
    assert response.status_code == 200
    assert b"Certificates" in response.data