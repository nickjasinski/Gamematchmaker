from controller import Controller

# main.py
from igdb_fetcher import IGDBFetcher
from game_service import GameService


def main_menu():
    print("\n==== Video Game Finder ====")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Search for Game Title")
    print("4. Save Game to Wishlist")
    print("5. Write a Review")
    print("6. Add Friend")
    print("7. Manage Preferences")
    print("0. Exit\n")
    return input("Choose an option: ")
    

def run():
    
    current_user = None  # Placeholder for User 
    controller = Controller()
    while True:
        choice = main_menu()

        if choice == '1':
            print("Signing up ...\n")

        elif choice == '2':
            print("Logging in ...\n")

        elif choice == '3':
            controller.search_game_by_title()

        elif choice == '4':
            print("Saving ... to wishlist ...\n")

        elif choice == '5':
            print("Writing a review ...\n")
        
        elif choice == '6':
            print("Adding ... to friends list\n")

        elif choice == '7':
            print("Managing preferences ...\n")

        elif choice == '0':
            print("Goodbye! See you soon!\n")
            break
        
        else:
            print("Invalid choice. Please enter a number from 0 to 7.\n")

if __name__ == "__main__":
    run()


