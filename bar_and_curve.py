#%%
import os 
from matplotlib import pyplot as plt
import numpy as np
import os 
np.random.seed(42)

#%% figure data
segments = 9
data = [[np.random.rand() for _ in range(segments)] for _ in range(2)]

# figure params
color_bar = "gray"
color_line = "darkviolet"
bar_width = 1/segments/2
xtick_labels_size = 50 / segments


# figure making
fig, ax = plt.subplots(figsize=(12,6))

# line plot
p1, = ax.plot([i/segments + 0.5 / segments  for i in range(segments)], np.sort(data[0]), color = color_line, label = 'REAL', marker = 'o')
bar_xpos = [pos + 0.5 / segments for pos in np.linspace(0, 1, segments+1)[:segments]]

# bar plot
tw = ax.twinx()
p2 = tw.bar(bar_xpos, np.array(data[1]), color = color_bar, width=bar_width, label = ' RMSE', alpha=0.5)

# bar xtick position and label
tw.set_xticks([pos + 0.5 / segments for pos in np.linspace(0, 1, segments+1)[:segments]])
xtick_labels = ['[{:.2f}, {:.2f})'.format(pos, (pos+1/segments)) for pos in np.linspace(0, 1, segments+1)[:segments] ]
xtick_labels[-1] = xtick_labels[-1].replace(')', ']')
tw.set_xticklabels(xtick_labels, fontsize = xtick_labels_size)

# set ytick
tkw_y = dict(size=10, width=1.5, labelsize = 14)
ax.tick_params(axis='y', colors=color_line, **tkw_y)
tw.tick_params(axis='y', colors = color_bar, **tkw_y)
ax.set_ylabel("yLabel",fontsize= 18)
tw.set_ylabel("Metric",fontsize= 18)

# layout and save
ax.legend(handles=[p1,p2],prop={'size':18})
ax.grid(True)
plt.rcParams['savefig.facecolor'] = "1"
fig.tight_layout()
fig.savefig('./figures/bar_and_curve.svg')


