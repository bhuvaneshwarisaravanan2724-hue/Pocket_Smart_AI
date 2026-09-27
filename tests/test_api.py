def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_login_page(client):
    response = client.get("/login")
    assert response.status_code == 200


def test_register_page(client):
    response = client.get("/register")
    assert response.status_code == 200


def test_dashboard(client):
    response = client.get("/dashboard")
    assert response.status_code == 200


def test_home_planner(client):
    response = client.get("/planners/home")
    assert response.status_code == 200


def test_party_planner(client):
    response = client.get("/planners/party")
    assert response.status_code == 200


def test_jewelry_planner(client):
    response = client.get("/planners/jewelry")
    assert response.status_code == 200