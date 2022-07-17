import matplotlib.patches as mpatches
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
from copy import copy

def plot_bar(data, x_labels, show_num=False, barWidth=0.18, figsize=(16,4), dpi=400, lw=1.5,
             colors=['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown']):
    # data = {name0:[data0], name1:[data1], ...}

    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

    bar_x = []
    for _ in data:
        # Set position of bar on X axis
        if len(bar_x) == 0:
            bar_x.append(np.arange(len(x_labels)))
        else:
            new_x = [x + barWidth for x in bar_x[-1]]
            bar_x.append(new_x)

    # Make the plot
    i = 0
    for name in data:
        plt.bar(bar_x[i], data[name], color=colors[i], width=barWidth, edgecolor='black', lw=lw, label=name)
        if show_num:
            for j in range(len(bar_x[i])):
                ax.text(bar_x[i][j]-barWidth/2, data[name][j]+0.02, '{:.2f}'.format(data[name][j]))
        i = i+1

    # plt.xticks([r + barWidth*1.5 for r in range(len(x_labels))], x_labels)

    return plt, ax

def plot_stack_bar(data, x_labels, barWidth=0.35, figsize=(16,4), dpi=400, lw=1.5,
                   colors=['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown'],
                   hatches=['/', 'o', '\/', '*', '/']):
    # data = {'name0': {'part0': [], 'part1': []},
    #         'name1': {'part0': [], 'part1': []} } or

    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)


    bar_x = []
    for _ in data:
        # Set position of bar on X axis
        if len(bar_x) == 0:
            bar_x.append(np.arange(len(x_labels)))
        else:
            new_x = [x + barWidth for x in bar_x[-1]]
            bar_x.append(new_x)

    # Make the plot
    i = 0
    for name in data:
        bar_data = data[name]
        j=0
        for part in bar_data:
            if j == 0:
                plt.bar(bar_x[i], bar_data[part], color ='None', width = barWidth, lw=0.,
                        edgecolor=colors[i], hatch=hatches[j])
                plt.bar(bar_x[i], bar_data[part], color ='None', width = barWidth, lw=lw,
                        edgecolor='k')
                bottom = bar_data[part]
            else:
                plt.bar(bar_x[i], bar_data[part], bottom=bottom, color ='None', width = barWidth, lw=0.,
                        edgecolor=colors[i], hatch=hatches[j])
                plt.bar(bar_x[i], bar_data[part], bottom=bottom, color ='None', width = barWidth, lw=lw,
                        edgecolor='k')
                bottom += bar_data[part]

            if i==0:
                plt.bar(bar_x[i], [0]*len(x_labels), color ='none', width = barWidth,
                        edgecolor='k', label=part, hatch=hatches[j])

            j += 1
        i += 1

    # plt.xticks([r + barWidth*0.5 for r in range(len(x_labels))], x_labels)
    plt.legend(ncol=4)

    return plt, ax

def plot_stack_single_bar(data, x_labels, barWidth=0.35, figsize=(16,4), dpi=400, lw=1.5,
                   colors=['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown'],
                   hatches=['/', 'o', '\/', '*', '/', 'x', '.', '-']):
    # data =  {'part0': [], 'part1': []}

    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)


    bar_x = np.arange(len(x_labels))

    # Make the plot
    bar_data = data
    j=0
    for part in bar_data:
        if isinstance(bar_data[part], list):
            bar_data[part] = np.array(bar_data[part])
        if j == 0:
            plt.bar(bar_x, bar_data[part], color ='None', width = barWidth, lw=0.,
                    edgecolor=colors[j], hatch=hatches[j])
            plt.bar(bar_x, bar_data[part], color ='None', width = barWidth, lw=lw,
                    edgecolor='k')
            bottom = copy(bar_data[part])
        else:
            plt.bar(bar_x, bar_data[part], bottom=bottom, color ='None', width = barWidth, lw=0.,
                    edgecolor=colors[j], hatch=hatches[j])
            plt.bar(bar_x, bar_data[part], bottom=bottom, color ='None', width = barWidth, lw=lw,
                    edgecolor='k')
            bottom += copy(bar_data[part])

        plt.bar(bar_x, [0]*len(x_labels), color ='none', width = barWidth,
                edgecolor=colors[j], label=part, hatch=hatches[j])

        j += 1


    plt.xticks([r for r in range(len(x_labels))], x_labels)
    return plt, ax

def to_percentage(raw_data, x_label):
    totals = []
    for i in range(len(x_label)):
        total = 0
        for part in raw_data:
            total += raw_data[part][i]
        totals.append(total)
    data = {}
    for part in raw_data:
        data[part] = []
        for i in range(len(raw_data[part])):
            num = raw_data[part][i]
            data[part].append(num/totals[i])
    return data
