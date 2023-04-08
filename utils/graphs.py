import seaborn as sns
import numpy as np
from scipy.interpolate import interp1d
from utils.trajectories import normalize_segments
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import LineString
import cartopy.crs as ccrs
import cartopy.feature as cfeature

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

def show_outliers_map(trajectories, labels, save_as):
  ax = plt.axes(projection=ccrs.PlateCarree())
  ax.patch.set_facecolor('white')

  plt.setp(ax.spines.values(), color='white')
  plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='white')

  ax.add_feature(cfeature.LAND.with_scale('50m'), facecolor=cfeature.COLORS['land'])
  ax.add_feature(cfeature.OCEAN.with_scale('50m'), facecolor=cfeature.COLORS['water'])
  ax.add_feature(cfeature.BORDERS.with_scale('50m'), linewidth=0.5)
  ax.set_extent([-10, 5, 35, 45], crs=ccrs.PlateCarree())

  geometry = [LineString([(point[1], point[0]) for point in trajectory]) for trajectory in trajectories]
  data = {'label': labels, 'geometry': geometry}
  routes = gpd.GeoDataFrame(data, crs='EPSG:4326')

  routes['color'] = 'blue'
  routes.loc[labels == -1, 'color'] = 'red'
  
  routes['alpha'] = 0.3
  routes.loc[labels == -1, 'alpha'] = 1

  routes.plot(ax=ax, transform=ccrs.Geodetic(), color=routes['color'], linewidth=0.2, alpha=routes['alpha'])
  plt.savefig(save_as, dpi=600)
  plt.show()


