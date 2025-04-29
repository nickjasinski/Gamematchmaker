import pytest
from unittest.mock import MagicMock
from postgres_handler import PostgresHandler
from user import User

@pytest.fixture
def mock_postgres_handler():
    """Fixture to create a mock PostgresHandler with a mocked database connection."""
    mock_postgres = MagicMock()
    handler = PostgresHandler(mock_postgres)
    return handler

def test_save_user(mock_postgres_handler):
    """Test saving a user to the database."""
    # Arrange
    user = User(None, "testuser", "testuser@example.com", "password123")
    mock_cursor = MagicMock()
    mock_postgres_handler.postgres.getSession.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {"user_id": 10}

    # Act
    saved_user = mock_postgres_handler.saveUser(user)

    # Assert
    mock_cursor.execute.assert_called_once_with(
        """
            INSERT INTO users (username, email, password)
            VALUES (%s, %s, %s)
            RETURNING user_id
        """,
        ("testuser", "testuser@example.com", "password123")
    )
    mock_postgres_handler.postgres.getConnection().commit.assert_called_once()
    assert saved_user.userID == 10
    assert saved_user.username == "testuser"
    assert saved_user.email == "testuser@example.com"
