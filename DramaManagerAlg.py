import os
from numpy import mean
from surprise import (BaselineOnly, Dataset, AlgoBase, Reader,
                      PredictionImpossible)
from surprise.model_selection import cross_validate


class DramaManagerAlg(AlgoBase):
    """
    My :mod: `DramaManagerAlg <Missing.DramaManagerAlg>`

    .. autosummary ..
        :no signatures:

        Predict (Takes in u in current i and data)


    """
    def __init__(self, sim_options={'name': 'cosine', 'u_based': True}):
        AlgoBase.__init__(self, sim_options=sim_options)

        # Build an algorithm, and train it.

    def fit(self, trainset):
        AlgoBase.fit(self, trainset)

        # Compute similarites and baseline
        self.bu, self.bi = self.compute_baselines()
        self.sim = self.compute_similarities()
        self.the_mean = mean([r for (_, _, r) in self.trainset.all_ratings()])
        return self

    def estimate(self, u, i):
        # This is an internal suprise function, you can't use your
        # own classes as input or for raising prediction impossible

        # Catch Impossible predictions
        if not (self.trainset.knows_user(u) and self.trainset.knows_item(i)):
            raise PredictionImpossible('u and or Item are unknown')

        neighbours = [(v, self.sim[u, v]) for (v, r) in self.trainset.ir[i]]
        neighbours = sorted(neighbours, key=lambda x: x[1], reverse=True)

        # print('The 3 nearest neighbours of user', str(u), 'are:')
        # for v, sim_uv in neighbours[:3]:
        #     print('user {0:} with sim {1:1.2f}'.format(v, sim_uv))
        # Mean
        prediction = sum(sim_uv
                         for v, sim_uv in neighbours[:3]) / len(neighbours)
        return prediction


def train_algorithms():
    """
    train one algorithm for each rating and return an array with each one.
    Algorithms in the array in the same order as the ratings
    """
    algorithms = list()
    for r in range(1, 10):
        # For each rating
        reader = Reader(line_format='item user rating',
                        sep=',',
                        rating_scale=(-30, 30))
        data = Dataset.load_from_file('./data/data_rating{}.csv'.format(r),
                                      reader=reader)
        # Initialise custom algorithm
        algo = DramaManagerAlg()
        # Run algorithm
        cross_validate(algo, data)
        algorithms.append(algo)
    return algorithms


def main():
    train_algorithms()


if __name__ == "__main__":
    main()
