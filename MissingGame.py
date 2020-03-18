import os
from User import User
from story_printer import StoryPrinter
# from DramaManagerAlg import DramaManagerAlg


class MissingGame():
    def __init__(self, user_id):
        self.indexes = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n'
        ]
        self.index_experienced = list()
        # alg = DramaManagerAlg()
        # Init current index
        self.user = User(user_id)
        # Run on construction
        self.Start()

    def Start(self):

        self.user.current_index = 'a'
        self.index_experienced.append('a')

        # Do some algorithm stuff
        # alg =
        # alg.fit

        story_printer = StoryPrinter(self.user.current_index)
        choice = 0
        while choice not in story_printer.choices:
            try:
                choice = int(input())
                if choice == 1:
                    # Do some algorithm stuff
                    pass
                elif choice == 2:
                    # Do some other algorithm stuff
                    pass
                else:
                    print("Please enter a valid choice.")
            except ValueError:
                print("Please enter a number for your choice.")


# For testing purposes. Run `python3 MissingGame.py`
def main():
    MissingGame("user1")


if __name__ == "__main__":
    main()