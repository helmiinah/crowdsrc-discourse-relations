import pandas as pd
import re
import json
from sklearn.metrics import accuracy_score


with open("utils/structures.json", "r") as f:
    structures = json.load(f)


def url_to_id(x):
    x = re.match(r".+/(\d+_pair.png)$", x)
    x = x.group(1).replace("_pair", "")
    return x


def find_gold_standard(row):
    d = [value for dic in structures for (key, value) in dic.items() if key == row["id"]]
    return d[0]["relation"]

df = pd.read_csv("pipeline_3/aggregate_relations_results.tsv", sep="\t")
df = df.rename(columns={"task": "id"})

df["id"] = df["id"].apply(lambda x: url_to_id(x))
df["gold"] = df.apply(lambda row: find_gold_standard(row), axis=1)

df = df.sort_values(by=["id"])

acc = accuracy_score(df["agg_label"], df["gold"])
print("Accuracy:", acc)

#df.to_csv("results_07-11-22.tsv", sep="\t", index=None)
