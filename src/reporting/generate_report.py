from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
from utils.markdown import  generate_title_markdown, generate_image_markdown, generate_paragraph_markdown, generate_results_table_markdown, generate_separation_markdown

def setValue(keys, value, dic):
    current_dict = dic
    for key in keys[:-1]:
        current_dict = current_dict.setdefault(key, {})
    current_dict[keys[-1]] = value


class GenerateReport(BaseEstimator, TransformerMixin):
    def __init__(self, report_path):
        self.report_path = report_path

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        data = X['data']
        models = X['models']
        
        content = []
        data = {}
        best_scores = {
            'silhouette': [],
            'davies_bouldin': []
        }

        dbscan__sspd__silhouette, dbscan__sspd__davies_bouldin, dbscan__erp__silhouette, dbscan__erp__davies_bouldin, hdbscan__sspd__silhouette, hdbscan__sspd__davies_bouldin, hdbscan__erp__silhouette, hdbscan__erp__davies_bouldin = models

        for model in [dbscan__sspd__silhouette, dbscan__sspd__davies_bouldin, dbscan__erp__silhouette, dbscan__erp__davies_bouldin, hdbscan__sspd__silhouette, hdbscan__sspd__davies_bouldin, hdbscan__erp__silhouette, hdbscan__erp__davies_bouldin]:
            keys = [model['algorithm_'], model['distance_fn_'], model['validation_method_']]
            results = model['search_']

            setValue(keys, results, data)
        
        for algorithm, value in data.items():
            for distance_fn, value in value.items():
                for validation_method, value in value.items():
                    best_scores[validation_method].append({
                        'clusters': value['best_estimator_']['clusters'],
                        'outliers': value['best_estimator_']['outliers'],
                        'noise': value['best_estimator_']['noise'],
                        'score': value['best_estimator_']['score'],
                        'algorithm': algorithm,
                        'distance_fn': distance_fn
                    })


        results = pd.DataFrame(best_scores['silhouette']).sort_values(by='score', ascending=False)
        content.append(generate_title_markdown('Resume'))
        content.append(generate_title_markdown('Silhouette', 2))
        content.append(generate_paragraph_markdown('Best algorithm/function distance configuration based on silhouette score.'))
        content.append(generate_results_table_markdown(results))
        content.append(generate_paragraph_markdown('Score represents the quality of the clustering. The best score is 1.0 and the worst score is -1.0. Scores around zero indicate overlapping clusters.'))
        
        results = pd.DataFrame(best_scores['davies_bouldin']).sort_values(by='score', ascending=False)
        content.append(generate_title_markdown('Resume'))
        content.append(generate_title_markdown('Davies-Bouldin', 2))
        content.append(generate_paragraph_markdown('Best algorithm/function distance configuration based on davies_bouldin score.'))
        content.append(generate_results_table_markdown(results))
        content.append(generate_paragraph_markdown('The minimum score is zero, with lower values indicating better clustering.'))
        
        content.append(generate_separation_markdown())

        for algorithm, value in data.items():
            content.append(generate_title_markdown(algorithm))

            for distance_fn, value in value.items():
                content.append(generate_title_markdown(distance_fn, 2))

                for validation_method, value in value.items():
                    reports_graphs_path = f'{algorithm}/{distance_fn}/{validation_method}'

                    content.append(generate_title_markdown(validation_method, 3))
                    
                    if(algorithm == 'dbscan'):
                      content.append(generate_title_markdown('Optimal epsilon visual representation', 4))
                      content.append(generate_image_markdown(f'{reports_graphs_path}/elbow.png'))

                    content.append(generate_title_markdown('Search params result', 4))
                    content.append(generate_results_table_markdown(value['results_']))

                    content.append(generate_title_markdown('Best estimator result', 4))
                    content.append(generate_results_table_markdown([value['best_estimator_']]))
                    content.append(generate_image_markdown(f'{reports_graphs_path}/outliers.png'))
            
        with open(f'{self.report_path}/report.md', 'w') as f:
          f.write(''.join(content))

        return X