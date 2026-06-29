from fastapi.testclient import TestClient

from src import app as app_module


client = TestClient(app_module.app)


def test_unregister_participant_removes_email_from_activity():
    app_module.activities["Chess Club"]["participants"] = [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]

    response = client.delete(
        "/activities/Chess Club/participants/daniel@mergington.edu"
    )

    assert response.status_code == 200
    assert "daniel@mergington.edu" not in app_module.activities["Chess Club"]["participants"]
    assert "michael@mergington.edu" in app_module.activities["Chess Club"]["participants"]


def test_unregister_participant_returns_404_for_unknown_participant():
    app_module.activities["Chess Club"]["participants"] = [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]

    response = client.delete(
        "/activities/Chess Club/participants/unknown@mergington.edu"
    )

    assert response.status_code == 404
