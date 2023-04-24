from sklearn.base import BaseEstimator, TransformerMixin
from utils.trajectories import df_to_trajectories, remove_taxi, interpolate_trajectory
import numpy as np

class TrajectoryCalculator(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        flight_points = X['flight_points']

        trajectories = df_to_trajectories(flight_points)
      
        return {'trajectories': trajectories}

class NormalizedTrajectoryCalculator(BaseEstimator, TransformerMixin):
    def __init__(self, clean_taxi = True):
        self.clean_taxi = clean_taxi
    
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        flight_points = X['flight_points']

        trajectories = df_to_trajectories(flight_points)
        trajectories = [remove_taxi(trajectory) if self.clean_taxi else trajectory for trajectory in trajectories]
        points_num = max([len(trajectory) for trajectory in trajectories])
        trajectories = [interpolate_trajectory(trajectory, points_num) for trajectory in trajectories]
        trajectories = [np.array([point.coords for point in trajectory]) for trajectory in trajectories]
      
        return {'trajectories': trajectories}
