from utils.distances import calculate_point_distances, are_same_point
from utils.point import Point
from geopy.distance import geodesic
import pandas as pd
import numpy as np


def df_to_trajectories(df: pd.DataFrame) -> list:
    # Ordenamos el dataFrame por 'ECTRL ID' y 'Sequence Number'
    df = df.sort_values(by=['ECTRL ID', 'Sequence Number'])
    # Creamos una lista vacía para almacenar las trayectorias
    trajectories = []
    # Obtenemos los ids únicos de las trayectorias
    trajectory_ids = df['ECTRL ID'].unique()
    # Para cada id de trayectoria
    for trajectory_id in trajectory_ids:
        # Filtramos los puntos de la trayectoria actual
        trajectory_df = df[df['ECTRL ID'] == trajectory_id]
        # Ordenamos por el número de secuencia
        trajectory_df = trajectory_df.sort_values(by='Sequence Number')
        # Convertimos  y las agregamos a la lista de trayectorias
        # trajectories.append(trajectory_df[['Latitude', 'Longitude']].values)
        trajectories.append(trajectory_df.apply(lambda row: Point(row['Latitude'], row['Longitude'], row['ECTRL ID'], row['Sequence Number'], row['Flight Level']), axis=1).tolist())

    return trajectories

def interpolate_trajectory(trajectory, num_points):
    # Calcular las distancias acumuladas a lo largo de la trayectoria
    distances = [0]
    for i in range(1, len(trajectory)):
        prev_point = trajectory[i-1]
        curr_point = trajectory[i]
        dist = geodesic(curr_point.coords, prev_point.coords).meters
        distances.append(distances[-1] + dist)
    
    # Interpolar nuevos puntos
    new_distances = np.linspace(0, distances[-1], num_points)
    new_points = []
    for j, d in enumerate(new_distances):
        i = np.searchsorted(distances, d)
        if i == 0:
            new_coords = trajectory[0].coords
            new_flight_level = trajectory[0].flight_level
            new_ectrl_id = trajectory[0].ectrl_id
            new_sequence_number = j + 1
        elif i == len(trajectory):
            new_coords = trajectory[-1].coords
            new_flight_level = trajectory[-1].flight_level
            new_ectrl_id = trajectory[-1].ectrl_id
            new_sequence_number = j + 1
        else:
            # Interpolación lineal de las coordenadas y el flight level
            p1 = trajectory[i-1]
            p2 = trajectory[i]
            d1 = distances[i-1]
            d2 = distances[i]
            f = (d - d1) / (d2 - d1)
            lat = p1.coords[0] + f * (p2.coords[0] - p1.coords[0])
            lon = p1.coords[1] + f * (p2.coords[1] - p1.coords[1])
            new_coords = (lat, lon)
            new_flight_level = p1.flight_level + f * (p2.flight_level - p1.flight_level)
            new_ectrl_id = p1.ectrl_id
            new_sequence_number = j + 1
        
        # Crear un nuevo punto con las coordenadas y el flight level interpolados
        new_point = Point(new_coords[0], new_coords[1], new_ectrl_id, new_sequence_number, new_flight_level)
        new_points.append(new_point)
    
    return new_points


def normalize_segments(trajectory):
    """
    Normalize las distancias entre segmentos de una trayectoria para que la suma total de las distancias con respecto al origen sea igual a 1.
    """
    distances = calculate_point_distances(trajectory);
    total_distance = sum(distances)

    distances.reverse()
    
    normalized_distances = [1]
    for distance in distances:
        normalized_distances.append(normalized_distances[-1] - (distance / total_distance))

    normalized_distances.reverse()
    return normalized_distances

def remove_taxi(trajectory_point):
    """
    Taxi period points have same coordenates but different timestamps.
    This function removes those extra points.
    """
    unique_points = [trajectory_point[1]];
    for trajectory_point in trajectory_point[1:]:
        if (not are_same_point(trajectory_point.coords, unique_points[-1].coords)):
            unique_points.append(trajectory_point)

    return unique_points

def remove_under_FL195(trajectory):
    """
    Removes points under flight level 195 (FL195), which represents a typical
    boundary between the lower and the upper airspace
    """
    points_over_195 = [];
    for trajectory_point in trajectory:
        if trajectory_point.flight_level > 195:
            points_over_195.append(trajectory_point)

    return points_over_195


