from matplotlib import pyplot as plt
import os
import numpy as np
import matplotlib.pyplot as plt

def horizontal_bar(data, names,putText = True):
    labels = list(data.keys())
    data = np.array(list(data.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('inferno')(
        np.linspace(0.15, 0.85, data.shape[1]))
    fig, ax = plt.subplots(figsize=(10.1, 6))
    plt.subplots_adjust(top=0.9, bottom=0.05, left=0.06, right=0.98, hspace=0, wspace=0)
    plt.margins(0, 0)
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(True)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.set_xlim(0, np.sum(data, axis=1).max())
    for i, (colname, color) in enumerate(zip(names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2
        r, g, b, _ = color
        if putText:
            text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
            for y, (x, c) in enumerate(zip(xcenters, widths)):
                ax.text(x, y, str(int(c)), ha='center', va='center',
                        color=text_color)
    ax.legend(ncol=len(names), bbox_to_anchor=(0.02, 1.01),
              loc='lower left', fontsize=15)

    return fig, ax

# figure data
dis_data ={}
dis_name = ["DIS {}".format(i) for i in range(5)]
dis_meta = []
for i in range(9):
    dis = np.random.choice([i for i in range(100)], 5)
    dis = dis / dis.sum()
    dis_data['CAT {}'.format(i)] = dis
    dis_meta.append(np.random.choice(10,2))

# figure making
fig,ax = horizontal_bar(dis_data,dis_name,putText=False)
ax.get_yticklabels()[8].set_color("red")
ax.tick_params(axis = 'y',labelsize=14)
for y, (mean, num) in enumerate(dis_meta):
    text = "Meta Data 1 : {:d}               Meta Data 2: {:d}" .format(mean,int(num))
    if y == 8:
        ax.text(0.01, y + 0.5, text, ha='left', va='center',
                color='red',fontsize = 12)
    else:
        ax.text(0.01, y+0.5, text, ha='left', va='center',
                color='black',fontsize = 12)

fig.tight_layout()
fig.savefig('./figures/horizontal_stack.svg')

