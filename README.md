### Installation steps

#### Install micromamba
Follow [micromamba installation instruction](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html)
#### Create env
```script
micromamba create -f spec_file.yaml
```
#### Use env
```script
micromamba activate ucjc_tfm_env
```

#### Add dataset 

This notebooks uses Eurocontrol datasets. More precisely, uses 2 types of Eurocontrol datasets, flights (those files prefixed with Fligths_) and flights points (prefixed with Flight_Points_Actual_)

On the top section of every notebook there's a constant section where the path for flight points and flights datasets era specified. By default, these paths are `data/flight_points` and `data/flights` (included in .gitignore by default as well).

In these folders you can add as many files of each type as you wish.
