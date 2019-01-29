import argparse
from augur.utils import json_to_tree
import json
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import seaborn as sns


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("table", help="tree JSON from Nextstrain (e.g., ebola_tree.json)")
    parser.add_argument("output", help="table of children per node for the given tree")
    parser.add_argument("--min-children", type=int, default=1, help="minimum children required per node to plot")

    args = parser.parse_args()

    table_path = Path(args.table)
    df = pd.read_table(args.table)
    df = df[df["number_of_children"] >= args.min_children].copy()

    ax = sns.distplot(df["number_of_children"], kde=False)
    ax.set_xlabel("Number of children per node")
    ax.set_ylabel("Number of nodes")
    ax.set_title(table_path.name.split(".")[0])

    plt.savefig(args.output)
    plt.close()
