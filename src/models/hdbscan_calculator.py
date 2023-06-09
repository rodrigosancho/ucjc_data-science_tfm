from sklearn.metrics import silhouette_score, davies_bouldin_score
from itertools import product
import numpy as np
import hdbscan
from sklearn.base import BaseEstimator, TransformerMixin

"""
Lo ideal es obtener el mayor coef. de silueta con el menor ruido posible. 
Segun Andrew Churchill and Michael Bloem, Hierarchical clustering of aircraft 
surface trajectories, AIAA AVIATION 2020 FORUM., los niveles de ruido no 
deberían superar el 20% y como mínimo, el nivel coef de silueta no debería bajar
de 50%
"""

def SearchHDBSCAN(distances, params, method = 'silhouette'):
    if isinstance(params["min_samples"], list) and len(params["min_samples"]) > 0:
      raise ValueError('params["min_samples"] must be defined, must be a list and must have any value')
    
    if isinstance(params["min_cluster_size"], list) and len(params["min_cluster_size"]) > 0:
      raise ValueError('params["min_cluster_size"] must be defined, must be a list and must have any value')
    
    results = []

    for min_samples, min_cluster_size in product(params["min_samples"], params["min_cluster_size"]):
      # Ajusta el modelo HDBSCAN utilizando la matriz de distancias
      clusterer = hdbscan.HDBSCAN(metric='precomputed', min_samples=min_samples, min_cluster_size = min_cluster_size)
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
          "min_samples": min_samples, 
          "min_cluster_size": min_cluster_size 
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


class HDBSCANCalculator(BaseEstimator, TransformerMixin):
    def __init__(self, method, distance_fn):
        self.method = method
        self.distance_fn = distance_fn
    
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        search = SearchHDBSCAN(X['distances_'], params = {
            "min_samples": np.arange(1, 16),
            "min_cluster_size": np.array([2, 5, 10, 20, 40, 60, 80, 100, 120, 140])
        }, method=self.method)

        params = search["best_estimator_"]["params"]
        clusterer = hdbscan.HDBSCAN(metric='precomputed', 
                                    min_samples=params["min_samples"], 
                                    min_cluster_size =params["min_cluster_size"])
        clusterer.fit(X['distances_'])

        return {
          'algorithm_': 'hdbscan',
          'labels_': clusterer.labels_,
          'search_': search,
          'validation_method_': self.method,
          'distance_fn_': self.distance_fn,
          'distances_': X['distances_']
        }