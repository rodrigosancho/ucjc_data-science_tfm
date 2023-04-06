import os
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class DataLoader(BaseEstimator, TransformerMixin):
    def __init__(self, flights_path, flights_points_path):
        self.flights_path = flights_path
        self.flights_points_path = flights_points_path

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        flights = []
        for root, dirs, files in os.walk(self.flights_path, topdown=False):
            for name in files:
                filepath = f'{root}/{name}'
                dataset = pd.read_csv(filepath, compression='gzip')
                flights.append(dataset)
        flights = pd.concat(flights)

        flight_points = []
        for root, dirs, files in os.walk(self.flights_points_path, topdown=False):
            for name in files:
                filepath = f'{root}/{name}'
                dataset = pd.read_csv(filepath, compression='gzip')
                flight_points.append(dataset)
        flight_points = pd.concat(flight_points)

        return {'flights': flights, 'flight_points': flight_points}