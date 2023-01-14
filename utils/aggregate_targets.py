# -*- coding: utf-8 -*-

from crowdkit.aggregation.classification.dawid_skene import DawidSkene
import pandas as pd
import toloka.client as toloka
import json

df = pd.read_csv("utils/assignments/assignments_13-01-2023.tsv", sep="\t")

df["task"] = df["INPUT:image"].astype(str)
df = df.rename(columns={"OUTPUT:result": "label", "ASSIGNMENT:worker_id": "worker"})
print(df)

# df = df[["task", "worker", "label", "image", "outlines"]]

result = DawidSkene().fit_predict(df)

print(len(result))
result.to_csv(f"describe_relations_results_13-01-23.tsv", sep="\t")
