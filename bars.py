import matplotlib.pyplot as plt
import numpy as np


def bars(visit_1, visit_2):
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
        data2.append(visit_2.loc[i, 'Значение'])
        color2.append(visit_2.loc[i, 'color'])

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, data1, width, label='Визит 1')
    rects2 = ax.bar(x + width/2, data2, width, label='Визит 2')
    children1 = rects1.get_children()
    children2 = rects2.get_children()
    for j, _ in enumerate(children1):
        children1[j].set_color(color1[j])
        children1[j].set_edgecolor('black')
        children1[j].set_alpha(0.5)
        children2[j].set_color(color2[j])
        children2[j].set_edgecolor('black')
        children2[j].set_alpha(0.5)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Оценки')
    ax.set_title('Шкалы')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    plt.xticks(rotation=-45, ha='left')
    # ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.savefig('/Users/kirill/Desktop/test.png')
    plt.show()


if __name__ == '__main__':
    bars()
