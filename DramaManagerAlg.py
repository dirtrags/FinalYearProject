import os
from numpy import mean
from surprise import BaselineOnly
from surprise import Dataset
from surprise import AlgoBase
from surprise import Reader
from surprise import PredictionImpossible


class DramaManagerAlg(AlgoBase):
    """
    My :mod: `DramaManagerAlg <Missing.DramaManagerAlg>`

    .. autosummary ..
        :no signatures:

        Predict (Takes in User in current index and data)


    """

    #Set definition and format of dataset
    file_path = os.path.expanduser('.data/UserData.csv')
    reader = Reader(
        line_format=
        'index userID funvalue attack magic armour skill Ny_Know Pm_Know El_Know Br_Know',
        sep='\t',
        rating_scale=(-30, 30))
    UserData = Dataset.load_from_file(file_path, reader=reader)

    def __init__(self, sim_options={'name': 'cosine', 'User_based': True}):
        AlgoBase.__init__(self, sim_options=sim_options)

    def fit(self, trainset):
        Algobase.fit(self, UserData)

        #Compute similarites and baseline
        self.bu, self.bi = self.compute_baselines()
        self.sim = self.compute_similarities()

        return self

    def estimate(self, User, index):

        #Catch Impossible predictions
        if not (self.UserData.knows_user(User)
                and self.UserData.knows_item(i)):
            raise PredictionImpossible('User and or Item are unknown')
        elif User.currentIndex == a and not (index == b):
            raise PredictionImpossible(
                'User current Index and Prediction invalid due to tree')
        elif User.currentIndex == b and not (index == c):
            raise PredictionImpossible(
                'User current Index and Prediction invalid due to tree')
        elif User.currentIndex == c and not (index == d):
            raise PredictionImpossible(
                'User current Index and Prediction invalid due to tree')
        elif User.currentIndex == d and not (index == g):
            raise PredictionImpossible(
                'User current Index and Prediction invalid due to tree')
        elif User.currentIndex == e and not (index == h or index == i):
            raise PredictionImpossible(
                'User current Index and Prediction invalid due to tree')
        elif User.currentIndex == f and not (index == j or index == k):
            raise PredictionImpossible(
                'User current Index and Prediction invalid due to tree')
        elif User.currentIndex == g:
            raise PredictionImpossible(
                'User current Index and Prediction invalid due to tree - End Index'
            )
        elif User.currentIndex == h and not (index == n):
            raise PredictionImpossible(
                'User current Index and Prediction invalid due to tree')
        elif User.currentIndex == i and not (index == n or index == l):
            raise PredictionImpossible(
                'User current Index and Prediction invalid due to tree')
        elif User.currentIndex == j:
            raise PredictionImpossible(
                'User current Index and Prediction invalid due to tree - End Index'
            )
        elif User.currentIndex == k:
            raise PredictionImpossible(
                'User current Index and Prediction invalid due to tree - End Index'
            )
        elif User.currentIndex == n:
            raise PredictionImpossible(
                'User current Index and Prediction invalid due to tree - End Index'
            )
        elif User.currentIndex == m:
            raise PredictionImpossible(
                'User current Index and Prediction invalid due to tree - End Index'
            )
        elif User.currentIndex == l:
            raise PredictionImpossible(
                'User current Index and Prediction invalid due to tree - End Index'
            )

        neighbours = [(v, self.sim[User, v])
                      for (v, r) in self.UserData.ir[index]]
        neighbours = sorted(neighbours, key=lambda x: x[1], reverse=True)

        print('The 3 nearest neighbours of user', str(User.userID), 'are:')
        for v, sim_Userv in neighbours[:3]:
            print('user {0:} with sim {1:1.2f}'.format(v, sim_Userv))

        prediction = mean(sim_Userv for (v, sim_Userv) in neighbours[:3])
        return prediction