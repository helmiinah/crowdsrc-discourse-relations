"""
Check distribution of chosen class.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import OrderedDict

sns.set()

fig = plt.figure()

data_dist = OrderedDict(
    sorted(
        {
            "identification": 65,
            "preparation": 14,
            "propertyascription": 12,
            "elaboration": 5,
            "classascription": 4,
        }.items()
    )
)

bars = sns.barplot(x=list(data_dist.keys()), y=list(data_dist.values()))
bars.set_xticklabels(bars.get_xticklabels(), rotation=90)
bars.set_title("Class distribution")

fig.set_size_inches(3, 6)
plt.tight_layout()

plt.savefig("analysis/plots/class_distribution_20-13-23.png")
plt.show()
