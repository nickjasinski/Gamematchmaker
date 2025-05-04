from game import Game
from genre import Genre

class Preferences:
    def __init__(self, preferenceId: int, preferredGenre: Genre, preferredPlatform: str, multiplayerPreference: bool):
        self.preferenceId = preferenceId
        self.preferredGenre = preferredGenre
        self.preferredPlatform = preferredPlatform
        self.multiplayerPreference = multiplayerPreference

    def updatePreferences(self):
        """Edit Preferences"""

        while True:
            print("")
            print("Which Preference would you like to edit?")
            print("1. Change Preferred Genre")
            print("2. Change Preferred Platform")
            print("3. Change Multiplayer Preference")
            print("")
            print("Current Preferences")
            print(f"Genre: {self.preferredGenre}")
            print(f"Platform: {self.preferredPlatform}")
            print(f"Multiplayer: {self.multiplayerPreference}")
            choice = input("\nEnter preference (or 'q' to quit): ").strip()
            if choice.lower() == 'q':
                break
            print("\n")
            if choice == "1":
                print("Changing Preferred Genre\n")
                new_genre = input("What Genre would you like to have? ")
                self.preferredGenre = new_genre
            elif choice == "2":
                print("Changing Preferred Platform\n")
                new_platform = input("What platform would you like to have? ")
                self.preferredPlatform = new_platform

            elif choice == "3":
                print("Changing Multiplayer Preference\n")
                new_mp = input("Do you prefer multiplayer games? (yes/no): ").strip().lower()
                self.multiplayerPreference = new_mp == "yes"

            else:
                print("Invalid option.")