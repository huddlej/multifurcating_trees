# multifurcating_trees

## Setup

[Install conda](https://conda.io/en/latest/miniconda.html) and then create an environment for the analysis.

```bash
conda env create -f=environment.yaml
```

## Analysis

Run the analysis script. Tables with children per node per tree are output in `tables/`. Histograms of children per node are output in `figures/`.

```bash
conda activate multifurcations
./run.sh
```
