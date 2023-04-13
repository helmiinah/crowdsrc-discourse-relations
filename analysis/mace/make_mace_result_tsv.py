import pandas as pd
import re
import json
from sklearn.metrics import accuracy_score


with open("utils/structures_final_94.json", "r") as f:
    structures = json.load(f)


def url_to_id(x):
    x = re.match(r".+/(\d+_pair.png)$", x)
    x = x.group(1).replace("_pair.png", "")
    return int(x)


def find_gold_standard(row):
    d = [
        value
        for dic in structures
        for (key, value) in dic.items()
        if key == f"{row['id']}.png"
    ]
    return d[0]["relation"].replace("-", "")


raw_df = pd.read_csv("analysis/data/assignments_13-01-2023.tsv", sep="\t")
raw_df["INPUT:image"] = raw_df["INPUT:image"].apply(lambda x: url_to_id(x))
idx = sorted(raw_df["INPUT:image"].unique())

df = pd.read_csv(
    "analysis/mace/results/prediction_balanced", index_col=False, header=None
)
df = df.rename(columns={0: "mace"})
df["id"] = idx

df["gold"] = df.apply(lambda row: find_gold_standard(row), axis=1)

df = df[["id", "mace", "gold"]]
print(df)

acc = accuracy_score(df["mace"], df["gold"])
print("Accuracy:", acc)

df.to_csv("analysis/mace/results/mace_results_13-01-2023.tsv", sep="\t", index=None)
