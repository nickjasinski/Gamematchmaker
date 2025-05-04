class Suggestion:
    def __init__(self, suggestionId:int, content: str):
        self.suggestions = []
        self.content = content

    def addSuggestion(self):
        """Suggestion Menu"""
        while True:
            print("\nWhat would you like to do?")
            print("1. Add a Suggestion")
            print("2. See Suggestions List")
            print("3. Remove a Suggestion")

            choice = input("\nEnter your choice (or 'q' to quit): ").strip().lower()

            if choice == 'q':
                print("\nExiting Suggestion Menu.\n")
                break

            elif choice == "1":
                game = input("Enter the game title: ").strip()
                if game.lower() == 'q':
                    continue

                suggestion = input("Enter your suggestion: ").strip()
                if suggestion.lower() == 'q':
                    continue

                full_suggestion = f"{game}: {suggestion}"
                self.suggestions.append(full_suggestion)
                print(f"Suggestion added for {game}!")

            elif choice == "2":
                print("\nSuggestions List:")
                if not self.suggestions:
                    print("No suggestions yet.")
                else:
                    for s in self.suggestions:
                        print(f"- {s}")

            elif choice == "3":
                print("\nCurrent Suggestions:")
                for i, s in enumerate(self.suggestions, start=1):
                    print(f"{i}. {s}")
                index = input("Enter the number of the suggestion to remove (or 'q' to cancel): ").strip()
                if index.lower() == 'q':
                    continue
                try:
                    idx = int(index) - 1
                    removed = self.suggestions.pop(idx)
                    print(f"Removed: {removed}")
                except (ValueError, IndexError):
                    print("Invalid number.")

            else:
                print("Invalid option.")
