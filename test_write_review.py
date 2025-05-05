# Joseph Schildt
import pytest
from unittest.mock import MagicMock
from controller import Controller
from user import User
from review import Review

@pytest.fixture
def mock_controller():
    controller = Controller()
    controller.data_handler = MagicMock()
    return controller

def test_write_review_success(mock_controller):
    user = User(userID=1, username="testuser", email="test@example.com", password="pass")
    game_name = "Elden Ring"
    content = "Amazing game!"
    rating = 5

    mock_controller.writeReview(user, game_name, content, rating)
    mock_controller.data_handler.saveReview.assert_called_once()
    saved_review = mock_controller.data_handler.saveReview.call_args[0][0]

    assert isinstance(saved_review, Review)
    assert saved_review.userID == 1
    assert saved_review.gameName == game_name
    assert saved_review.content == content
    assert saved_review.rating == rating

def test_write_review_invalid_rating(mock_controller):
    user = User(userID=1, username="testuser", email="test@example.com", password="pass")
    game_name = "Skyrim"
    content = "Great game!"
    invalid_rating = 10

    with pytest.raises(ValueError):
        mock_controller.writeReview(user, game_name, content, invalid_rating)

def test_write_review_db_failure(mock_controller):
    user = User(userID=2, username="testuser2", email="t2@example.com", password="pass")
    game_name = "Zelda"
    content = "Loved it"
    rating = 5

    mock_controller.data_handler.saveReview.side_effect = Exception("DB error")

    with pytest.raises(Exception, match="DB error"):
        mock_controller.writeReview(user, game_name, content, rating)
