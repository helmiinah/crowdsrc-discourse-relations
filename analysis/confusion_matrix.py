import pycm
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


classes = [
    "class-\nascription",
    "elaboration",
    "identification",
    "preparation",
    "property-\nascription",
]

df1 = pd.read_csv("analysis/data/results_without_other_20-01-23.tsv", sep="\t")
cm = pycm.ConfusionMatrix(df1["gold"].to_numpy(), df1["agg_label"].to_numpy())

cm_array = cm.to_array(normalized=True).round(2)

print(cm_array)

hm = sns.heatmap(
    cm_array, cmap="viridis_r", annot=True, xticklabels=classes, yticklabels=classes
)
hm.set_xlabel("Predicted", fontsize=12)
hm.set_ylabel("Gold", fontsize=12)

# cm.plot(cmap=plt.cm.Oranges, number_label=True, normalized=True)

plt.title("Random distribution", fontweight="bold", fontsize=14)
plt.xticks(rotation="horizontal")
plt.tight_layout()
plt.show()
