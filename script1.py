import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset("tips")

fig, ax = plt.subplots()
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="smoker")

plt.savefig("fig.png")