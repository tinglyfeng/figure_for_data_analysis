#%%
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.lines import Line2D
import numpy as np
import os 
import random
random.seed(42)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# figure data
cate_list = ['CLS {}'.format(i) for i in range(1,9)]
cate_data = {cate: [random.randrange(80,95)/100 for _ in range(8)] for cate in cate_list}
metric_list = ["Metric {}".format(i) for i in range(4)]
legend_label = ["Label {}".format(i) for i in range(4)]

# figure parameters
bins = list(range(1,len(cate_list) + 1))
bar_width=0.7
bar_colors =  ['darkviolet', 'coral', 'maroon', 'steelblue']
y_limiter = [0.70,0.95]
subfigure_space = 0.3
xtick_label_rotation = 45
tick_label_size = 15


#%% figure making
fig, axs = plt.subplots(nrows= 1, ncols= len(metric_list), figsize = (16,5))
fig.subplots_adjust(wspace=subfigure_space)

for m_i, metric in enumerate(metric_list):
    # main plot
    axs[m_i].yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    data = [v[m_i] for v in cate_data.values()]
    axs[m_i].bar(bins,data,width=bar_width,color = bar_colors[m_i])
    
    # spine off
    axs[m_i].spines["right"].set_visible(False)
    axs[m_i].spines['top'].set_visible(False)
    axs[m_i].spines["left"].set_visible(False)

    # tick params
    axs[m_i].xaxis.set_tick_params(which='major', bottom=False)
    axs[m_i].yaxis.set_tick_params(which='major', bottom=False)
    axs[m_i].set_yticks(np.linspace(y_limiter[0],y_limiter[1],6)[1:-1])
    axs[m_i].set_xticks(list(map(lambda x: x, range(1,len(data)+1))))
    axs[m_i].set_xticklabels(cate_list,rotation=xtick_label_rotation, rotation_mode="anchor", ha="right")
    axs[m_i].tick_params(axis='y', which='major', labelsize=tick_label_size)
    axs[m_i].tick_params(axis='x', which='major', labelsize=tick_label_size)
    axs[m_i].set_ylim(y_limiter)
    
    # grid setting
    axs[m_i].grid(color='gray', linestyle='-', linewidth=0.3, axis='y', alpha=1)
    axs[m_i].set_axisbelow(True)

# custom legend
custom_lines = []
for i in range(4):
    custom_lines.append(Line2D([0], [0], color=bar_colors[i], lw=6))
fig.legend(custom_lines, metric_list, ncol = len(metric_list),bbox_to_anchor=(0.83, 0.13),fontsize =18)

# adjust layout
plt.tight_layout()
plt.subplots_adjust(left=0.037, right=0.99, bottom=0.25, top=1.035)
plt.savefig('./figures/multi_group_bar.svg')

