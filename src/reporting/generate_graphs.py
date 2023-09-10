from utils.graphs import show_outliers_map, show_flights_map, show_elbow_plot
from sklearn.base import BaseEstimator, TransformerMixin
from src.features.epsilon_calculator import EpsilonCalculator

class GenerateGraphs(BaseEstimator, TransformerMixin):
    def __init__(self, report_path):
        self.report_path = report_path

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        data = X['data']
        models = X['models']
        trajectories = data['trajectories']

        show_flights_map(trajectories, f'{self.report_path}/flights.png') 
        
        dbscan__sspd__silhouette, dbscan__sspd__davies_bouldin, dbscan__erp__silhouette, dbscan__erp__davies_bouldin, hdbscan__sspd__silhouette, hdbscan__sspd__davies_bouldin, hdbscan__erp__silhouette, hdbscan__erp__davies_bouldin = models

        for model in [dbscan__sspd__silhouette, dbscan__sspd__davies_bouldin, dbscan__erp__silhouette, dbscan__erp__davies_bouldin, hdbscan__sspd__silhouette, hdbscan__sspd__davies_bouldin, hdbscan__erp__silhouette, hdbscan__erp__davies_bouldin]:
            labels = model['labels_']
            algorithm_ = model['algorithm_']
            validation_method_ = model['validation_method_']
            distance_fn_ = model['distance_fn_']
            labels = model['labels_']
            graphs_path = f'{self.report_path}/{algorithm_}/{distance_fn_}/{validation_method_}'
            outliers = model['search_']['best_estimator_']['outliers']

            show_outliers_map(trajectories, labels, f'{graphs_path}/outliers.png', outliers) 

            if(algorithm_ == 'dbscan'):
              calculator = EpsilonCalculator()
              result = calculator.transform(model)

              eps_curve = result['eps_curve_']
              eps_index = result['eps_index_']

              show_elbow_plot(eps_curve, eps_index, f'{graphs_path}/elbow.png')
        
        return X