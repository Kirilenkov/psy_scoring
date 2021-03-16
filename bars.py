import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from matplotlib.lines import Line2D


def bars(visit_1, title, visit_2=None):
    print(visit_1)
    print(visit_2)
    labels = []
    data1 = []
    data2 = []
    color1 = []
    color2 = []
    for i in range(visit_1.__len__()):
        # [:24] если не влазит название шкалы
        labels.append(visit_1.loc[i, 'Шкала'][:24])
        data1.append(visit_1.loc[i, 'Значение'])
        color1.append(visit_1.loc[i, 'color'])
        if visit_2 is not None:
            data2.append(visit_2.loc[i, 'Значение'])
            color2.append(visit_2.loc[i, 'color'])

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots(dpi=250)
    ax.set_ylim([0, 9])
    plt.axhline(y=4, color='b', linestyle='-', zorder=1, alpha=0.5)
    rects1 = ax.bar(x - width/2, data1, width, zorder=2)
    children1 = rects1.get_children()
    children2 = ''
    rects2 = ''
    if visit_2 is not None:
        rects2 = ax.bar(x + width/2, data2, width, zorder=2)
        children2 = rects2.get_children()
    for j, _ in enumerate(children1):
        children1[j].set_color(color1[j])
        children1[j].set_edgecolor('black')
        # children1[j].set_alpha(0.5)
        if visit_2 is not None:
            children2[j].set_color(color2[j])
            children2[j].set_edgecolor('black')
            # children2[j].set_alpha(0.5)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Оценки')
    ax.set_title('Шкалы')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    plt.xticks(rotation=-45, ha='left')
    # Add custom legend
    legend_elements = [Patch(facecolor='#7FB17F', edgecolor='black', label=' Норма',),
                       Patch(facecolor='#7F7FBF', edgecolor='black', label=' Реф. значение'),
                       Patch(facecolor='#FF7F7F', edgecolor='black', label=' Клин. порог')]
    leg = plt.legend(bbox_to_anchor=(1.0, 1.0), loc='upper left', handles=legend_elements,
                     frameon=False, fontsize=8, labelspacing=1.3)

    for patch in leg.get_patches():
        patch.set_height(10)

    def autolabel(rects, shift=None):
        """Attach a text label above each bar in *rects*, displaying its height."""
        sh = 0
        fweight = 'regular'
        if shift is not None:
            sh = shift
            fweight = 'semibold'
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),     # (round(height, 1)),
                        xy=(rect.get_x() + rect.get_width() / 2 + sh, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom',
                        fontsize=8, fontweight=fweight)
    autolabel(rects1)
    if visit_2 is not None:
        autolabel(rects2, shift=0.15)
    fig.tight_layout()
    plt.savefig('/Users/kirill/Desktop/{}.png'.format(title))
    plt.show()


if __name__ == '__main__':
    bars()
