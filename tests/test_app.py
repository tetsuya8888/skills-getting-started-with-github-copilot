from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_remove_participant_from_activity():
    original_participants = activities["Chess Club"]["participants"].copy()
    try:
        response = client.delete(
            "/activities/Chess Club/signup",
            params={"email": "michael@mergington.edu"},
        )

        assert response.status_code == 200
        assert "Removed" in response.json()["message"]
        assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]
    finally:
        activities["Chess Club"]["participants"] = original_participants
