
# Case 3

Flight from Madrid to Alicante, Barcelona, Bilbao, Coruña, Córdoba, Granada and Jerez.

## Resume

### Silhouette

Best algorithm/function distance configuration based on silhouette score.

|   clusters |   outliers |    noise |    score | algorithm   | distance_fn    |
|-----------:|-----------:|---------:|---------:|:------------|:---------------|
|          9 |          8 | 0.467836 | 0.933264 | hdbscan     | erp_distances  |
|          9 |         18 | 1.05263  | 0.908816 | hdbscan     | sspd_distances |
|         39 |        142 | 8.30409  | 0.719922 | dbscan      | erp_distances  |
|         23 |        116 | 6.78363  | 0.6718   | dbscan      | sspd_distances |

Score represents the quality of the clustering. The best score is 1.0 and the worst score is -1.0. Scores around zero indicate overlapping clusters.

|               | dbscan  | hdbscan | 
|---------------|:-------:|:-------:|
| erp_distance  | ![](dbscan/erp_distances/silhouette/outliers.png) | ![](hdbscan/sspd_distances/silhouette/outliers.png) |
| sspd_distance | ![](dbscan/erp_distances/silhouette/outliers.png) | ![](hdbscan/sspd_distances/silhouette/outliers.png) |

### Davies-Bouldin

Best algorithm/function distance configuration based on davies_bouldin score.

|   clusters |   outliers |    noise |    score | algorithm   | distance_fn    |
|-----------:|-----------:|---------:|---------:|:------------|:---------------|
|         10 |         47 |  2.74854 | 0.376022 | hdbscan     | erp_distances  |
|         10 |         57 |  3.33333 | 0.555239 | hdbscan     | sspd_distances |
|         16 |        335 | 19.5906  | 0.99077  | dbscan      | erp_distances  |
|         16 |        190 | 11.1111  | 1.10795  | dbscan      | sspd_distances |

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

|   clusters |   outliers |    noise | method     |    score |       eps |   min_samples |
|-----------:|-----------:|---------:|:-----------|---------:|----------:|--------------:|
|         23 |        116 |  6.78363 | silhouette | 0.6718   | 0.0142401 |             5 |
|         27 |         95 |  5.55556 | silhouette | 0.666885 | 0.0142401 |             4 |
|         31 |         83 |  4.8538  | silhouette | 0.666362 | 0.0142401 |             3 |
|         19 |        138 |  8.07018 | silhouette | 0.660404 | 0.0142401 |             6 |
|         19 |        139 |  8.12865 | silhouette | 0.659916 | 0.0142401 |             7 |
|         19 |        139 |  8.12865 | silhouette | 0.659916 | 0.0142401 |             8 |
|         18 |        151 |  8.83041 | silhouette | 0.651028 | 0.0142401 |             9 |
|         17 |        162 |  9.47368 | silhouette | 0.640233 | 0.0142401 |            10 |
|         16 |        190 | 11.1111  | silhouette | 0.638891 | 0.0142401 |            15 |
|         16 |        172 | 10.0585  | silhouette | 0.633802 | 0.0142401 |            11 |

##### Best estimator result

|   clusters |   outliers |   noise | method     |   score |       eps |   min_samples |
|-----------:|-----------:|--------:|:-----------|--------:|----------:|--------------:|
|         23 |        116 | 6.78363 | silhouette |  0.6718 | 0.0142401 |             5 |

![](dbscan/sspd_distances/silhouette/outliers.png)

#### erp_distances

##### Search params result

|   clusters |   outliers |    noise | method     |    score |     eps |   min_samples |
|-----------:|-----------:|---------:|:-----------|---------:|--------:|--------------:|
|         39 |        142 |  8.30409 | silhouette | 0.719922 | 35348.5 |             3 |
|         33 |        163 |  9.53216 | silhouette | 0.70572  | 35348.5 |             4 |
|         30 |        179 | 10.4678  | silhouette | 0.700251 | 35348.5 |             5 |
|         54 |        112 |  6.54971 | silhouette | 0.696803 | 35348.5 |             2 |
|         26 |        203 | 11.8713  | silhouette | 0.696586 | 35348.5 |             6 |
|         26 |        212 | 12.3977  | silhouette | 0.686862 | 35348.5 |             7 |
|         24 |        227 | 13.2749  | silhouette | 0.674054 | 35348.5 |             8 |
|         22 |        243 | 14.2105  | silhouette | 0.656767 | 35348.5 |             9 |
|         20 |        266 | 15.5556  | silhouette | 0.633937 | 35348.5 |            10 |
|         19 |        277 | 16.1988  | silhouette | 0.623988 | 35348.5 |            11 |

##### Best estimator result

|   clusters |   outliers |   noise | method     |    score |     eps |   min_samples |
|-----------:|-----------:|--------:|:-----------|---------:|--------:|--------------:|
|         39 |        142 | 8.30409 | silhouette | 0.719922 | 35348.5 |             3 |

