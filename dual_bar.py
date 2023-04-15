#%%
import matplotlib
from matplotlib import pyplot as plt

import random
random.seed(43)
# figure data
bar_cnt = 10
xdata1 = [random.random() for _ in range(bar_cnt)]
xdata2 = [random.random() * 10 for _ in range(bar_cnt)]

# figure params
color1 = "#2c3c4b"
color2 = "#ae3b2f"
axis_label_size = 30
axis_label_pad = 10
digit_fontsize = 22

# figure making
fig, ax = plt.subplots(figsize=(18,8))
tw = ax.twinx()
bar_width = 0.04
ax.bar([i/bar_cnt-0.02 for i in range(bar_cnt)], xdata1, width = bar_width, color = color1)

tw.bar([i/bar_cnt + 0.02 for i in range(bar_cnt)], xdata2, width = bar_width, color = color2)

for i in range(bar_cnt):
    x_pos = i/bar_cnt - 0.05
    y_pos  =  xdata1[i]+0.007
    ax.text(x_pos, y_pos, str(y_pos)[:4],fontsize = digit_fontsize, color = color1)
    x_pos = i/bar_cnt
    y_pos  =  xdata2[i]+0.007
    tw.text(x_pos, y_pos, str(y_pos)[:4],fontsize = digit_fontsize, color = color2)
    
    
ax.yaxis.label.set_color(color1)
ax.yaxis.label.set_fontsize(12)
tw.yaxis.label.set_color(color2)
tw.yaxis.label.set_fontsize(12)

tkw = dict(size=6, width=1.5, labelsize = 22)
ax.tick_params(axis='y', colors=color1, **tkw)
tw.tick_params(axis='y', colors=color2, **tkw)
ax.tick_params(axis='x', **tkw)

ax.set_xlabel('xLabel', fontsize = axis_label_size, labelpad=axis_label_pad)
ax.set_ylabel("yLabel 1", fontsize = axis_label_size, labelpad=axis_label_pad)
tw.set_ylabel("yLabel 2", fontsize = axis_label_size, labelpad = axis_label_size)
fig.tight_layout()
fig.savefig('./figures/dual_bar.svg')


