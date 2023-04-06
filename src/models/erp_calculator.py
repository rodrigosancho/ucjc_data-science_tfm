from sklearn.base import BaseEstimator, TransformerMixin
import traj_dist.distance as tdist
import numpy as np

class ERPCalculator(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        trajectories = X['trajectories']
        g = np.zeros(trajectories[0].shape[1], dtype=float)

        sspd_distances = np.zeros((len(trajectories), len(trajectories)))
        for i in range(len(trajectories)):
            for j in range(i+1, len(trajectories)):
                d = tdist.erp(trajectories[i], trajectories[j], type_d = "spherical", g=g)
                sspd_distances[i,j] = d
                sspd_distances[j,i] = d

        return {'erp_distances': sspd_distances }