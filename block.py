from user import User

class Block:
    def __init__(self, user: 'User'):
        self.user = user
        self.blocked_users = []  

    def blockusers(self):
        """Block Users Menu"""

        while True:
            print("\nWhat would you like to do?")
            print("1. Block a User")
            print("2. See Blocked Users List")
            print("3. Remove a Blocked User")
            choice = input("\nEnter preference (or 'q' to quit): ").strip()

            if choice.lower() == 'q':
                print("\nExiting Block Menu.\n")
                break

            if choice == "1":
                add = input("\nEnter the name of the user to block (or 'q' to cancel): ").strip()
                if add.lower() == 'q':
                    continue
                self.blocked_users.append(add)
                print(f"{add} has been blocked!")

            elif choice == "2":
                print("\nBlocked Users:")
                if not self.blocked_users:
                    print("No users blocked yet.")
                else:
                    for user in self.blocked_users:
                        print(f"- {user}")

            elif choice == "3":
                remove = input("\nEnter the name of the user to unblock (or 'q' to cancel): ").strip()
                if remove.lower() == 'q':
                    continue
                if remove in self.blocked_users:
                    self.blocked_users.remove(remove)
                    print(f"{remove} has been unblocked!")
                else:
                    print(f"{remove} was not in your blocked list.")

            else:
                print("Invalid option.")
