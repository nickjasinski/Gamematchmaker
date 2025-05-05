import pytest
from unittest.mock import MagicMock
from controller import Controller
from user import User


def test_add_friend():
    mock_data_handler = MagicMock()
    controller = Controller()
    controller.data_handler = mock_data_handler

    user1 = User(userID=1, username="AA",
                 email="aa@example.com", password="pass")
    user2 = User(userID=2, username="BB",
                 email="bb@example.com", password="pass")

    controller.addFriend(user1, user2)

    mock_data_handler.saveFriend.assert_called_once_with(user1, user2)


def test_remove_friend():
    mock_data_handler = MagicMock()
    controller = Controller()
    controller.data_handler = mock_data_handler

    user1 = User(userID=1, username="AA",
                 email="AA@example.com", password="pass")
    user2 = User(userID=2, username="BB",
                 email="bb@example.com", password="pass")

    controller.removeFriend(user1, user2)

    mock_data_handler.deleteFriend.assert_called_once_with(user1, user2)
