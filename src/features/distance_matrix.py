from sklearn.base import BaseEstimator, TransformerMixin

class DistanceMatrix(BaseEstimator, TransformerMixin):
    def __init__(self, distance_fn):
        self.distance_fn = distance_fn

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        sspd_calculator, erp_calculator = X

        if self.distance_fn == 'sspd_distances':
          return { 'distances_': sspd_calculator['sspd_distances'] }
        else:
          return { 'distances_': erp_calculator['erp_distances'] }