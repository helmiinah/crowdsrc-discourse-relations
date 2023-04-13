import pandas as pd
import re
import json
from sklearn.metrics import accuracy_score, classification_report


with open("utils/structures_final_94.json", "r") as f:
    structures = json.load(f)


def url_to_id(x):
    x = re.match(r".+/(\d+_pair.png)$", x)
    x = x.group(1).replace("_pair", "")
    return x


def find_gold_standard(row):
    d = [
        value for dic in structures for (key, value) in dic.items() if key == row["id"]
    ]
    return d[0]["relation"].replace("-", "")


df = pd.read_csv("pipeline_4/aggregate_relations_results_13-01-23.tsv", sep="\t")
df = df.rename(columns={"task": "id"})

df_without_other = df[df["agg_label"] != "other"]

df_without_other["id"] = df_without_other["id"].apply(lambda x: url_to_id(x))
df_without_other["gold"] = df_without_other.apply(
    lambda row: find_gold_standard(row), axis=1
)

df_without_other = df_without_other.sort_values(by=["id"])

acc = accuracy_score(df_without_other["agg_label"], df_without_other["gold"])
print("Accuracy:", acc)

print(classification_report(df_without_other["agg_label"], df_without_other["gold"]))

# df_without_other.to_csv(
#    "pipeline_4/results/results_without_other_20-01-23.tsv", sep="\t", index=None
# )

# df["id"] = df["id"].apply(lambda x: url_to_id(x))
# df["gold"] = df.apply(lambda row: find_gold_standard(row), axis=1)

# df = df.sort_values(by=["id"])

# acc = accuracy_score(df["agg_label"], df["gold"])
# print("Accuracy:", acc)

# df.to_csv("pipeline_4/results/results_13-01-23.tsv", sep="\t", index=None)
