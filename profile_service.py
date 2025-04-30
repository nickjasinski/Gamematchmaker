from user_profile import Profile
from abstract_data_handler import AbstractDataHandler
from user import User


class ProfileService:
    def __init__(self, data_handler: AbstractDataHandler):
        self.data_handler = data_handler

    def editProfile(self, name: str, favorite_game: str, bio: str, user: User) -> bool:
        profile = Profile(
            name=name, favorite_game=favorite_game, bio=bio, user=user)
        try:
            self.data_handler.saveProfile(profile)
            user.profile = profile
            return True
        except Exception as e:
            print(f"[ERROR] Failed to update profile: {e}")
            return False
    
    def getProfile(self, user: User):
        data = self.data_handler.getProfile(user.userID)
        if data:
            from user_profile import Profile
            profile = Profile(
                name=data['name'],
                favorite_game=data['favorite_game'],
                bio=data['bio'],
                user=user
            )
            user.profile = profile  # Optionally update in-memory state
            return profile
        return None

    def deleteProfile(self, user: User) -> bool:
        try:
            self.data_handler.deleteProfile(user.userID)
            user.profile = None  # Optional: clear in-memory profile
            return True
        except Exception as e:
            print(f"[ERROR] Failed to delete profile: {e}")
            return False

