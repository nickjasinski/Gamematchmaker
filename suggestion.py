
from game import Game

class Suggestion:
    def __init__(self, suggestionId: int, content: str):
        self.suggestionId = []
        self.content = content

    def addSuggestion(self):
        """Add Suggestion Menu"""

        while True:
            print("\nWhat would you like to do?")
            print("1. Add a Suggestion")
            print("2. See Suggestions List")
            print("3. Remove a Suggestion")
            choice = input("\nEnter preference (or 'q' to quit): ").strip()

            if choice.lower() == 'q':
                print("\nExiting Suggestion Menu.\n")
                break

            if choice == "1":
                add = input("\nEnter your suggestion (or 'q' to cancel): ").strip()
                if add.lower() == 'q':
                    continue
                self.suggestionId.append(add)
                print(f"{add} has been added!")

            elif choice == "2":
                print("\nSuggestions:")
                if not self.suggestionId:
                    print("No suggestions yet.")
                else:
                    for suggestion in self.suggestionId:
                        print(f"- {suggestion}")

            elif choice == "3":
                remove = input("\nEnter the name of the suggestion to remove (or 'q' to cancel): ").strip()
                if remove.lower() == 'q':
                    continue
                if remove in self.suggestionId:
                    self.suggestionId.remove(remove)
                    print(f"{remove} has been removed!")
                else:
                    print(f"{remove} was not in your suggestions list.")

            else:
                print("Invalid option.")