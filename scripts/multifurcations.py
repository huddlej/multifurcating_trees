import argparse
from augur.utils import json_to_tree
import json
import pandas as pd
from pathlib import Path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("tree", help="tree JSON from Nextstrain (e.g., ebola_tree.json)")
    parser.add_argument("output", help="table of children per node for the given tree")
    parser.add_argument("--multifurcating-only", action="store_true", help="only output nodes with more than 2 children")

    args = parser.parse_args()

    with open(args.tree, "r") as fh:
        tree_json = json.load(fh)

    tree = json_to_tree(tree_json)

    # Calculate number of children per internal node.
    children_per_node = [
        (node.name, len(node.clades))
        for node in tree.find_clades()
        if not node.is_terminal() and (not args.multifurcating_only or len(node.clades) > 2)
    ]

    df = pd.DataFrame(children_per_node, columns=["node", "number_of_children"])

    # Annotate source name based on tree filename.
    tree_path = Path(args.tree)
    source = tree_path.name.split(".")[0]
    df["source"] = source

    df.to_csv(args.output, sep="\t", index=False)
