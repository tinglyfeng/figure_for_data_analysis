#%%
import os 
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec


def mse(x):
    return x ** 2
def mae(x):
    return np.abs(x)

def smooth_l1(x,beta):
    mask = (np.abs(x) < beta)
    y = np.zeros_like(x)
    y[mask] = 0.5 * (x[mask]**2) / beta
    y[~mask] = np.abs(x[~mask]) - 0.5 * beta
    return y


#%%
# figure data
x = np.arange(-1,1,0.0001)
smooth_betas = [0.2, 0.4, 0.6, 0.8]
figure_list = ['MAE', 'MSE', 'Smooth L1']

# figure_params  
smooth_colors = ['darkviolet', 'coral', 'maroon', 'steelblue']
main_line_color = 'darkviolet'
linewidth = 4
x_axis_label_fontsize = 28
y_axis_label_fontsize = 28
x_labelpad = 10
y_labelpad = 10
tkw = dict(size=6, width=1.5, labelsize = 22)

# figure making 
fig = plt.figure(figsize=(24,13))
gs = gridspec.GridSpec(7, 4, figure= fig)
gs.update(wspace=0.5, hspace = 5.7)
ax1 = plt.subplot(gs[0:3, :2], )
ax2 = plt.subplot(gs[0:3, 2:])
ax3 = plt.subplot(gs[3:, 0:4])
axs = [ax1, ax2, ax3]

for i, figure  in enumerate(figure_list):
    axs[i].grid(visible=True, axis = 'y', which='both')
    if figure == "MAE":
        axs[i].set_ylabel("MAE Loss",fontsize= y_axis_label_fontsize, labelpad=y_labelpad)
        axs[i].plot(x, mae(x), color = main_line_color, linewidth = linewidth)
    elif figure == "MSE":
        axs[i].set_ylabel("MSE Loss",fontsize= y_axis_label_fontsize, labelpad=y_labelpad)
        axs[i].plot(x, mse(x), color = main_line_color, linewidth = linewidth)
    elif figure == "Smooth L1":
        axs[i].set_ylabel("Smooth L1 Loss",fontsize= y_axis_label_fontsize, labelpad=y_labelpad)
        for j,beta in enumerate(smooth_betas):
            axs[i].plot(x, smooth_l1(x,beta), color = smooth_colors[j], linewidth = linewidth)
        legends = ['$\\beta = {}$'.format(str(beta)) for beta in smooth_betas]
        axs[i].legend(legends,prop={'size': 32})

    axs[i].set_xlabel("Distance",fontsize= x_axis_label_fontsize,labelpad = x_labelpad)    
    axs[i].tick_params(axis='both', **tkw)
fig.subplots_adjust(
                    wspace=0.3,
            )
fig.tight_layout()
fig.savefig('./figures/multi_figure_layout.svg')
