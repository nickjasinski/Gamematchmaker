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
    print("6. Like a Review")
    print("7. Dislike a Review")
    print("8. Add Friend")
    print("9. Manage Preferences")
    print("10. Edit Profile")
    print("11. Display Profile")
    print("12. Search for Game Recommendations")
    print("13. Delete Profile")
    print("14. Log Out")
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

            # Ask to create a profile
            if current_user:
                choice_profile = input("Would you like to create a profile now? (yes/no): ").strip().lower()

                if choice_profile == 'yes':
                    name = input("Enter your name: ")
                    favorite_game = input("Enter your favorite game: ")
                    bio = input("Write a short bio: ")
                    controller.editProfile(current_user, name, favorite_game, bio)
                else:
                    # Save empty profile
                    controller.editProfile(current_user, "", "", "")
                    print("Profile skipped. You can create it later from the menu.")

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


        elif choice == '6': #Like a review
            review_id = int(input("Enter the Review ID to like: "))
            review = controller.getReviewById(review_id)
            if review:
                controller.likeReview(review)
                print("You liked the review!")
            else:
                print("Review not found.")
        
        elif choice == '7': #Dislike a review
            review_id = int(input("Enter the Review ID to dislike: "))
            review = controller.getReviewById(review_id)
            if review:
                controller.dislikeReview(review)
                print("You disliked the review!")
            else:
                print("Review not found.")

        elif choice == '8': #Add friend
            print("Adding ... to friends list\n")

        elif choice == '9': #Manage preferences
            preferences.updatePreferences()

        elif choice == '10': #Edit profile
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

        elif choice == '11': #Display profile
            if current_user:
                controller.displayProfile(current_user)
            else:
                print("You must be logged in to view your profile.\n")
                
        elif choice == '12': #Game recommendations
            print("Searching for game recommendations ...\n")
            controller.search_recommended_games()
 
        elif choice == '13':  # Delete Profile
            if current_user and current_user.profile:
                confirm = input("Are you sure you want to delete your profile? (yes/no): ")
                if confirm.lower() == "yes":
                    controller.deleteProfile(current_user)
                else:
                    print("Profile deletion canceled.")
            else:
                print("No profile found or not logged in.")

        elif choice == '14':  # Log Out
            if current_user:
                current_user.logOut()
                current_user = None
            else:
                print("No user is currently logged in.")


        elif choice == '0': #Exit
            print("Goodbye! See you soon!\n")
            break

        else:
            print("Invalid choice. Please enter a number from 0 to 8.\n")


if __name__ == "__main__":
    run()