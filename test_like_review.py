#Nick Jasinski
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

def test_like_review_success(mock_controller):
    """Test liking a review successfully."""
    review = Review(1, 2, "GTA V", "Great!", 4)
    
    mock_controller.likeReview(review)

    mock_controller.data_handler.likeReview.assert_called_once_with(review)

def test_dislike_review_success(mock_controller):
    """Test disliking a review successfully."""
    review = Review(2,3,"Skyrim", "Too many dragons",2)

    mock_controller.dislikeReview(review)

    mock_controller.data_handler.dislikeReview.assert_called_once_with(review)

def test_like_review_db_failure(mock_controller):
    """Test liking a review when database throws an error."""
    review = Review(5, 6, "Minecraft", "Fun blocks",5)
    mock_controller.data_handler.likeReview.side_effect = Exception("DB Failure")

    with pytest.raises(Exception, match="DB Failure"):
        mock_controller.likeReview(review)

def test_dislike_review_db_failure(mock_controller):
    """Test disliking a review when database throws an error."""
    review = Review(6, 7, "Portal", "Mind bending", 5)
    mock_controller.data_handler.dislikeReview.side_effect = Exception("DB Failure")

    with pytest.raises(Exception, match="DB Failure"):
        mock_controller.dislikeReview(review)