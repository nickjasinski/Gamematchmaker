from controller import Controller
from igdb_fetcher import IGDBFetcher
from game_service import GameService
from preferences import Preferences


def main_menu():
    print("\n==== Video Game Finder ====")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Search for Game Title")
    print("4. Manage Wishlist")
    print("5. Write a Review")
    print("6. Add Friend")
    print("7. Manage Preferences")
    print("8. Edit Profile")
    print("9. Display Profile")
    print("10. Search for Game Recommendations")
    print("0. Exit\n")
    return input("Choose an option: ")


def run():
    controller = Controller()
    current_user = None

    preferences = Preferences(
                preferenceId=1,
                preferredGenre="RPG",
                preferredPlatform="PC",
                multiplayerPreference=True)
    while True:
        choice = main_menu()

        if choice == '1': #Sign up
            print("Signing up ...\n")
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = input("Enter password: ")
            current_user = controller.signUp(username, email, password)

        elif choice == '2': #Log in
            print("Logging in ...\n")
            email = input("Enter email: ")
            password = input("Enter password: ")
            current_user = controller.logIn(email, password)

            if current_user:
                print(
                    f"\nLogin successful! Welcome, {current_user.username}.\n")
            else:
                print("Login failed. Please check your email and password.\n")

        elif choice == '3': #Search for game by title
            controller.search_game_by_title()

        elif choice == '4': #Manage wishlist
            if current_user:
                controller.manage_wishlist(current_user) 
            else:
                print("Please log in first to manage your wishlist.\n")

        elif choice == '5': #Writing a review
            if current_user:
                print("Writing a review ...\n")

                game_title = input("Enter the title of the game you want to review: ")
                game = controller.search_game_by_title_return_game(game_title)

                if game:
                    content = input("Enter your review: ")
                    rating = int(input("Enter a rating (1-5): "))

                    new_review = current_user.writeReview(game, content, rating)

                    controller.saveReview(new_review)

                    print("Review was submitted successfully!\n")

                else:
                    print("Game not found. Please try again.\n")
            else:
                print("You must be logged in to write a review.\n")

        elif choice == '6': #Add friend
            print("Adding ... to friends list\n")

        elif choice == '7': #Manage preferences
            preferences.updatePreferences()

        elif choice == '8': #Edit profile
            if current_user:
                print("Editing profile...\n")
                name = input("Enter your name: ")
                favorite_game = input("Enter your favorite game: ")
                bio = input("Write a short bio: ")
                success = controller.editProfile(
                    current_user, name, favorite_game, bio)
                if success:
                    print("Profile updated successfully!\n")
                else:
                    print("Failed to update profile.\n")
            else:
                print("Please log in first to edit your profile.\n")

        elif choice == '9': #Display profile
            if current_user:
                controller.displayProfile(current_user)
            else:
                print("You must be logged in to view your profile.\n")
                
        elif choice == '10': #Game recommendations
            print("Searching for game recommendations ...\n")
            controller.search_recommended_games()
 
        elif choice == '0': #Exit
            print("Goodbye! See you soon!\n")
            break

        else:
            print("Invalid choice. Please enter a number from 0 to 8.\n")


if __name__ == "__main__":
    run()