import pandas as pd
import os


df = pd.DataFrame(columns=["image"])

for f in os.listdir("../pipeline/data/bbox_pairs"):
    url = f"https://s3.datacloud.helsinki.fi/crowdsrc:disc-rel/{f}"
    print(url)
    row = pd.DataFrame({"image": [url]})
    df = pd.concat([df, row], ignore_index=True)

print(df)

df.to_csv("../pipeline/data/bbox_pairs_100.tsv", sep="\t", index=None)