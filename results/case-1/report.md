
# Case 1

Flight from Madrid to Barcelona

## Resume

### Silhouette

Best algorithm/function distance configuration based on silhouette score.

|   clusters |   outliers |   noise |    score | algorithm   | distance_fn    |
|-----------:|-----------:|--------:|---------:|:------------|:---------------|
|          4 |          8 | 1.0568  | 0.923877 | hdbscan     | erp_distances  |
|          4 |         18 | 2.37781 | 0.917562 | hdbscan     | sspd_distances |
|         14 |         48 | 6.34082 | 0.772658 | dbscan      | erp_distances  |
|          9 |         55 | 7.26552 | 0.695729 | dbscan      | sspd_distances |

Score represents the quality of the clustering. The best score is 1.0 and the worst score is -1.0. Scores around zero indicate overlapping clusters.

|               | dbscan  | hdbscan | 
|---------------|:-------:|:-------:|
| erp_distance  | ![](dbscan/erp_distances/silhouette/outliers.png) | ![](hdbscan/sspd_distances/silhouette/outliers.png) |
| sspd_distance | ![](dbscan/erp_distances/silhouette/outliers.png) | ![](hdbscan/sspd_distances/silhouette/outliers.png) |

### Davies-Bouldin

Best algorithm/function distance configuration based on davies_bouldin score.

|   clusters |   outliers |    noise |    score | algorithm   | distance_fn    |
|-----------:|-----------:|---------:|---------:|:------------|:---------------|
|          3 |         13 |  1.71731 | 0.530331 | hdbscan     | sspd_distances |
|          5 |         47 |  6.20872 | 0.61976  | hdbscan     | erp_distances  |
|          9 |         78 | 10.3038  | 0.98805  | dbscan      | erp_distances  |
|          8 |         76 | 10.0396  | 1.13507  | dbscan      | sspd_distances |

The minimum score is zero, with lower values indicating better clustering.

|               | dbscan  | hdbscan | 
|---------------|:-------:|:-------:|
| erp_distance  | ![](dbscan/erp_distances/davies_bouldin/outliers.png) | ![](hdbscan/sspd_distances/davies_bouldin/outliers.png) |
| sspd_distance | ![](dbscan/erp_distances/davies_bouldin/outliers.png) | ![](hdbscan/sspd_distances/davies_bouldin/outliers.png) |

-----------------------

# silhouette

### dbscan

Finding the best eps value.

![](dbscan/erp_distances/silhouette/elbow.png)

In order to calculate the best eps value, first, the nearest neighbors of the data are calculated. Then, the points are sorted and in order to obtain a curve. Next, a line is generated that fits to the curve and the distances between each point of the curve and the line are calculated. The elbow index is the point where the distance is maximum.

As a custom distance function it is used, the distance between trajectories are normalized and epsilon values may not be true magnitudes.

#### sspd_distances

##### Search params result

|   clusters |   outliers |    noise | method     |    score |        eps |   min_samples |
|-----------:|-----------:|---------:|:-----------|---------:|-----------:|--------------:|
|          9 |         55 |  7.26552 | silhouette | 0.695729 | 0.00056864 |             3 |
|          8 |         58 |  7.66182 | silhouette | 0.689371 | 0.00056864 |             4 |
|          9 |         58 |  7.66182 | silhouette | 0.683559 | 0.00056864 |             5 |
|         16 |         41 |  5.41612 | silhouette | 0.682849 | 0.00056864 |             2 |
|          8 |         63 |  8.32232 | silhouette | 0.67807  | 0.00056864 |             6 |
|          9 |         77 | 10.1717  | silhouette | 0.646707 | 0.00056864 |             9 |
|          9 |         78 | 10.3038  | silhouette | 0.644335 | 0.00056864 |            10 |
|          9 |         69 |  9.11493 | silhouette | 0.633774 | 0.00056864 |             7 |
|          7 |        103 | 13.6063  | silhouette | 0.622072 | 0.00056864 |            11 |
|          8 |         76 | 10.0396  | silhouette | 0.621965 | 0.00056864 |             8 |

