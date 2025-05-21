from app import create_app
import pytest

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        from app.database import db
        db.create_all()

    yield client


def test_create_and_get_task(client):
    response = client.post('/tasks', json={"title": "Integration Task"})
    assert response.status_code == 201

    response = client.get('/tasks')
    data = response.get_json()
    assert any(task['title'] == "Integration Task" for task in data)