![](dbscan/erp_distances/silhouette/outliers.png)

### hdbscan

#### sspd_distances

##### Search params result

|   clusters |   outliers |   noise | method     |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|--------:|:-----------|---------:|--------------:|-------------------:|
|          9 |         18 | 1.05263 | silhouette | 0.908816 |             1 |                100 |
|          9 |         18 | 1.05263 | silhouette | 0.908816 |             2 |                100 |
|          9 |         18 | 1.05263 | silhouette | 0.908816 |             3 |                100 |
|          9 |         18 | 1.05263 | silhouette | 0.908816 |             4 |                100 |
|          9 |         18 | 1.05263 | silhouette | 0.908816 |             5 |                100 |
|          9 |         18 | 1.05263 | silhouette | 0.908816 |             6 |                100 |
|          9 |         18 | 1.05263 | silhouette | 0.908816 |             7 |                100 |
|          9 |         18 | 1.05263 | silhouette | 0.908816 |             8 |                100 |
|          9 |         18 | 1.05263 | silhouette | 0.908816 |             9 |                100 |
|          9 |         18 | 1.05263 | silhouette | 0.908816 |            10 |                100 |

##### Best estimator result

|   clusters |   outliers |   noise | method     |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|--------:|:-----------|---------:|--------------:|-------------------:|
|          9 |         18 | 1.05263 | silhouette | 0.908816 |             1 |                100 |

![](hdbscan/sspd_distances/silhouette/outliers.png)

#### erp_distances

##### Search params result

|   clusters |   outliers |    noise | method     |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|---------:|:-----------|---------:|--------------:|-------------------:|
|          9 |          8 | 0.467836 | silhouette | 0.933264 |             1 |                100 |
|          9 |          8 | 0.467836 | silhouette | 0.933264 |             1 |                120 |
|          9 |          9 | 0.526316 | silhouette | 0.932849 |             2 |                100 |
|          9 |          9 | 0.526316 | silhouette | 0.932849 |             2 |                120 |
|          9 |          9 | 0.526316 | silhouette | 0.932849 |             3 |                100 |
|          9 |          9 | 0.526316 | silhouette | 0.932849 |             3 |                120 |
|          9 |         11 | 0.643275 | silhouette | 0.932015 |             4 |                100 |
|          9 |         11 | 0.643275 | silhouette | 0.932015 |             5 |                100 |
|          9 |         14 | 0.818713 | silhouette | 0.930294 |            11 |                100 |
|          9 |         14 | 0.818713 | silhouette | 0.930294 |            13 |                100 |

##### Best estimator result

|   clusters |   outliers |    noise | method     |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|---------:|:-----------|---------:|--------------:|-------------------:|
|          9 |          8 | 0.467836 | silhouette | 0.933264 |             1 |                100 |

![](hdbscan/erp_distances/silhouette/outliers.png)

# davies_bouldin

### dbscan

Finding the best eps value.

![](dbscan/erp_distances/davies_bouldin/elbow.png)

In order to calculate the best eps value, first, the nearest neighbors of the data are calculated. Then, the points are sorted and in order to obtain a curve. Next, a line is generated that fits to the curve and the distances between each point of the curve and the line are calculated. The elbow index is the point where the distance is maximum.

As a custom distance function it is used, the distance between trajectories are normalized and epsilon values may not be true magnitudes.

#### sspd_distances

##### Search params result

|   clusters |   outliers |    noise | method         |   score |       eps |   min_samples |
|-----------:|-----------:|---------:|:---------------|--------:|----------:|--------------:|
|         16 |        190 | 11.1111  | davies_bouldin | 1.10795 | 0.0142401 |            15 |
|         27 |         95 |  5.55556 | davies_bouldin | 1.12157 | 0.0142401 |             4 |
|         17 |        162 |  9.47368 | davies_bouldin | 1.12269 | 0.0142401 |            10 |
|         16 |        174 | 10.1754  | davies_bouldin | 1.12797 | 0.0142401 |            13 |
|         16 |        172 | 10.0585  | davies_bouldin | 1.12837 | 0.0142401 |            11 |
|         16 |        172 | 10.0585  | davies_bouldin | 1.12837 | 0.0142401 |            12 |
|         19 |        139 |  8.12865 | davies_bouldin | 1.13317 | 0.0142401 |             7 |
|         19 |        139 |  8.12865 | davies_bouldin | 1.13317 | 0.0142401 |             8 |
|         17 |        174 | 10.1754  | davies_bouldin | 1.13326 | 0.0142401 |            14 |
|         19 |        138 |  8.07018 | davies_bouldin | 1.13498 | 0.0142401 |             6 |

##### Best estimator result

|   clusters |   outliers |   noise | method         |   score |       eps |   min_samples |
|-----------:|-----------:|--------:|:---------------|--------:|----------:|--------------:|
|         16 |        190 | 11.1111 | davies_bouldin | 1.10795 | 0.0142401 |            15 |