##### Best estimator result

|   clusters |   outliers |   noise | method     |    score |        eps |   min_samples |
|-----------:|-----------:|--------:|:-----------|---------:|-----------:|--------------:|
|          9 |         55 | 7.26552 | silhouette | 0.695729 | 0.00056864 |             3 |

![](dbscan/sspd_distances/silhouette/outliers.png)

#### erp_distances

##### Search params result

|   clusters |   outliers |    noise | method     |    score |     eps |   min_samples |
|-----------:|-----------:|---------:|:-----------|---------:|--------:|--------------:|
|         14 |         48 |  6.34082 | silhouette | 0.772658 | 4594.31 |             3 |
|         16 |         44 |  5.81242 | silhouette | 0.736918 | 4594.31 |             2 |
|         12 |         62 |  8.19022 | silhouette | 0.733985 | 4594.31 |             4 |
|         10 |         70 |  9.24703 | silhouette | 0.730997 | 4594.31 |             5 |
|         10 |         72 |  9.51123 | silhouette | 0.727956 | 4594.31 |             6 |
|          9 |         78 | 10.3038  | silhouette | 0.718635 | 4594.31 |             7 |
|          4 |        124 | 16.3804  | silhouette | 0.707146 | 4594.31 |            11 |
|          4 |        124 | 16.3804  | silhouette | 0.707146 | 4594.31 |            12 |
|          4 |        124 | 16.3804  | silhouette | 0.707146 | 4594.31 |            13 |
|          4 |        124 | 16.3804  | silhouette | 0.707146 | 4594.31 |            14 |

##### Best estimator result

|   clusters |   outliers |   noise | method     |    score |     eps |   min_samples |
|-----------:|-----------:|--------:|:-----------|---------:|--------:|--------------:|
|         14 |         48 | 6.34082 | silhouette | 0.772658 | 4594.31 |             3 |

![](dbscan/erp_distances/silhouette/outliers.png)

### hdbscan

#### sspd_distances

##### Search params result

|   clusters |   outliers |   noise | method     |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|--------:|:-----------|---------:|--------------:|-------------------:|
|          4 |         18 | 2.37781 | silhouette | 0.917562 |             1 |                100 |
|          4 |         18 | 2.37781 | silhouette | 0.917562 |             2 |                100 |
|          4 |         18 | 2.37781 | silhouette | 0.917562 |             3 |                100 |
|          4 |         18 | 2.37781 | silhouette | 0.917562 |             4 |                100 |
|          4 |         18 | 2.37781 | silhouette | 0.917562 |             5 |                100 |
|          4 |         18 | 2.37781 | silhouette | 0.917562 |             6 |                100 |
|          4 |         18 | 2.37781 | silhouette | 0.917562 |             7 |                100 |
|          4 |         18 | 2.37781 | silhouette | 0.917562 |             8 |                100 |
|          4 |         18 | 2.37781 | silhouette | 0.917562 |             9 |                100 |
|          4 |         18 | 2.37781 | silhouette | 0.917562 |            10 |                100 |

##### Best estimator result

|   clusters |   outliers |   noise | method     |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|--------:|:-----------|---------:|--------------:|-------------------:|
|          4 |         18 | 2.37781 | silhouette | 0.917562 |             1 |                100 |

![](hdbscan/sspd_distances/silhouette/outliers.png)

#### erp_distances

##### Search params result

