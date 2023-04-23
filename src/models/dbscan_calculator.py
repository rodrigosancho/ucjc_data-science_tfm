from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.cluster import DBSCAN
from itertools import product
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

"""
Lo ideal es obtener el mayor coef. de silueta con el menor ruido posible. 
Segun Andrew Churchill and Michael Bloem, Hierarchical clustering of aircraft 
surface trajectories, AIAA AVIATION 2020 FORUM., los niveles de ruido no 
deberían superar el 20% y como mínimo, el nivel coef de silueta no debería bajar
de 50%
"""

def SearchDBSCAN(distances, params, method = 'silhouette'):
    if isinstance(params["eps"], list) and len(params["eps"]) > 0:
      raise ValueError('params["eps"] must be defined, must be a list and must have any value')
    
    if isinstance(params["min_samples"], list) and len(params["min_samples"]) > 0:
      raise ValueError('params["min_samples"] must be defined, must be a list and must have any value')
    
    results = []

    for eps, min_samples in product(params["eps"], params["min_samples"]):
      clusterer = DBSCAN(metric='precomputed', eps=eps, min_samples = min_samples)
      clusterer.fit(distances)

      # Obtiene las etiquetas de los clusters para cada trayectoria
      labels = clusterer.labels_

      score = 0
      if(method == 'davies_bouldin'):
        score = davies_bouldin_score(distances, labels)
      else:
        score = silhouette_score(distances, labels)
        method = 'silhouette'

      n_outliers = np.sum(labels == -1)
      results.append({
        "params": {
          "eps": eps, 
          "min_samples": min_samples 
        },
        "clusters": len(set(labels)),
        "outliers": n_outliers,
        "noise": 100 * n_outliers / len(labels),
        "method": method,
        "score": score,
      })

    results_ = sorted(results, key=lambda x: x["score"], reverse=method == 'silhouette')
    best_estimator_ = results_[0]

    return {
      "results_": results_,
      "best_estimator_": best_estimator_
    }
  
class DBSCANCalculator(BaseEstimator, TransformerMixin):
    def __init__(self, method, distance_fn):
        self.method = method
        self.distance_fn = distance_fn

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        search = SearchDBSCAN(X['distances_'], params = {
          "eps": np.array([X['eps']]),
          "min_samples": np.arange(2, 16)
        }, method=self.method)

        params = search["best_estimator_"]["params"]
        clusterer = DBSCAN(metric='precomputed', 
                          min_samples=params["min_samples"], 
                          eps=params["eps"])
        clusterer.fit(X['distances_'])
        
        return {
          'algorithm_': 'dbscan',
          'labels_': clusterer.labels_,
          'search_': search,
          'validation_method_': self.method,
          'distance_fn_': self.distance_fn,
          'distances_': X['distances_']
        }
