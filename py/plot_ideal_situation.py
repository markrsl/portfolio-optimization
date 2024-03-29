# coding: UTF-8
# Created by Mark Hsu on 2021/1/8
#
"""
This file ...
"""

import numpy as np
import matplotlib.pyplot as plt


def run():
    data = get_seq_sin()
    data = get_seq_rotation()
    x = data[0]
    y = data[1:]
    # plt.figure(figsize=(10.8, 7.2))
    plt.figure(figsize=(7.2, 4.8))
    plt.rcParams["font.family"] = "Times New Roman"
    plt.xlabel('Day', fontsize=14)
    plt.ylabel('Daily Return', fontsize=14)
    c1 = np.array([222, 222, 54]) / 255
    c2 = np.array([204, 153, 255]) / 255

    colors = ['tab:green', 'tab:blue', 'tab:orange', 'tab:red']
    for i in range(len(y)):
        if i < 2:
            plt.plot(x, y[i], linestyle='dashdot', c=colors[i])
        else:
            plt.plot(x, y[i], c=colors[i])
    l = plt.legend(('Stock A', 'Stock B', 'Equally weighted portfolio', 'Optimal portfolio'), fontsize=14, ncol=2,
               handletextpad=0.2, columnspacing=0.5, handlelength=1.6)
    # l.get_texts()[0].set_color("white")
    plt.tight_layout()
    plt.savefig('./py_output/ideal_situation.pdf')
    plt.show()


def get_seq_sin():
    n = 101
    x = [i + 1 for i in range(101)]
    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n)
    d = np.zeros(n)

    for i in range(len(a)):
        a[i] = np.sin(i / (n - 1) * 2 * np.pi) * 25
        b[i] = a[i] * 4 * -1
        c[i] = (a[i] + b[i]) / 2
    a = a + 100
    b = b + 100
    c = c + 100
    d = d + 100
    return x, a, b, c, d


def get_seq_rotation():
    n = 121
    x = [i + 1 for i in range(101)]
    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n)
    d = np.zeros(n)

    for i in range(len(a)):
        a[i] = np.sin(i / (n - 1) * 2 * np.pi + np.pi) * 50

    a = a[10:111]
    b = b[10:111]
    c = c[10:111]
    d = d[10:111]

    d[0] = a[0]
    d[-1] = a[-1]
    for _x in np.arange(1, len(x) - 1):
        d[_x] = d[0] + (d[-1] - d[0]) * (x[_x] - x[0]) / (x[-1] - x[0])
    b = (d - a) * 4 + a
    c = (a + b) / 2

    a = a + 100
    b = b + 100
    c = c + 100
    d = d + 100
    print(np.min(a))
    print(np.max(b))
    print(np.max(c))
    print(d)
    return x, a, b, c, d


if __name__ == '__main__':
    run()
