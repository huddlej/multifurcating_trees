#!/bin/bash

# Define variables.
MIN_CHILDREN=3

# Prepare output directories.
DATA_DIR=data
TABLES_DIR=tables
FIGURES_DIR=figures
mkdir -p ${DATA_DIR} ${TABLES_DIR} ${FIGURES_DIR}

# Define trees to analyze.
TREES="flu_seasonal_h3n2_ha_2y_tree.json ebola_tree.json zika_tree.json mumps_global_tree.json"

# Analyze multifications per tree.
for tree in ${TREES}
do
    echo "Analyzing tree: ${tree}"
    curl http://data.nextstrain.org/${tree} | gzip -c -d > ${DATA_DIR}/${tree}
    python3 scripts/multifurcations.py ${DATA_DIR}/${tree} ${TABLES_DIR}/${tree/_tree.json/.tsv}
    python3 scripts/plot_children_per_node.py ${TABLES_DIR}/${tree/_tree.json/.tsv} ${FIGURES_DIR}/${tree/_tree.json/.pdf} --min-children ${MIN_CHILDREN}
done
