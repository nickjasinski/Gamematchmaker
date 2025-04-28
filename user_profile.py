from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from user import User


class Profile:
    # Python wont try to resolve user right away "user: 'User'"
    def __init__(self, name: str, favorite_game: str, bio: str, user: 'User'):
        self.profile_id = None
        self.name = name
        self.favorite_game = favorite_game
        self.bio = bio
        self.user = user