|   clusters |   outliers |   noise | method     |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|--------:|:-----------|---------:|--------------:|-------------------:|
|          4 |          8 | 1.0568  | silhouette | 0.923877 |             1 |                100 |
|          4 |          8 | 1.0568  | silhouette | 0.923877 |             1 |                120 |
|          4 |          9 | 1.1889  | silhouette | 0.922353 |             2 |                100 |
|          4 |          9 | 1.1889  | silhouette | 0.922353 |             2 |                120 |
|          4 |          9 | 1.1889  | silhouette | 0.922353 |             3 |                100 |
|          4 |          9 | 1.1889  | silhouette | 0.922353 |             3 |                120 |
|          4 |         11 | 1.4531  | silhouette | 0.922324 |             4 |                100 |
|          4 |         11 | 1.4531  | silhouette | 0.922324 |             5 |                100 |
|          4 |         14 | 1.84941 | silhouette | 0.918357 |            11 |                100 |
|          4 |         14 | 1.84941 | silhouette | 0.918357 |            12 |                100 |

##### Best estimator result

|   clusters |   outliers |   noise | method     |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|--------:|:-----------|---------:|--------------:|-------------------:|
|          4 |          8 |  1.0568 | silhouette | 0.923877 |             1 |                100 |

![](hdbscan/erp_distances/silhouette/outliers.png)

# davies_bouldin

### dbscan

Finding the best eps value.

![](dbscan/erp_distances/davies_bouldin/elbow.png)

In order to calculate the best eps value, first, the nearest neighbors of the data are calculated. Then, the points are sorted and in order to obtain a curve. Next, a line is generated that fits to the curve and the distances between each point of the curve and the line are calculated. The elbow index is the point where the distance is maximum.

As a custom distance function it is used, the distance between trajectories are normalized and epsilon values may not be true magnitudes.

#### sspd_distances

##### Search params result

|   clusters |   outliers |    noise | method         |   score |        eps |   min_samples |
|-----------:|-----------:|---------:|:---------------|--------:|-----------:|--------------:|
|          8 |         76 | 10.0396  | davies_bouldin | 1.13507 | 0.00056864 |             8 |
|          9 |         69 |  9.11493 | davies_bouldin | 1.13629 | 0.00056864 |             7 |
|          7 |        105 | 13.8705  | davies_bouldin | 1.18777 | 0.00056864 |            12 |
|          7 |        105 | 13.8705  | davies_bouldin | 1.18777 | 0.00056864 |            13 |
|          7 |        106 | 14.0026  | davies_bouldin | 1.18886 | 0.00056864 |            14 |
|          7 |        106 | 14.0026  | davies_bouldin | 1.18886 | 0.00056864 |            15 |
|          9 |         77 | 10.1717  | davies_bouldin | 1.2084  | 0.00056864 |             9 |
|          9 |         78 | 10.3038  | davies_bouldin | 1.21287 | 0.00056864 |            10 |
|          7 |        103 | 13.6063  | davies_bouldin | 1.2465  | 0.00056864 |            11 |
|         16 |         41 |  5.41612 | davies_bouldin | 1.50683 | 0.00056864 |             2 |

##### Best estimator result

|   clusters |   outliers |   noise | method         |   score |        eps |   min_samples |
|-----------:|-----------:|--------:|:---------------|--------:|-----------:|--------------:|
|          8 |         76 | 10.0396 | davies_bouldin | 1.13507 | 0.00056864 |             8 |

![](dbscan/sspd_distances/davies_bouldin/outliers.png)

#### erp_distances

##### Search params result

|   clusters |   outliers |    noise | method         |    score |     eps |   min_samples |
|-----------:|-----------:|---------:|:---------------|---------:|--------:|--------------:|
|          9 |         78 | 10.3038  | davies_bouldin | 0.98805  | 4594.31 |             7 |
|         16 |         44 |  5.81242 | davies_bouldin | 0.998495 | 4594.31 |             2 |
|         10 |         70 |  9.24703 | davies_bouldin | 1.00773  | 4594.31 |             5 |
|         14 |         48 |  6.34082 | davies_bouldin | 1.02936  | 4594.31 |             3 |
|         10 |         72 |  9.51123 | davies_bouldin | 1.03731  | 4594.31 |             6 |
|         12 |         62 |  8.19022 | davies_bouldin | 1.06494  | 4594.31 |             4 |
|          7 |         95 | 12.5495  | davies_bouldin | 1.14201  | 4594.31 |             8 |
|          6 |        105 | 13.8705  | davies_bouldin | 1.18548  | 4594.31 |             9 |
|          5 |        114 | 15.0594  | davies_bouldin | 1.20688  | 4594.31 |            10 |
|          4 |        124 | 16.3804  | davies_bouldin | 1.42433  | 4594.31 |            11 |

