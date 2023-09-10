import os
import seaborn as sns
import numpy as np
from scipy.interpolate import interp1d
from utils.trajectories import normalize_segments
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import LineString
import cartopy.crs as ccrs
import cartopy.feature as cfeature


CODES = {
  (40.47222, -3.56083): 'MAD', # Madrid
  (43.30111, -2.91056): 'BIO', # Bilbao
  (41.29695, 2.07833): 'BCN', # Barcelona
  (43.30195, -8.37722): 'LCG', # A Coruña
  (36.74472, -6.06): 'XRY', # Jerez
  (43.56361, -6.03472): 'OVD', # Asturias
  (37.18861, -3.77722): 'GRX' # Granada
}


def ensure_saving_path(path):
  directory, file_name = os.path.split(path)

  if not os.path.exists(directory):
      os.makedirs(directory)


def interpolate_altitudes (trajectory, max_length):
  flight_levels = [point.flight_level for point in trajectory]
  x = np.arange(len(flight_levels))
  f = interp1d(x, flight_levels)
  xnew = np.linspace(0, len(flight_levels)-1, max_length)
  return f(xnew)

def accumulated_distance(trajectories, ax):
  # Calculamos la distancia de cada punto al origen de su respectiva trayectoria
  distances = [distance for trajectory in trajectories for distance in normalize_segments(trajectory)]

  # Creamos el histograma
  sns.histplot(distances, bins=15, ax=ax)
  ax.set_xlabel('Distance from the origin')
  ax.set_ylabel('Number of points')

def altitude_profile(trajectories, ax):
  # Determinar la longitud máxima de las trayectorias
  max_length = max(len(trajectory) for trajectory in trajectories)

  for trajectory in trajectories:
      flight_levels_interp = interpolate_altitudes(trajectory, max_length)
      sns.lineplot(data=flight_levels_interp, 
                   color='red', 
                   alpha=0.3, 
                   linewidth=0.5, 
                   ax=ax)

  ax.set(xticklabels=[])
  ax.set_ylabel('Flight Level')

def pad_number(number):
  length = 6
  fill_char = ' '
  return str(number).rjust(length - len(str(number)), fill_char)   

def show_outliers_map(trajectories, labels, save_as, outliers):
  total = len(trajectories)
  ax = plt.axes(projection=ccrs.PlateCarree())
  ax.patch.set_facecolor('white')

  plt.setp(ax.spines.values(), color='white')
  plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='white')

  ax.add_feature(cfeature.LAND.with_scale('50m'), facecolor=cfeature.COLORS['land'])
  ax.add_feature(cfeature.OCEAN.with_scale('50m'), facecolor=cfeature.COLORS['water'])
  ax.add_feature(cfeature.BORDERS.with_scale('50m'), linewidth=0.5)
  ax.set_extent([-10, 5, 35, 45], crs=ccrs.PlateCarree())

  annotated = {}
  for trajectory in trajectories:
      if tuple(trajectory[0]) not in annotated:
          coords = (trajectory[0][1], trajectory[0][0])
          ax.annotate(CODES[tuple(trajectory[0])], xy=coords, xytext=(5,-5), textcoords='offset points', fontsize=5, bbox=dict(facecolor='white', alpha=0.5))
          annotated[tuple(trajectory[0])] = True
      if tuple(trajectory[-1]) not in annotated:
          coords = (trajectory[-1][1], trajectory[-1][0])
          ax.annotate(CODES[tuple(trajectory[-1])], xy=coords, xytext=(5,-5), textcoords='offset points', fontsize=5, bbox=dict(facecolor='white', alpha=0.5))
          annotated[tuple(trajectory[-1])] = True

  geometry = [LineString([(point[1], point[0]) for point in trajectory]) for trajectory in trajectories]
  data = {'label': labels, 'geometry': geometry}
  routes = gpd.GeoDataFrame(data, crs='EPSG:4326')

  routes['color'] = 'blue'
  routes.loc[labels == -1, 'color'] = 'red'
  
  routes['alpha'] = 0.3
  routes.loc[labels == -1, 'alpha'] = 1

  routes.plot(ax=ax, transform=ccrs.Geodetic(), color=routes['color'], linewidth=0.2, alpha=routes['alpha'])
  
  ensure_saving_path(save_as)

  plt.annotate('Vuelos totales: {}\nVuelos anómalos: {}'.format(pad_number(total), pad_number(outliers)), 
               xy=(1.0, 0.0), xycoords='axes fraction', fontsize=10, 
               xytext=(-5, 5), textcoords='offset points', ha='right', va='bottom', 
               bbox=dict(boxstyle='square', fc='white', ec='white'))
  plt.savefig(save_as, dpi=600, bbox_inches='tight')
  plt.close()

