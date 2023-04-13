import pandas as pd
import re


def url_to_id(x):
    x = re.match(r".+/(\d+_pair.png)$", x)
    x = x.group(1).replace("_pair.png", "")
    return int(x)


raw_df = pd.read_csv("analysis/data/assignments_20-01-2023.tsv", sep="\t")

raw_df["INPUT:image"] = raw_df["INPUT:image"].apply(lambda x: url_to_id(x))

workers = list(range(1, len(raw_df["ASSIGNMENT:worker_id"].unique()) + 1))

for i, worker in enumerate(raw_df["ASSIGNMENT:worker_id"].unique()):
    raw_df["ASSIGNMENT:worker_id"] = raw_df["ASSIGNMENT:worker_id"].replace(
        worker, i + 1
    )

print(raw_df)

rows = []
idx = sorted(raw_df["INPUT:image"].unique())
for img_id in idx:
    row = []
    for worker in workers:
        try:
            pred = raw_df.loc[
                (raw_df["INPUT:image"] == img_id)
                & (raw_df["ASSIGNMENT:worker_id"] == worker),
                "OUTPUT:result",
            ].values[0]
        except:
            pred = ""
        row.extend([pred])
    rows.append(row)

columns = []
columns.extend(list(range(1, len(raw_df["ASSIGNMENT:worker_id"].unique()) + 1)))
df = pd.DataFrame(rows, columns=columns, index=idx)
print(df)

df.to_csv("analysis/mace/mace_input_random.csv", index=None, columns=None)
