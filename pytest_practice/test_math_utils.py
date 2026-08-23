from fastapi.testclient import TestClient
from math_utils import app

client = TestClient(app)


# ── ১. GET request test ──
def test_read_root_does_not_exist():
    response = client.get("/")
    assert response.status_code == 404  # ei route amra banai ni, tai 404 expected


# ── ২. POST request test (success case) ──
def test_register_success():
    response = client.post(
        "/register", json={"username": "mahmud", "password": "mypassword123"}
    )
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}


# ── ৩. POST request test (failure case — duplicate user) ──
def test_register_duplicate_user():
    # প্রথমবার register — pass হবে
    client.post("/register", json={"username": "duplicate_user", "password": "pass123"})

    # দ্বিতীয়বার একই username দিয়ে আবার register — fail হওয়ার কথা
    response = client.post(
        "/register", json={"username": "duplicate_user", "password": "pass123"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "User already exists"


# ── ৪. Login success case ──
def test_login_success():
    client.post("/register", json={"username": "login_test", "password": "correctpass"})

    response = client.post(
        "/login", json={"username": "login_test", "password": "correctpass"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()  # token আছে কিনা check


# ── ৫. Login failure case (wrong password) ──
def test_login_wrong_password():
    client.post("/register", json={"username": "user2", "password": "rightpass"})

    response = client.post(
        "/login", json={"username": "user2", "password": "wrongpass"}
    )
    assert response.status_code == 401


# ── ৬. Protected route WITHOUT token ──
def test_profile_without_token():
    response = client.get("/profile")  # headers দিচ্ছি না
    assert response.status_code == 401


# ── ৭. Protected route WITH token (headers ব্যবহার) ──
def test_profile_with_token():
    response = client.get(
        "/profile", headers={"Authorization": "Bearer fake-jwt-token"}
    )
    assert response.status_code == 200
    assert response.json()["username"] == "test_user"
