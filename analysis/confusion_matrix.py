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

df1 = pd.read_csv("analysis/data/results_without_other_13-01-23.tsv", sep="\t")
cm = pycm.ConfusionMatrix(df1["gold"].to_numpy(), df1["agg_label"].to_numpy())

cm_array = cm.to_array(normalized=True).round(2)

print(cm_array)

hm = sns.heatmap(
    cm_array, cmap="crest", annot=True, xticklabels=classes, yticklabels=classes
)
hm.set_xlabel("Crowdsourced", fontsize=12)
hm.set_ylabel("Expert", fontsize=12)

# cm.plot(cmap=plt.cm.Oranges, number_label=True, normalized=True)

plt.title("Balanced distribution", fontweight="bold", fontsize=14)
plt.xticks(rotation="horizontal")
plt.tight_layout()
plt.gcf().set_size_inches(7.5, 5.5)
plt.savefig("analysis/pdf_plots/cm_balanced_13-01-23.pdf", format="pdf")
