# -*- coding: utf-8 -*-

from task import Task
from buchi_parse import Buchi
from workspace import Workspace
import datetime
from collections import OrderedDict
import numpy as np
from unbiased_tree import unbiasedTree
from unbiased_construct_unbiased_tree import construction_unbiased_tree, path_via_visibility
from draw_picture import path_plot, path_print
import matplotlib.pyplot as plt
import pyvisgraph as vg
from termcolor import colored
import pickle
import sys

# task
start = datetime.datetime.now()
task = Task()
# with open('data_3_1_1', 'rb') as filehandle:
# with open('data_{0}_{1}_{2}'.format(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])), 'rb') as filehandle:
#     task = pickle.load(filehandle)
# with open('data_{0}_{1}_{2}'.format(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])), 'wb') as filehandle:
# #     store the data as binary data stream
#     pickle.dump(task, filehandle)
# exit()
buchi = Buchi(task)
buchi.construct_buchi_graph()
buchi.get_minimal_length()
buchi.get_feasible_accepting_state()
buchi_graph = buchi.buchi_graph
NBA_time = (datetime.datetime.now() - start).total_seconds()
# print('{0:.4f}'.format(NBA_time))
# buchi.buchi_graph.graph['accept'] = ['accept_all']

# workspace
workspace = Workspace()

# parameters
n_max = 100000000
para = dict()
# lite version, excluding extending and rewiring
para['is_lite'] = False

# minimum distance between any pair of robots
para['threshold'] = task.threshold
para['weight'] = 0.2

# step_size used in function near
para['step_size'] = np.inf # 0.4 * buchi.number_of_robots

cost_path = OrderedDict()

for b_init in buchi_graph.graph['init']:
    # initialization
    opt_cost = (np.inf, 0)
    opt_path_pre = []
    opt_path_suf = []

    # ----------------------------------------------------------------#
    #                            Prefix Part                          #
    # ----------------------------------------------------------------#

    start = datetime.datetime.now()
    init_state = (task.init, b_init)
    init_label = task.init_label
    tree_pre = unbiasedTree(workspace, buchi, init_state, init_label, 'prefix', para)
    print('------------------------------ prefix path --------------------------------')
    # construct the tree for the prefix part
    cost_path_pre = construction_unbiased_tree(tree_pre, n_max)
    if len(tree_pre.goals):
        pre_time = (datetime.datetime.now() - start).total_seconds()
        print('Time for the prefix path: {0:.4f} s'.format(pre_time))
        print('{0} accepting goals found'.format(len(tree_pre.goals)))
    else:
        print('Couldn\'t find the path within predetermined number of iteration')
        break

    # ----------------------------------------------------------------#
    #                            Suffix Part                          #
    # ----------------------------------------------------------------#
    # treat all regions as obstacles
    polys_suf = []
    for poly in workspace.obs.values():
        polys_suf.append([vg.Point(x[0], x[1]) for x in list(poly.exterior.coords)[:-1]])

    for poly in workspace.regions.values():
        polys_suf.append([vg.Point(x[0], x[1]) for x in list(poly.exterior.coords)[:-1]])

    start = datetime.datetime.now()
    goals = list(tree_pre.goals)

    for i in range(1):  # range(len(tree_pre.goals)):
        # set the goal product state of the prefix part as the initial state
        init_state = goals[i]
        init_label = tree_pre.unbiased_tree.nodes[init_state]['label']
        buchi_graph.graph['accept'] = init_state[1]
        tree_suf = unbiasedTree(workspace, buchi, init_state, init_label, 'suffix', para)

        # construct the tree for the suffix part
        cost_path_suf_cand = construction_unbiased_tree(tree_suf, n_max)

        print('-------------- suffix path for {0}-th pre-goal (of {1} in total) --------------'.format(i+1,
                                                                                         len(tree_pre.goals)))
        print('{0}-th pre-goals: {1} accepting goals found'.format(i+1, len(tree_suf.goals)))

        # couldn't find the path within predtermined number of iterations
        if not cost_path_suf_cand:
            del cost_path_pre[i]
            print('delete {0}-th item in cost_path_pre, {1} left'.format(i+1, len(cost_path_pre)))
            continue
        # not trivial suffix path
        if cost_path_suf_cand[0][1]:
            # find the remaining path to close the loop using the visibility graph
            tree_suf.g = vg.VisGraph()
            tree_suf.g.build(polys_suf, status=False)
            for k in range(len(cost_path_suf_cand)):
                cost, path_free = path_via_visibility(tree_suf, cost_path_suf_cand[k][1])
                cost_path_suf_cand[k][0] += cost
                cost_path_suf_cand[k][1] += path_free[1:]

        # order according to cost
        cost_path_suf_cand = OrderedDict(sorted(cost_path_suf_cand.items(), key=lambda x: x[1][0]))
        min_cost = list(cost_path_suf_cand.keys())[0]
        cost_path_suf = cost_path_suf_cand[min_cost]
        # update the best path so far
        if para['weight'] * cost_path_pre[i][0] + (1-para['weight']) * cost_path_suf[0] < \
                para['weight'] * opt_cost[0] + (1-para['weight']) * opt_cost[1]:
            opt_path_pre = cost_path_pre[i][1]  # plan of [(position, buchi)]
            opt_path_suf = cost_path_suf[1]
            opt_cost = [cost_path_pre[i][0], cost_path_suf[0]]  # optimal cost (pre_cost, suf_cost)

    suf_time = (datetime.datetime.now() - start).total_seconds()
    print('Time for the suffix path: {0:.4f} s'.format(suf_time))

    # ----------------------------------------------------------------#
    #                       Prefix + Suffix Part                      #
    # ----------------------------------------------------------------#

    print('------------------------ prefix + suffix path -----------------------------')
    print('t_pre  | t_suf  | t_total | cost')
    print("{0:.4f} | {1:.4f} | {2:.4f}  | {3:.4f}".format(pre_time, suf_time, pre_time + suf_time + NBA_time,
                                                          para['weight'] * opt_cost[0] + (1-para['weight']) * opt_cost[1]))
    print("{0:.4f}  {1:.4f}  {2:.4f}   {3:.4f}".format(pre_time, suf_time, pre_time + suf_time + NBA_time,
                                                          para['weight'] * opt_cost[0] + (1 - para['weight']) *
                                                          opt_cost[1]), opt_cost[0], opt_cost[1])
    #print([(round(p[0][0][0], 2), round(p[0][0][1], 2)) for p in opt_path_pre])
    # draw the picture
    print('------------------------- print the path path -----------------------------')
    print('(. for empty label,', colored('||', 'yellow'), '...', colored('||', 'yellow'), 'for the suffix path)')
    path_print((opt_path_pre, opt_path_suf), workspace, buchi.number_of_robots)
    path_plot((opt_path_pre, opt_path_suf), workspace, buchi.number_of_robots)
    plt.show()
