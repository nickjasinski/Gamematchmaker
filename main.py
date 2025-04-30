from controller import Controller
from preferences import Preferences
from block import Block
from suggestion import Suggestion


def main_menu():
    print("\n==== Video Game Finder ====")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Search for Game Title")
    print("4. Save Game to Wishlist")
    print("5. Write a Review")
    print("6. Add Friend")
    print("7. Manage Preferences")
    print("8. View Blocked Menu")
    print("0. Exit\n")
    return input("Choose an option: ")
    

def run():
    
    controller = Controller()

    preferences = Preferences(
                preferenceId=1,
                preferredGenre="RPG",
                preferredPlatform="PC",
                multiplayerPreference=True)

    blocker = Block(user = "placeholder")

    suggest = Suggestion(
                suggestionId=1,
                content="fix bugs in the game")

    while True:
        choice = main_menu()

        if choice == '1':
            print("Signing up ...\n")

        elif choice == '2':
            print("Logging in ...\n")

        elif choice == '3':
            print("Searching for ...\n")

        elif choice == '4':
            print("Saving ... to wishlist ...\n")

        elif choice == '5':
            print("Writing a review ...\n")
        
        elif choice == '6':
            print("Adding ... to friends list\n")

        elif choice == '7':
            
            preferences.updatePreferences()

        elif choice == '8':
            blocker.blockusers()

        elif choice == '9':
            suggest.addSuggestion()

        elif choice == '0':
            print("Goodbye! See you soon!\n")
            break
        
        else:
            print("Invalid choice. Please enter a number from 0 to 7.\n")

if __name__ == "__main__":
    run()


