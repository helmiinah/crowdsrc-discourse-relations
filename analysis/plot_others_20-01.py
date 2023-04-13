"""
Check which relations received answer 'None of the above'.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import json
import re


sns.set()

fig = plt.figure()
df1 = pd.read_csv("analysis/data/results_20-01-23.tsv", sep="\t")
df1 = df1[df1["agg_label"] == "other"]
df1 = df1.rename(columns={"gold": "expert annotation"})
df1 = df1.replace("propertyascription", "property-\nascription")
df1 = df1.replace("identification", "identification\n")

df2 = pd.read_csv("analysis/data/results_13-01-23.tsv", sep="\t")
df2 = df2[df2["agg_label"] == "other"]
df2 = df2.rename(columns={"gold": "expert annotation"})
df2 = df2.replace("propertyascription", "property-\nascription")
df2 = df2.replace("identification", "identification\n")

fig, axs = plt.subplots(ncols=2, sharey=True)

sns.countplot(data=df2, x="expert annotation", palette="crest", ax=axs[0]).set(
    title="Balanced distribution (Trial run 5)"
)
sns.countplot(
    data=df1, x="expert annotation", palette="pastel", ax=axs[1], width=0.27
).set(title="Random distribution (Trial run 6)")
fig.suptitle(
    'Relations annotated with "None of the above" by crowdworkers', fontsize=16
)
axs[1].set(ylabel=None)

plt.tight_layout()
plt.gcf().set_size_inches(7.5, 4.5)
plt.savefig("analysis/pdf_plots/other_both.pdf", format="pdf", dpi=199)
