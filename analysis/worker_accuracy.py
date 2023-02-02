"""
Check accuracy of each worker.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import json
import re


with open("utils/structures_random_100.json", "r") as f:
    structures = json.load(f)


def find_gold_standard(row):
    d = [
        value for dic in structures for (key, value) in dic.items() if key == row["id"]
    ]
    return d[0]["relation"].replace("-", "")


def url_to_id(x):
    x = re.match(r".+/(\d+_pair.png)$", x)
    x = x.group(1).replace("_pair", "")
    return x


sns.set()

df1 = pd.read_csv("analysis/data/assignments_20-01-2023.tsv", sep="\t")
df1 = df1[["ASSIGNMENT:worker_id", "OUTPUT:result", "INPUT:image"]]
df1 = df1.rename(
    columns={
        "ASSIGNMENT:worker_id": "worker",
        "OUTPUT:result": "pred_label",
        "INPUT:image": "id",
    }
)

for i, worker in enumerate(df1["worker"].unique()):
    df1["worker"] = df1["worker"].replace(worker, i + 1)

df1["id"] = df1["id"].apply(lambda x: url_to_id(x))
df1["gold_label"] = df1.apply(lambda row: find_gold_standard(row), axis=1)

df1 = df1[["worker", "id", "pred_label", "gold_label"]]
worker_accuracies = {}

for i in range(1, len(df1["worker"].unique()) + 1):
    acc = accuracy_score(
        df1[df1.worker == i]["pred_label"], df1[df1.worker == i]["gold_label"]
    )
    print(f"Worker {i} accuracy: {acc}")
    worker_accuracies[f"Worker {i}"] = round(acc, 2) * 100

plt.bar(
    range(len(worker_accuracies)),
    list(worker_accuracies.values()),
    align="center",
    color=["#5b62ab", "#5b96ab", "#5bab98", "#5bab6e", "#88ab5b"],
)
plt.xticks(range(len(worker_accuracies)), list(worker_accuracies.keys()))
plt.title("Worker accuracy (%)")
plt.ylim(0, 100)

plt.savefig("analysis/plots/worker_accuracy_20-01-2023.png")

print(worker_accuracies)
print(df1)
