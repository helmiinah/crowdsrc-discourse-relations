import pandas as pd
import re
import json


with open("structures.json", "r") as f:
    structures = json.load(f)


def remove_ab(x):
    if (x[0:2] == "A " and x[-2:] == " B") or (x[0:2] == "B " and x[-2:] == " A"):
        x = x[2:-2]
    return x.lower().strip()


def url_to_id(x):
    x = re.match(r".+/(\d+_pair.png)$", x)
    x = x.group(1).replace("_pair", "")
    return x


def find_gold_standard(row):
    d = [value for dic in structures for (key, value) in dic.items() if key == row["id"]]
    return d[0]["relation"]

df = pd.read_csv("assignments/description_assignments_28-09-2022.tsv", sep="\t")

df["OUTPUT:result"] = df["OUTPUT:result"].apply(lambda x: remove_ab(x))
df["INPUT:image"] = df["INPUT:image"].apply(lambda x: url_to_id(x))

df = df.rename(columns={"INPUT:image": "id", "OUTPUT:result": "answer"})

df["gold"] = df.apply(lambda row: find_gold_standard(row), axis=1)

df = df.sort_values(by=["id"])

df[["id", "answer", "gold"]].to_csv("cleaned_assignments_28-09-22.tsv", sep="\t", index=None)
