from sklearn.neighbors import NearestNeighbors
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class EpsilonCalculator(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        result = X.copy()

        neighbors = NearestNeighbors(n_neighbors=6, metric='precomputed')
        neighbors_fit = neighbors.fit(X['distances_'])
        points, indices = neighbors_fit.kneighbors(X['distances_'])

        curve = np.sort(points, axis=0)
        curve = curve[:,1]

        line = np.linspace(curve[0], curve[-1], len(curve))
        distances_to_line = np.abs(curve - line)
        elbow_index = np.argmax(distances_to_line)
        
        result['eps'] = curve[elbow_index]
        result['eps_index_'] = elbow_index
        result['eps_curve_'] = curve

        return result