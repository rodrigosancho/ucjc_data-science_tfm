from sklearn.base import BaseEstimator, TransformerMixin

class FlightFilter(BaseEstimator, TransformerMixin):
    def __init__(self, departure, destinations):
        self.departure = departure
        self.destinations = destinations

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        flights = X['flights']
        flight_points = X['flight_points']

        # Filter -  Vuelos entre Madrid y Barcelona
        flights = flights[(flights['ADEP'] == self.departure) & (flights['ADES'].isin(self.destinations))]

        # Filter - Puntos que pertenezcan a alguno de los vuelos guardados arriba
        flight_points = flight_points[flight_points['ECTRL ID'].isin(flights['ECTRL ID'])]

        return {'flights': flights, 'flight_points': flight_points}