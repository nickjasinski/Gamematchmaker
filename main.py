from controller import Controller
from igdb_fetcher import IGDBFetcher
from game_service import GameService
from preferences import Preferences
from block import Block
from suggestion import Suggestion


def main_menu():
    print("\n==== GameMatch Recommender ====")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Search for Game Title")
    print("4. Manage Wishlist")
    print("5. Review Menu")
    print("6. Friend Menu")
    print("7. Block Menu")
    print("8. Profile Menu")
    print("9. Manage Preferences")
    print("10. Add Suggestion")
    print("11. Search for Game Recommendations")
    print("0. Exit\n")
    return input("Choose an option: ")

def run():
    controller = Controller()
    current_user = None
    blocker = Block(user = "placeholder")
    preferences = Preferences(
                preferenceId=1,
                preferredGenre="None",
                preferredPlatform="None",
                multiplayerPreference=True)
    
    suggest = Suggestion(
                suggestionId=1,
                content="fix bugs in the game")

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

        elif choice == '5':
            """Review Menu"""
            while True:
                print("\nWhat would you like to do?")
                print("1. Write a review")
                print("2. Like a Review")
                print("3. Dislike a Review")
                print("4. View a Review")
                choice = input("\nEnter selection (or 'q' to quit:) ").strip()

                if choice.lower() == 'q':
                    print("\nExiting Review Menu.\n")
                    break

                if choice == "1":
                    if current_user:
                        print("Writing a review ...\n")

                        game_name = input("Enter the name of the game you want to review: ")
                        content = input("Enter your review: ")
                        rating = int(input("Enter a rating (1-5): "))

                        controller.writeReview(current_user, game_name, content, rating)
                    else:
                        print("You must be logged in to write a review.\n")


                if choice == '2': #Like a review
                    review_id = int(input("Enter the Review ID to like: "))
                    review = controller.getReviewById(review_id)
                    if review:
                        controller.likeReview(review)
                        print("You liked the review!")
                    else:
                        print("Review not found.")
        
                if choice == '3': #Dislike a review
                    review_id = int(input("Enter the Review ID to dislike: "))
                    review = controller.getReviewById(review_id)
                    if review:
                        controller.dislikeReview(review)
                        print("You disliked the review!")
                    else:
                        print("Review not found.")
                if choice == '4': # view reviews
                    review_id = input("Enter the review ID you want to view: ")
                    controller.view_review_by_id(review_id)

        elif choice == '6':
            """Friend Menu"""
            while True:
                print("\nWhat would you like to do?")
                print("1. Add Friend")
                print("2. Remove Friend")
                print("3. View Friend's Profile")
                print("4. View Friends List")
                choice = input("\nEnter selection (or 'q' to quit:) ").strip()

                if choice.lower() == 'q':
                    print("\nExiting Review Menu.\n")
                    break
                
                if choice == '1': # Add friend
                    if current_user:
                        friend_email = input("Enter the email of the friend to add: ")
                        friend_user = controller.get_user_by_email(friend_email)

                        if friend_user:
                            controller.addFriend(current_user, friend_user)
                        else:
                            print("No user found with that email.\n")
                    else:
                        print("Please log in first to add friends.\n")

                if choice == '2': # Remove friend
                    if current_user:
                        friend_email = input("Enter the email of the friend to remove: ")
                        friend_user = controller.get_user_by_email(friend_email)

                        if friend_user:
                            controller.removeFriend(current_user, friend_user)
                        else:
                            print("No user found with that email.\n")
                    else:
                        print("Please log in first to remove friends.\n")

                if choice == '3': #View friend's profile
                    if current_user:
                        friend_email = input("Enter your friend's email: ")
                        friend_user = controller.get_user_by_email(friend_email)

                        if friend_user:
                            controller.displayProfile(friend_user)
                        else:
                            print("No user found with that email.\n")
                    else:
                        print("Please log in first to view friend profiles.\n")

                if choice == '4': #View friends list
                    if current_user:
                        print("Fetching friends list...\n")
                        controller.viewFriendsList(current_user)
                    else:
                        print("Please log in first to view your friends list.\n")

        elif choice == '7': #Block users
            blocker.blockusers()

        elif choice == '8': #Profile menu
            while True:
                print("\nWhat would you like to do?")
                print("1. Edit Profile")
                print("2. Display Profile")
                print("3. Delete Profile")
                choice = input("\nEnter selection (or 'q' to quit:) ").strip()

                if choice.lower() == 'q':
                    print("\nExiting Profile Menu.\n")
                    break

            
                elif choice == '1': #Edit profile
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

                elif choice == '2': #Display profile
                    if current_user:
                        controller.displayProfile(current_user)
                    else:
                        print("You must be logged in to view your profile.\n")

                elif choice == '3':  # Delete Profile
                    if current_user and current_user.profile:
                        confirm = input("Are you sure you want to delete your profile? (yes/no): ")
                        if confirm.lower() == "yes":
                            controller.deleteProfile(current_user)
                        else:
                            print("Profile deletion canceled.")
                    else:
                        print("No profile found or not logged in.")

        elif choice == '9': #Manage preferences
            preferences.updatePreferences()

        elif choice == '10': #Add suggestion
            suggest.addSuggestion()

        elif choice == '11': #Game recommendations
            print("Searching for game recommendations ...\n")
            controller.search_recommended_games()
 
        elif choice == '0': #Exit
            print("Goodbye! See you soon!\n")
            break

        else:
            print("Invalid choice. Please enter a number from 0 to 8.\n")


if __name__ == "__main__":
    run()