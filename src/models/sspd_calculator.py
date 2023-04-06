from sklearn.base import BaseEstimator, TransformerMixin
import traj_dist.distance as tdist
import numpy as np

class SSPDCalculator(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        trajectories = X['trajectories']

        sspd_distances = np.zeros((len(trajectories), len(trajectories)))
        for i in range(len(trajectories)):
            for j in range(i+1, len(trajectories)):
                d = tdist.sspd(trajectories[i], trajectories[j])
                sspd_distances[i,j] = d
                sspd_distances[j,i] = d

        return {'sspd_distances': sspd_distances }