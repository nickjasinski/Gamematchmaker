#Carter Bojan
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
    user = User(None, "testuser", "testuser@example.com", "password123")
    mock_cursor = MagicMock()
    mock_postgres_handler.postgres.getSession.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {"user_id": 100}

    saved_user = mock_postgres_handler.saveUser(user)

    mock_cursor.execute.assert_called_once_with(
        """
                INSERT INTO users (username, email, password)
                VALUES (%s, %s, %s)
                RETURNING user_id
                """,
        ("testuser", "testuser@example.com", "password123")
    )
    mock_postgres_handler.postgres.getConnection().commit.assert_called_once()
    assert saved_user.userID == 100
    assert saved_user.username == "testuser"
    assert saved_user.email == "testuser@example.com"

def test_save_user_invalid_data(mock_postgres_handler):
    """Test saving a user with invalid data."""
   
    user = User(None, "", "invalidemail", "")  
    mock_cursor = MagicMock()
    mock_postgres_handler.postgres.getSession.return_value = mock_cursor

    with pytest.raises(ValueError):  
        mock_postgres_handler.saveUser(user)

def test_save_user_db_failure(mock_postgres_handler):
    """Test saving a user when the database insertion fails."""

    user = User(None, "testuser", "testuser@example.com", "password123")
    mock_cursor = MagicMock()
    mock_postgres_handler.postgres.getSession.return_value = mock_cursor
    mock_cursor.execute.side_effect = Exception("Database error")

  
    with pytest.raises(Exception, match="Database error"):
        mock_postgres_handler.saveUser(user)
    mock_postgres_handler.postgres.getConnection().rollback.assert_called_once()
