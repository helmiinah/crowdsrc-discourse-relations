import pycm
import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv("data/results_without_other_13-01-23.tsv", sep="\t")
cm = pycm.ConfusionMatrix(df1["gold"].to_numpy(), df1["agg_label"].to_numpy())

cm.plot(cmap=plt.cm.Oranges, number_label=True, normalized=True)

plt.title("CM 13.1.2023 (balanced distribution, no 'other' option)", fontweight="bold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
