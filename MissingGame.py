import os
from User import User
from story_printer import StoryPrinter
from DramaManagerAlg import train_algorithm


class MissingGame():
    def __init__(self, user_id):
        self.indeces = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n'
        ]
        self.users = ["U{}".format(i) for i in range(1, 11)]
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
        algo = train_algorithm()

        story_printer = StoryPrinter(self.user.current_index)
        choice = 0
        while choice not in story_printer.choices:
            try:
                choice = int(input())
                if choice == 1:
                    algo.estimate(self.users.index(self.user.userID),
                                  self.indeces.index(self.user.current_index))
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