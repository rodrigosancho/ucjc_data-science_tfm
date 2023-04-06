import math
from geopy.distance import geodesic

def calculate_total_distance(trajectory):
    """
    Calculate the total distance traveled along a trajectory.

    :param trajectory: A list of tuples representing points in geographic space in terms of latitude and longitude.
    :return: The total distance traveled along the trajectory in meters.
    """  
    total_distance = 0
    for i in range(len(trajectory) - 1):
        current_point = trajectory[i]
        next_point = trajectory[i + 1]
        # Calculate the geodesic distance between the two points in meters
        distance = geodesic(current_point.coords, next_point.coords).meters
        total_distance += distance
    return total_distance

def calculate_point_distances(trajectory):
    """
    Calculate the distances between consecutive points along a trajectory.

    :param trajectory: A list of tuples representing points in geographic space in terms of latitude and longitude.
    :return: A list of distances between consecutive points along the trajectory in meters.
    """
    point_distances = []
    for i in range(len(trajectory) - 1):
        current_point = trajectory[i]
        next_point = trajectory[i + 1]
        # Calculate the geodesic distance between the two points in meters
        distance = geodesic(current_point.coords, next_point.coords).meters
        point_distances.append(distance)
    return point_distances


def distance_between_points(p1, p2):
    """
    Calculate the euclidean distance between two points.

    :param p1: A tuples representing point.
    :param p2: A tuples representing point.
    :return: A list of distances between consecutive points along the trajectory in meters.
    """
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def are_same_point(p1, p2):
    """
    :param p1: A tuples representing point.
    :param p2: A tuples representing point.
    :return: Whether a couple of points are the same.
    """
    x1, y1 = p1
    x2, y2 = p2
    return x1 == x2 and y1 == y2
