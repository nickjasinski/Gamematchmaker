# run the test file: python -m pytest test_save_friend.py

import pytest
from unittest.mock import MagicMock, call, ANY
from postgres_handler import PostgresHandler
from user import User

@pytest.fixture
def mock_postgres_handler():
    """Fixture to create a mock PostgresHandler with a mocked database connection."""
    mock_postgres = MagicMock()
    handler = PostgresHandler(mock_postgres)
    return handler

def test_save_friend_success(mock_postgres_handler):
    """Test adding a friend successfully updates the friends list in the database."""

    user = User(userID=1, username="alice", email="alice@example.com", password="pass")
    friend = User(userID=2, username="bob", email="bob@example.com", password="pass")

    mock_cursor = MagicMock()
    mock_postgres_handler.postgres.getSession.return_value = mock_cursor

    # Simulate current friends list
    mock_cursor.fetchone.return_value = {"friends": ["charlie@example.com"]}

    # Call the function
    mock_postgres_handler.saveFriend(user, friend)

    # Assert SELECT query was executed
    mock_cursor.execute.assert_any_call(
        ANY,  # Allow any SQL string
        (1,)
    )

    # Assert UPDATE was called with updated friends list
    mock_cursor.execute.assert_any_call(
        ANY,
        (["charlie@example.com", "bob@example.com"], 1)
    )

    # Ensure commit was called
    mock_postgres_handler.postgres.getConnection().commit.assert_called_once()

def test_save_friend_already_exists(mock_postgres_handler):
    """Test that duplicate friend is not added to the friends list."""

    user = User(userID=1, username="alice", email="alice@example.com", password="pass")
    friend = User(userID=2, username="bob", email="bob@example.com", password="pass")

    mock_cursor = MagicMock()
    mock_postgres_handler.postgres.getSession.return_value = mock_cursor

    # Friend already exists
    mock_cursor.fetchone.return_value = {"friends": ["bob@example.com"]}

    # Call the function
    mock_postgres_handler.saveFriend(user, friend)

    # SELECT should be called
    mock_cursor.execute.assert_any_call(
        ANY,
        (1,)
    )

    # Ensure UPDATE was not called since friend already exists
    update_calls = [call for call in mock_cursor.execute.call_args_list if "UPDATE" in str(call)]
    assert not update_calls

    # Ensure commit is not called
    mock_postgres_handler.postgres.getConnection().commit.assert_not_called()