def show_flights_map(trajectories, save_as):
  ax = plt.axes(projection=ccrs.PlateCarree())
  ax.patch.set_facecolor('white')

  plt.setp(ax.spines.values(), color='white')
  plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='white')

  ax.add_feature(cfeature.LAND.with_scale('50m'), facecolor=cfeature.COLORS['land'])
  ax.add_feature(cfeature.OCEAN.with_scale('50m'), facecolor=cfeature.COLORS['water'])
  ax.add_feature(cfeature.BORDERS.with_scale('50m'), linewidth=0.5)
  ax.set_extent([-10, 5, 35, 45], crs=ccrs.PlateCarree())

  annotated = {}
  for trajectory in trajectories:
      if tuple(trajectory[0]) not in annotated:
          coords = (trajectory[0][1], trajectory[0][0])
          ax.annotate(CODES[tuple(trajectory[0])], xy=coords, xytext=(5,-5), textcoords='offset points', fontsize=6, bbox=dict(facecolor='white', alpha=0.5))
          annotated[tuple(trajectory[0])] = True
      if tuple(trajectory[-1]) not in annotated:
          coords = (trajectory[-1][1], trajectory[-1][0])
          ax.annotate(CODES[tuple(trajectory[-1])], xy=coords, xytext=(5,-5), textcoords='offset points', fontsize=6, bbox=dict(facecolor='white', alpha=0.5))
          annotated[tuple(trajectory[-1])] = True

  geometry = [LineString([(point[1], point[0]) for point in trajectory]) for trajectory in trajectories]
  data = {'geometry': geometry}
  routes = gpd.GeoDataFrame(data, crs='EPSG:4326')

  routes['color'] = 'blue'
  routes['alpha'] = 0.3

  routes.plot(ax=ax, transform=ccrs.Geodetic(), color=routes['color'], linewidth=0.2, alpha=routes['alpha'])
  
  ensure_saving_path(save_as)

  plt.savefig(save_as, dpi=600, bbox_inches='tight')
  plt.close()


def show_elbow_plot(curve, elbow_index, save_as):
  elbow_val = curve[elbow_index]

  fig, (ax1, ax2) = plt.subplots(1, 2)

  ax1.plot(curve)
  ax1.set_title('KNN')
  plt.subplots_adjust(wspace=0.5)


  ax2.plot(curve)
  ax2.plot(elbow_index, elbow_val, 'ro')

  ax2.axhline(y=elbow_val, color='r', linestyle='--')
  ax2.axvline(x=elbow_index, color='r', linestyle='--')

  ax2.set_xticks([elbow_index])
  ax2.set_yticks([elbow_val])

  ax2.set_title('KNN zoom')

  x_gap = elbow_index * 0.2
  y_gap = (curve[-1] - curve[0]) * 0.2
  
  x_start = max(elbow_index - x_gap, 0)
  x_end = elbow_index + x_gap 
  y_start = max(elbow_val - y_gap, 0)
  y_end =elbow_val + y_gap

  ax2.axis([x_start,x_end,y_start,y_end])

  plt.savefig(save_as, dpi=600, bbox_inches='tight')
  plt.close()
   