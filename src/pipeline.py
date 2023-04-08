from sklearn.pipeline import FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

from src.features.trajectory_calculator import NormalizedTrajectoryCalculator
from src.models.sspd_calculator import SSPDCalculator
from src.models.erp_calculator import ERPCalculator
from src.preprocesing.data_loader import DataLoader
from src.preprocesing.flight_filter import FlightFilter

class Identity(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return X
    
def build_pipeline(flights_path, flights_points_path, departure, destinations):
    return Pipeline([
        ('data_loader', DataLoader(flights_path, flights_points_path)),
        ('flight_filter', FlightFilter(departure, destinations)),
        ('trajectory_calculator', NormalizedTrajectoryCalculator()),
        ('distances_matrix', FeatureUnion([
            ('trajectories_result', Identity()),
            ('sspd_calculator', SSPDCalculator()),
            ('erp_calculator', ERPCalculator()),
        ], n_jobs = -1))
    ])