"""
Check distribution of chosen class for each worker.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

# 13.1.2023:

df1 = pd.read_csv("data/assignments_13-01-2023.tsv", sep="\t")
df1 = df1[["ASSIGNMENT:worker_id", "OUTPUT:result"]]

df1 = df1.rename(columns={"ASSIGNMENT:worker_id": "worker", "OUTPUT:result": "label"})

# sns.displot(data=df1, x="label")

for i, worker in enumerate(df1["worker"].unique()):
    df1["worker"] = df1["worker"].replace(worker, i + 1)

unique_n = len(df1["worker"].unique())

fig, ax = plt.subplots(1, unique_n, sharey=True)
fig.subplots_adjust(bottom=0.35)

for i in range(1, unique_n + 1):
    ax[i - 1].set_title(f"Worker {i}")

worker_1 = df1[df1["worker"] == 1]
worker_2 = df1[df1["worker"] == 2]
worker_3 = df1[df1["worker"] == 3]

worker_1_counts = worker_1["label"].value_counts().sort_index()
worker_2_counts = worker_2["label"].value_counts().sort_index()
worker_3_counts = worker_3["label"].value_counts().sort_index()

print(worker_1_counts)

bars1 = sns.barplot(ax=ax[0], x=worker_1_counts.index, y=worker_1_counts.values)
ax[0].set_title("Worker 1")
bars1.set_xticklabels(bars1.get_xticklabels(), rotation=90)

bars2 = sns.barplot(ax=ax[1], x=worker_2_counts.index, y=worker_2_counts.values)
ax[1].set_title("Worker 2")
bars2.set_xticklabels(bars2.get_xticklabels(), rotation=90)

bars3 = sns.barplot(ax=ax[2], x=worker_3_counts.index, y=worker_3_counts.values)
ax[2].set_title("Worker 3")
bars3.set_xticklabels(bars3.get_xticklabels(), rotation=90)

# plt.savefig("plots/worker_distribution_13-01-23.png")
plt.show()


# 20.1.2023:

df2 = pd.read_csv("data/assignments_20-01-2023.tsv", sep="\t")
df2 = df2[["ASSIGNMENT:worker_id", "OUTPUT:result"]]

df2 = df2.rename(columns={"ASSIGNMENT:worker_id": "worker", "OUTPUT:result": "label"})
df2 = df2.astype({"label": "category"})

# sns.displot(data=df1, x="label")

for i, worker in enumerate(df2["worker"].unique()):
    df2["worker"] = df2["worker"].replace(worker, i + 1)

unique_n = len(df2["worker"].unique())
print("UNIIKKEJA", unique_n)

fig, ax = plt.subplots(1, unique_n, sharey=True)
fig.subplots_adjust(bottom=0.35)

for i in range(1, unique_n + 1):
    ax[i - 1].set_title(f"Worker {i}")

worker_1 = df2[df2["worker"] == 1]
worker_2 = df2[df2["worker"] == 2]
worker_3 = df2[df2["worker"] == 3]
worker_4 = df2[df2["worker"] == 4]
worker_5 = df2[df2["worker"] == 5]

worker_1_counts = worker_1["label"].value_counts().sort_index()
worker_2_counts = worker_2["label"].value_counts().sort_index()
worker_3_counts = worker_3["label"].value_counts().sort_index()
worker_4_counts = worker_4["label"].value_counts().sort_index()
worker_5_counts = worker_5["label"].value_counts().sort_index()

bars1 = sns.barplot(ax=ax[0], x=worker_1_counts.index, y=worker_1_counts.values)
ax[0].set_title("Worker 1")
bars1.set_xticklabels(bars1.get_xticklabels(), rotation=90)

bars2 = sns.barplot(ax=ax[1], x=worker_2_counts.index, y=worker_2_counts.values)
ax[1].set_title("Worker 2")
bars2.set_xticklabels(bars2.get_xticklabels(), rotation=90)

bars3 = sns.barplot(ax=ax[2], x=worker_3_counts.index, y=worker_3_counts.values)
ax[2].set_title("Worker 3")
bars3.set_xticklabels(bars3.get_xticklabels(), rotation=90)

bars4 = sns.barplot(ax=ax[3], x=worker_4_counts.index, y=worker_4_counts.values)
ax[3].set_title("Worker 4")
bars4.set_xticklabels(bars4.get_xticklabels(), rotation=90)

bars5 = sns.barplot(ax=ax[4], x=worker_5_counts.index, y=worker_5_counts.values)
ax[4].set_title("Worker 5")
bars5.set_xticklabels(bars5.get_xticklabels(), rotation=90)

fig.set_size_inches(10, 5)
plt.savefig(
    "plots/worker_distribution_20-01-23.png",
)
plt.show()
