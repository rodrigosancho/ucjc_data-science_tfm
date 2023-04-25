from sklearn.pipeline import FeatureUnion
from sklearn.pipeline import Pipeline

from src.features.trajectory_calculator import NormalizedTrajectoryCalculator, TrajectoryCalculator
from src.features.epsilon_calculator import EpsilonCalculator
from src.features.distance_matrix import DistanceMatrix
from src.models.sspd_calculator import SSPDCalculator
from src.models.erp_calculator import ERPCalculator
from src.models.dbscan_calculator import DBSCANCalculator
from src.models.hdbscan_calculator import HDBSCANCalculator
from src.preprocesing.data_loader import DataLoader
from src.preprocesing.flight_filter import FlightFilter
from src.reporting.generate_graphs import GenerateGraphs
from src.reporting.generate_report import GenerateReport
    
    
def build_dbscan_pipeline(distance_fn, validation_method):
  return Pipeline([
      ('pick_distance', DistanceMatrix(distance_fn)),
      ('add_epsilon', EpsilonCalculator()),
      ('dbscan_model', DBSCANCalculator(validation_method, distance_fn))
  ])

def build_hdbscan_pipeline(distance_fn, validation_method):
  return Pipeline([
      ('pick_distance', DistanceMatrix(distance_fn)),
      ('hdbscan_model', HDBSCANCalculator(validation_method, distance_fn)),
  ])

def build_data_pipeline(flights_path, flights_points_path, departure, destinations, clean_taxi):
   return Pipeline([
      ('data_loader', DataLoader(flights_path, flights_points_path)),
      ('flight_filter', FlightFilter(departure, destinations)),
      ('trajectory_calculator', NormalizedTrajectoryCalculator(clean_taxi))
   ])
    
def build_models_pipeline():
    return Pipeline([
        ('distances_matrix', FeatureUnion([
            ('sspd_calculator', SSPDCalculator()),
            ('erp_calculator', ERPCalculator())
        ], n_jobs = -1)),
        ('model_training', FeatureUnion([
          ('dbscan__sspd__silhouette', build_dbscan_pipeline('sspd_distances', 'silhouette')),
          ('dbscan__sspd__davies_bouldin', build_dbscan_pipeline('sspd_distances', 'davies_bouldin')),
          ('dbscan__erp__silhouette', build_dbscan_pipeline('erp_distances', 'silhouette')),
          ('dbscan__erp__davies_bouldin', build_dbscan_pipeline('erp_distances', 'davies_bouldin')),
          ('hdbscan__sspd__silhouette', build_hdbscan_pipeline('sspd_distances', 'silhouette')),
          ('hdbscan__sspd__davies_bouldin', build_hdbscan_pipeline('sspd_distances', 'davies_bouldin')),
          ('hdbscan__erp__silhouette', build_hdbscan_pipeline('erp_distances', 'silhouette')),
          ('hdbscan__erp__davies_bouldin', build_hdbscan_pipeline('erp_distances', 'davies_bouldin')),
        ], n_jobs = -1))
    ])

def build_reporting_pipeline(report_path, report_data):
    return Pipeline([
        ('generate_graphs', GenerateGraphs(report_path)),
        ('generate_report', GenerateReport(report_path, report_data))
    ])