# multifurcating_trees

## Setup

[Install conda](https://conda.io/en/latest/miniconda.html). Then create an environment for the analysis and install augur.

```bash
conda create -n multifurcations python=3 pandas seaborn
conda activate multifurcations
pip install nextstrain-augur
```

## Analysis

Run the analysis script. Tables with children per node per tree are output in `tables/`. Histograms of children per node are output in `figures/`.

```bash
./run.sh
```
