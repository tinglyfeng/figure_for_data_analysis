import matplotlib
import matplotlib as mpl
from matplotlib import pyplot as plt
import random


# figure data
x_data = [random.random() for _ in range(2000)]
y_data = [e + random.random()  for e in x_data]

# figure params
scatter_color = "coral"

# figure making
fig, ax = plt.subplots(figsize = (12,6))
cm_base = x_data
cmap = plt.get_cmap('hot')
sc = ax.scatter(y_data, x_data,c = x_data, marker = "o",s=100,cmap=cmap, edgecolor='y', alpha = 0.9)
tkw = dict(size=6, width=1.5, labelsize = 18)

ax.set_xlabel('xLabel', fontsize = 20)
ax.set_ylabel("yLabel", fontsize = 20)
ax.tick_params(axis='y', **tkw)
ax.tick_params(axis='x', **tkw)

ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(True, axis = 'y')

clb = fig.colorbar(sc,ticks=[1e-2, max(x_data)/2,max(x_data)])
clb.ax.tick_params(size=10)
clb.ax.set_yticklabels(["Low", "Mid", "High"],size = 18)

plt.rcParams['savefig.facecolor'] = "1"
fig.tight_layout()
fig.savefig("./figures/gradual_scatter.svg")