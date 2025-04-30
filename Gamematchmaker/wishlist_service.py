from game import Game
from postgres_handler import PostgresHandler
from wishlist import Wishlist

class WishlistService:
    def __init__(self, data_handler: PostgresHandler):
        self.data_handler = data_handler
        self.wishlists = {}  # Dictionary to store Wishlist objects by user_id

    def getWishlist(self, user_id: int) -> Wishlist:
        """Retrieves the Wishlist for the given user_id from memory or database"""
        if user_id not in self.wishlists:
            # Fetch the wishlist from the database if it doesn't exist in memory
            wishlist_data = self.data_handler.getWishlist(user_id)
            if wishlist_data:
                self.wishlists[user_id] = Wishlist(games=wishlist_data)
            else:
                # Initialize a new Wishlist if none exists in the database
                self.wishlists[user_id] = Wishlist()
        return self.wishlists[user_id]

    def addGame(self, game_name: str, user_id: int) -> bool:
        """Adds a game to the user's wishlist and updates the database"""
        try:
            wishlist = self.getWishlist(user_id)
            if game_name not in wishlist.games:
                wishlist.games.append(game_name)
                self.data_handler.saveWishlist(wishlist, user_id)
                print(f"Game '{game_name}' successfully added to the wishlist.")
                return True
            else:
                print(f"Game '{game_name}' is already in the wishlist.")
                return False
        except Exception as e:
            print(f"Failed to add game '{game_name}' to the wishlist: {e}")
            return False

    def removeGame(self, game_name: str, user_id: int) -> bool:
        """Removes a game from the user's wishlist and updates the database"""
        try:
            wishlist = self.getWishlist(user_id)
            if game_name in wishlist.games:
                wishlist.games.remove(game_name)
                self.data_handler.saveWishlist(wishlist, user_id)
                print(f"Game '{game_name}' successfully removed from the wishlist.")
                return True
            else:
                print(f"Game '{game_name}' not found in the wishlist.")
                return False
        except Exception as e:
            print(f"Failed to remove game '{game_name}' from the wishlist: {e}")
            return False