![](dbscan/sspd_distances/davies_bouldin/outliers.png)

#### erp_distances

##### Search params result

|   clusters |   outliers |    noise | method         |    score |     eps |   min_samples |
|-----------:|-----------:|---------:|:---------------|---------:|--------:|--------------:|
|         16 |        335 | 19.5906  | davies_bouldin | 0.99077  | 35348.5 |            15 |
|         16 |        329 | 19.2398  | davies_bouldin | 0.996401 | 35348.5 |            14 |
|         17 |        313 | 18.3041  | davies_bouldin | 0.997855 | 35348.5 |            13 |
|         18 |        295 | 17.2515  | davies_bouldin | 1.02183  | 35348.5 |            12 |
|         19 |        277 | 16.1988  | davies_bouldin | 1.04431  | 35348.5 |            11 |
|         20 |        266 | 15.5556  | davies_bouldin | 1.04724  | 35348.5 |            10 |
|         22 |        243 | 14.2105  | davies_bouldin | 1.06706  | 35348.5 |             9 |
|         24 |        227 | 13.2749  | davies_bouldin | 1.10188  | 35348.5 |             8 |
|         26 |        212 | 12.3977  | davies_bouldin | 1.11338  | 35348.5 |             7 |
|         39 |        142 |  8.30409 | davies_bouldin | 1.13297  | 35348.5 |             3 |

##### Best estimator result

|   clusters |   outliers |   noise | method         |   score |     eps |   min_samples |
|-----------:|-----------:|--------:|:---------------|--------:|--------:|--------------:|
|         16 |        335 | 19.5906 | davies_bouldin | 0.99077 | 35348.5 |            15 |

![](dbscan/erp_distances/davies_bouldin/outliers.png)

### hdbscan

#### sspd_distances

##### Search params result

|   clusters |   outliers |   noise | method         |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|--------:|:---------------|---------:|--------------:|-------------------:|
|         10 |         57 | 3.33333 | davies_bouldin | 0.555239 |             1 |                 80 |
|         10 |         57 | 3.33333 | davies_bouldin | 0.555239 |             2 |                 80 |
|         10 |         57 | 3.33333 | davies_bouldin | 0.555239 |             3 |                 80 |
|         10 |         57 | 3.33333 | davies_bouldin | 0.555239 |             4 |                 80 |
|         10 |         57 | 3.33333 | davies_bouldin | 0.555239 |             5 |                 80 |
|         10 |         57 | 3.33333 | davies_bouldin | 0.555239 |             6 |                 80 |
|         10 |         57 | 3.33333 | davies_bouldin | 0.555239 |             7 |                 80 |
|         10 |         57 | 3.33333 | davies_bouldin | 0.555239 |             8 |                 80 |
|         10 |         57 | 3.33333 | davies_bouldin | 0.555239 |             9 |                 80 |
|         10 |         57 | 3.33333 | davies_bouldin | 0.555239 |            10 |                 80 |

##### Best estimator result

|   clusters |   outliers |   noise | method         |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|--------:|:---------------|---------:|--------------:|-------------------:|
|         10 |         57 | 3.33333 | davies_bouldin | 0.555239 |             1 |                 80 |

![](hdbscan/sspd_distances/davies_bouldin/outliers.png)

#### erp_distances

##### Search params result

|   clusters |   outliers |   noise | method         |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|--------:|:---------------|---------:|--------------:|-------------------:|
|         10 |         47 | 2.74854 | davies_bouldin | 0.376022 |             1 |                 80 |
|         10 |         49 | 2.8655  | davies_bouldin | 0.379135 |             2 |                 60 |
|         10 |         49 | 2.8655  | davies_bouldin | 0.379135 |             2 |                 80 |
|         10 |         49 | 2.8655  | davies_bouldin | 0.379135 |             3 |                 60 |
|         10 |         49 | 2.8655  | davies_bouldin | 0.379135 |             3 |                 80 |
|         10 |         51 | 2.98246 | davies_bouldin | 0.392887 |             4 |                 60 |
|         10 |         51 | 2.98246 | davies_bouldin | 0.392887 |             4 |                 80 |
|         10 |         51 | 2.98246 | davies_bouldin | 0.392887 |             5 |                 60 |
|         10 |         51 | 2.98246 | davies_bouldin | 0.392887 |             5 |                 80 |
|         10 |         55 | 3.21637 | davies_bouldin | 0.403465 |            10 |                 80 |

##### Best estimator result

|   clusters |   outliers |   noise | method         |    score |   min_samples |   min_cluster_size |
|-----------:|-----------:|--------:|:---------------|---------:|--------------:|-------------------:|
|         10 |         47 | 2.74854 | davies_bouldin | 0.376022 |             1 |                 80 |

![](hdbscan/erp_distances/davies_bouldin/outliers.png)
