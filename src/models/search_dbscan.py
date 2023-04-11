from sklearn.metrics import silhouette_score, davies_bouldin_score
from sklearn.cluster import DBSCAN
from itertools import product
import numpy as np

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