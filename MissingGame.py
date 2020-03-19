import os
from User import User
from story_printer import StoryPrinter
from DramaManagerAlg import train_algorithms
from numpy.random import RandomState


class MissingGame():
    def __init__(self, seed=None):

        # Init with seed if given for testing
        if seed is None:
            self.random_state = RandomState()
        elif isinstance(seed, int):
            self.random_state = RandomState(seed)
        elif isinstance(seed, RandomState):
            self.random_state = seed
        else:
            raise Exception("{} cannot be used to seed".format(seed))

        self.indeces = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n'
        ]
        self.users_ids = ["U{}".format(i) for i in range(1, 11)]

        # Pick a random user id for the current player
        self.user = User(self.random_state.choice(self.users_ids))
        self.index_experienced = list()
        self.algorithms = list()
        # Run on construction
        self.Start()

    def Start(self):

        self.user.current_index = 'a'
        self.index_experienced.append('a')

        # Load algorithm array for each rating
        self.algorithms = train_algorithms()

        story_printer = StoryPrinter(self.user.current_index)
        choice = 0
        while choice not in story_printer.choices:
            try:
                choice = int(input())
                if choice == 1 or choice == 2:
                    self.update_user_attributes(choice)
                    self.update_user_id()
                else:
                    print("Please enter a valid choice.")
            except ValueError:
                print("Please enter a number for your choice.")

    def update_user_attributes(self, choice):
        # Extract predictions for each corresponding algorithm in index
        item_idx = self.choice_to_item_idx(choice)
        user_idx = self.users_ids.index(self.user.userID)
        # Get prediction from corresponding algorithm.
        # Algorithms are in the same order as the ratings
        self.user.armour = self.algorithms[0].estimate(user_idx, item_idx)
        print("Your armour is predicted to be {}".format(self.user.armour))
        self.user.attack = self.algorithms[1].predict(user_idx, item_idx)
        # and so on...

    def update_user_id(self):
        """
        Update userID attribute using the most frequently repeated neighbour
        across all items and ratings. 
        TODO: Extract neighbors at each item.
        """
        user_idx = self.users_ids.index(self.user.userID)
        # Find the next 3-nearest neighbours user id across all ratings
        # and choose the most frequent one to be the next user id.
        all_neighbors = [
            id for alg in self.algorithms
            for id in alg.get_neighbors(user_idx, 3)
        ]
        # Find mode
        closest_user_idx = max(all_neighbors, key=all_neighbors.count)
        self.user.userID = self.users_ids[closest_user_idx]

    def choice_to_item_idx(self, choice):
        """
        For a given choice, it returns the index of the next node in tree.
        """
        if choice == 1:
            if self.user.current_index == 'a':
                return self.indeces.index('b')
            # returns 1 which is the index of b
        # and so on ...


# For testing purposes. Run `python3 MissingGame.py`
def main():
    MissingGame(seed=100)


if __name__ == "__main__":
    main()