##### Best estimator result

|   clusters |   outliers |   noise | method         |   score |     eps |   min_samples |
|-----------:|-----------:|--------:|:---------------|--------:|--------:|--------------:|
|          9 |         78 | 10.3038 | davies_bouldin | 0.98805 | 4594.31 |             7 |

![](dbscan/erp_distances/davies_bouldin/outliers.png)

### hdbscan

#### sspd_distances

##### Search params result

|   clusters |   outliers |   noise | method         |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|--------:|:---------------|---------:|--------------:|-------------------:|
|          3 |         13 | 1.71731 | davies_bouldin | 0.530331 |             4 |                120 |
|          3 |         13 | 1.71731 | davies_bouldin | 0.530331 |             4 |                140 |
|          3 |         13 | 1.71731 | davies_bouldin | 0.530331 |             5 |                120 |
|          3 |         13 | 1.71731 | davies_bouldin | 0.530331 |             5 |                140 |
|          3 |         13 | 1.71731 | davies_bouldin | 0.530331 |             6 |                120 |
|          3 |         13 | 1.71731 | davies_bouldin | 0.530331 |             6 |                140 |
|          3 |         13 | 1.71731 | davies_bouldin | 0.530331 |             7 |                120 |
|          3 |         13 | 1.71731 | davies_bouldin | 0.530331 |             7 |                140 |
|          3 |         13 | 1.71731 | davies_bouldin | 0.530331 |             8 |                120 |
|          3 |         13 | 1.71731 | davies_bouldin | 0.530331 |             8 |                140 |

##### Best estimator result

|   clusters |   outliers |   noise | method         |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|--------:|:---------------|---------:|--------------:|-------------------:|
|          3 |         13 | 1.71731 | davies_bouldin | 0.530331 |             4 |                120 |

![](hdbscan/sspd_distances/davies_bouldin/outliers.png)

#### erp_distances

##### Search params result

|   clusters |   outliers |   noise | method         |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|--------:|:---------------|---------:|--------------:|-------------------:|
|          5 |         47 | 6.20872 | davies_bouldin | 0.61976  |             1 |                 40 |
|          5 |         47 | 6.20872 | davies_bouldin | 0.61976  |             1 |                 60 |
|          5 |         47 | 6.20872 | davies_bouldin | 0.61976  |             1 |                 80 |
|          5 |         49 | 6.47292 | davies_bouldin | 0.627875 |             2 |                 40 |
|          5 |         49 | 6.47292 | davies_bouldin | 0.627875 |             2 |                 60 |
|          5 |         49 | 6.47292 | davies_bouldin | 0.627875 |             2 |                 80 |
|          5 |         49 | 6.47292 | davies_bouldin | 0.627875 |             3 |                 40 |
|          5 |         49 | 6.47292 | davies_bouldin | 0.627875 |             3 |                 60 |
|          5 |         49 | 6.47292 | davies_bouldin | 0.627875 |             3 |                 80 |
|          5 |         51 | 6.73712 | davies_bouldin | 0.665518 |             4 |                 40 |

##### Best estimator result

|   clusters |   outliers |   noise | method         |   score |   min_samples |   min_cluster_size |
|-----------:|-----------:|--------:|:---------------|--------:|--------------:|-------------------:|
|          5 |         47 | 6.20872 | davies_bouldin | 0.61976 |             1 |                 40 |

![](hdbscan/erp_distances/davies_bouldin/outliers.png)
