# run: python -m pytest test_get_friend_profile.py

import pytest
from unittest.mock import MagicMock, ANY
from postgres_handler import PostgresHandler

@pytest.fixture
def mock_postgres_handler():
    """Fixture to create a mock PostgresHandler with a mocked database connection."""
    mock_postgres = MagicMock()
    handler = PostgresHandler(mock_postgres)
    return handler

def test_get_friend_profile_success(mock_postgres_handler):
    """Test retrieving a friend's profile by user_id."""

    mock_cursor = MagicMock()
    mock_postgres_handler.postgres.getSession.return_value = mock_cursor

    mock_cursor.fetchone.return_value = {
        "user_id": 2,
        "name": "Bob",
        "favorite_game": "The Witcher 3",
        "bio": "I love RPGs!"
    }

    user_id = 2
    profile = mock_postgres_handler.getProfile(user_id)

    # Check that execute was called with the correct parameter tuple
    mock_cursor.execute.assert_any_call(ANY, (user_id,))

    # Validate returned data
    assert profile["name"] == "Bob"
    assert profile["favorite_game"] == "The Witcher 3"
    assert profile["bio"] == "I love RPGs!"

def test_get_friend_profile_not_found(mock_postgres_handler):
    """Test retrieving a profile that does not exist returns None."""

    mock_cursor = MagicMock()
    mock_postgres_handler.postgres.getSession.return_value = mock_cursor
    mock_cursor.fetchone.return_value = None

    profile = mock_postgres_handler.getProfile(999)

    # We don't care about the exact query string here
    mock_cursor.execute.assert_called_once()
    assert profile is None
