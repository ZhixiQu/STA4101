from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import pandas as pd

# Load built-in Iris dataset
iris = load_iris(as_frame=True)
df = iris.frame
df["species"] = df["target"].map(dict(zip(range(3), iris.target_names)))

# Aesthetic setup
plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(8, 6))

# Scatter plot by species
colors = {"setosa":"#0000FF", "versicolor":"#00FFFF", "virginica":"#DBC7DB"}
for species, group in df.groupby("species"):
    ax.scatter(
        group["sepal length (cm)"],
        group["sepal width (cm)"],
        label=species,
        s=100000,
        alpha=0.8,
        edgecolor="white",
        linewidth=0.8,
        color=colors[species],
    )

# Titles and labels
ax.set_title("daascscscee", fontsize=16, weight="bold")
ax.set_xlabel("scwcververv", fontsize=12)
ax.set_ylabel("vrverververv", fontsize=12)

# Legend and layout
ax.legend(title="Species", frameon=True)
plt.tight_layout()
plt.show()