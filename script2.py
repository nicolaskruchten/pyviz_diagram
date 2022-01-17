import matplotlib.pyplot as plt
import mplcursors
import seaborn as sns
tips = sns.load_dataset("tips")

fig, ax = plt.subplots()
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="smoker")

@mplcursors.cursor(ax, hover=True).connect("add")
def on_add(sel):
    sel.annotation.set(text=tips.sex[sel.index])
    
plt.show()