import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# figure data
boxes = [np.random.random(size = 1000) for i in range(5)]
xlabels = ["Label {}".format(i) for i in range(5)]

# figure making
fig, ax = plt.subplots(figsize=(8, 5))
bp = ax.boxplot(boxes,labels = xlabels, patch_artist = True, showfliers=False)
colors = plt.get_cmap('inferno')(
        np.linspace(0.15, 0.85, 5))
for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
ax.yaxis.grid(True)
fontsize = 14
ax.set_xlabel('Data1',fontsize = fontsize,) 
ax.set_ylabel('Data2', fontsize = fontsize) 
plt.setp(ax.get_xticklabels(), fontsize=fontsize) 
plt.setp(ax.get_yticklabels(), fontsize=fontsize)

plt.tight_layout()
plt.savefig('./figures/boxplot.svg')