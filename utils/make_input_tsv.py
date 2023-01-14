import pandas as pd
import os


df = pd.DataFrame(columns=["image"])

for f in os.listdir("pipeline_4/data/bbox_pairs_final_94"):
    url = f"https://s3.datacloud.helsinki.fi/crowdsrc:disc-rel/{f}"
    print(url)
    row = pd.DataFrame({"image": [url]})
    df = pd.concat([df, row], ignore_index=True)

print(df)

df.to_csv("pipeline_4/data/bbox_pairs_final_94.tsv", sep="\t", index=None)
