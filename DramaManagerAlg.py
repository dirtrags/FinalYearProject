from surprise import BaselineOnly
from surprise import Dataset
from surprise import AlgoBase
from surprise import Reader
from surprise import PredictionImpossible

"""
My :mod: `DramaManagerAlg <Missing.DramaManagerAlg>`

.. autosummary ..
    :no signatures:

    Predict (Takes in User in current index and data)


"""
class DramaManagerAlg(AlgoBase):

    

    #Set definition and format of dataset
    file_path = os.path.expanduser('~/Missing/UserData.csv')
    reader = Reader(line_format='index userID funvalue attack magic armour skill Ny_Know Pm_Know El_Know Br_Know' sep='\t', rating_scale=(-30,30))
    UserData = Dataset.load_from_file(file_path, reader=reader)

    def __init__(self, sim_options={'name': 'cosine', 'User_based': True}):
        AlgoBase.__init__(self,sim_options = sim_options)
    
    def fit(self, trainset):
        Algobase.fit(self,UserData)

        #Compute similarites and baseline
        self.bu, self.bi = self.compute_baselines()
        self.sim = self.compute_similarities()

        return self

    def estimate(self, User, index)
       
        #Catch Impossible predictions       
        if not(self.UserData.knows_user(User) and self.UserData.knows_item(i)):
            raise PredictionImpossible('User and or Item are unknown')
        elif User.currentIndex == a and not(index == b):
            raise PredictionImpossible('User current Index and Prediction invalid due to tree')
        elif User.currentIndex == b and not(index == c):
            raise PredictionImpossible('User current Index and Prediction invalid due to tree')
        elif User.currentIndex == c and not(index == d):
            raise PredictionImpossible('User current Index and Prediction invalid due to tree')
        elif User.currentIndex == d and not(index == g):
            raise PredictionImpossible('User current Index and Prediction invalid due to tree')
        elif User.currentIndex == e and not(index == h or index == i):
            raise PredictionImpossible('User current Index and Prediction invalid due to tree')
        elif User.currentIndex == f and not(index == j or index == k):
            raise PredictionImpossible('User current Index and Prediction invalid due to tree')
        elif User.currentIndex == g:
            raise PredictionImpossible('User current Index and Prediction invalid due to tree - End Index')
        elif User.currentIndex == h and not(index == n):
            raise PredictionImpossible('User current Index and Prediction invalid due to tree')
        elif User.currentIndex == i and not(index == n or index == l):
            raise PredictionImpossible('User current Index and Prediction invalid due to tree')
        elif User.currentIndex == j:
            raise PredictionImpossible('User current Index and Prediction invalid due to tree - End Index')
        elif User.currentIndex == k:
            raise PredictionImpossible('User current Index and Prediction invalid due to tree - End Index')
        elif User.currentIndex == n:
            raise PredictionImpossible('User current Index and Prediction invalid due to tree - End Index')
        elif User.currentIndex == m:
            raise PredictionImpossible('User current Index and Prediction invalid due to tree - End Index')
        elif User.currentIndex == l:
            raise PredictionImpossible('User current Index and Prediction invalid due to tree - End Index')

        