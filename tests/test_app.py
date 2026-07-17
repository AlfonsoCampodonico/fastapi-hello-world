from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_says_hello_from_laravel_cloud():
    resp = client.get("/")
    assert resp.status_code == 200
    body = resp.json()
    assert body["message"] == "Hello from Laravel Cloud 👋"
    assert body["docs"] == "/docs"


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_greetings_are_seeded_with_laravel_cloud():
    resp = client.get("/api/v1/greetings")
    assert resp.status_code == 200
    assert any("Laravel Cloud" in g["message"] for g in resp.json())


def test_create_then_fetch_greeting():
    created = client.post("/api/v1/greetings", json={"message": "Bonjour", "language": "fr"})
    assert created.status_code == 201
    greeting_id = created.json()["id"]

    fetched = client.get(f"/api/v1/greetings/{greeting_id}")
    assert fetched.status_code == 200
    assert fetched.json()["message"] == "Bonjour"
    assert fetched.json()["language"] == "fr"


def test_create_greeting_rejects_empty_message():
    resp = client.post("/api/v1/greetings", json={"message": ""})
    assert resp.status_code == 422  # fails Pydantic min_length validation


def test_missing_greeting_returns_404():
    resp = client.get("/api/v1/greetings/999999")
    assert resp.status_code == 404
    assert "not found" in resp.json()["detail"].lower()


def test_openapi_schema_is_exposed():
    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    schema = resp.json()
    assert schema["info"]["title"] == "Hello from Laravel Cloud"
    assert "/api/v1/greetings" in schema["paths"]
