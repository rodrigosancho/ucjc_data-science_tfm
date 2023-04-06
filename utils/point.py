class Point:
    def __init__(self, latitude, longitude, ectrl_id, sequence_number, flight_level):
        self.ectrl_id = ectrl_id
        self.sequence_number = sequence_number
        self.flight_level = flight_level
        self.latitude = latitude
        self.longitude = longitude
        self.coords = (latitude, longitude)