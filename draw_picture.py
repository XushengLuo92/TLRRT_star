# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from workspace import get_label
from termcolor import colored


def workspace_plot(workspace, r_or_o, id_r_or_o, ax):
    """
    plot the workspace
    :param workspace: workspace
    :param r_or_o: regions or obstacles
    :param id_r_or_o: indicators for regions of obstacles
    :param ax: figure axis
    :return: figure
    """
    ax.set_xlim((0, workspace[0]))
    ax.set_ylim((0, workspace[1]))
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(b=True, which='major', color='k', linestyle='--')
    for key in r_or_o.keys():
        color = '0.75' if id_r_or_o != 'region' else 'c'
        x = []
        y = []
        patches = []
        for point in list(r_or_o[key].exterior.coords)[:-1]:
            x.append(point[0])
            y.append(point[1])
        polygon = Polygon(np.column_stack((x, y)), True)
        patches.append(polygon)
        p = PatchCollection(patches, facecolors=color, edgecolors=color)
        ax.add_collection(p)
        ax.text(np.mean(x), np.mean(y), r'${}_{{{}}}$'.format(key[0], key[1:]), fontsize=16)


def path_plot(path, workspace, number_of_robots):
    """
    plot the path
    :param path: found path
    :param workspace: workspace
    :param number_of_robots:
    :return: figure
    """

    for n in range(number_of_robots):
        ax = plt.figure(n).gca()
        workspace_plot(workspace.workspace, workspace.regions, 'region', ax)
        workspace_plot(workspace.workspace, workspace.obs, 'obs', ax)

        # prefix path
        x_pre = np.asarray([point[0][n][0] for point in path[0]])
        y_pre = np.asarray([point[0][n][1] for point in path[0]])
        pre = plt.quiver(x_pre[:-1], y_pre[:-1], x_pre[1:] - x_pre[:-1], y_pre[1:] - y_pre[:-1], color='r',
                         scale_units='xy', angles='xy', scale=1, label='prefix path')

        # suffix path
        x_suf = np.asarray([point[0][n][0] for point in path[1]])
        y_suf = np.asarray([point[0][n][1] for point in path[1]])
        suf = plt.quiver(x_suf[:-1], y_suf[:-1], x_suf[1:] - x_suf[:-1], y_suf[1:] - y_suf[:-1], color='g',
                         scale_units='xy', angles='xy', scale=1, label='suffix path')

        plt.legend(handles=[pre, suf])
        plt.savefig('img/path{0}.png'.format(n+1), bbox_inches='tight', dpi=600)


def path_print(path, workspace, number_of_robots):
    """
    print the path
    :param path: found path
    :param workspace: workspace
    :param number_of_robots:
    :return: printed path of traversed regions. points with empty label are depicted as dots
    """
    for n in range(number_of_robots):
        print('robot {0:<2}: '.format(n+1), end='')
        # prefix path, a path of x's or y's of a robot
        x_pre = [point[0][n][0] for point in path[0]]
        y_pre = [point[0][n][1] for point in path[0]]
        path_print_helper(x_pre, y_pre, workspace)
        # suffix path
        x_suf = [point[0][n][0] for point in path[1]]
        y_suf = [point[0][n][1] for point in path[1]]
        path_print_helper(x_suf, y_suf, workspace)
        print('')


def path_print_helper(x, y, workspace):
    """
    help to print the path
    :param x: a path of x's of a robot throughout the run
    :param y: a path of y's of a robot throughout the run
    :param workspace: workspace
    :return: printed path of traversed regions. points with empty label are depicted as dots
    """
    for i in range(len(x)):
        label = get_label((x[i], y[i]), workspace)
        label = ' .' if not label else label
        print(label + ' --> ', end='')
    print(colored('|| ', 'yellow'), end='')
