# -*- coding: utf-8 -*-

import subprocess
import os.path
import re
import networkx as nx
import numpy as np
from networkx.classes.digraph import DiGraph
from sympy.logic.inference import satisfiable
from sympy.logic.boolalg import to_dnf
from itertools import combinations
import requests
from bs4 import BeautifulSoup


class Buchi(object):
    """
    construct buchi automaton graph
    """

    def __init__(self, task):
        """
        initialization
        :param task: task specified in LTL
        """
        # task specified in LTL
        self.formula = task.formula
        self.subformula = task.subformula
        self.number_of_robots = task.number_of_robots
        # graph of buchi automaton
        self.buchi_graph = DiGraph(type='buchi', init=[], accept=[])

        # minimal length (in terms of number of transitions) between a pair of nodes
        self.min_length = dict()
                
    def construct_buchi_graph(self):
        """
        parse the output of the program ltl2ba and build the buchi automaton
        """
        program = 'online'
        if program == 'offline':
            # directory of the program ltl2ba
            dirname = os.path.dirname(__file__)
            # output of the program ltl2ba
            output = subprocess.check_output(dirname + "/./ltl2ba -f \"" + self.formula + "\"", shell=True).decode(
                "utf-8")
            # find all states/nodes in the buchi automaton
            states = r'\n(\w+):'
            if_fi = r':\n\tif(.*?)fi'

        elif program == 'online':
            para = {
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                'formule': self.formula,
                'convert': 'Convert',
                'image': 'on',
                'descr': 'on',
                'flysimpl': 'on',
                'latsimpl': 'on',
                'sccsimpl': 'on',
                'fjtofj': 'on'
                }
            html_doc = requests.post('http://www.lsv.fr/~gastin/ltl2ba/index.php', data=para)
            # print(html_doc.text)
            output = BeautifulSoup(html_doc.text, 'html.parser').tt.string
            states = r'\n(\w+) :'
            if_fi = r' :(.*?)fi'

        # find all states/nodes in the buchi automaton
        state_re = re.compile(states)
        state_group = re.findall(state_re, output)
        # find initial and accepting states
        init = [s for s in state_group if 'init' in s]
        accept = [s for s in state_group if 'accept' in s]
        # finish the inilization of the graph of the buchi automaton
        self.buchi_graph.graph['init'] = init
        self.buchi_graph.graph['accept'] = accept
        
        order_key = list(self.subformula.keys())
        order_key.sort(reverse=True)
        # for each state/node, find it transition relations
        for state in state_group:
            # add node
            self.buchi_graph.add_node(state)
            # loop over all transitions starting from current state
            state_if_fi = re.findall(state + if_fi, output, re.DOTALL)
            if state_if_fi:
                relation_group = re.findall(r':: (\(.*?\)) -> goto (\w+)\n\t', state_if_fi[0])
                for symbol, next_state in relation_group:
                    sym = symbol
                    # delete edges with multiple subformulas
                    num_pos = 0
                    for sym in symbol.split(' && '):
                        if '!' not in sym:
                            num_pos += 1
                    if num_pos >= 2: continue
                    # whether the edge is feasible in terms of atomic propositions
                    for k in order_key:
                        symbol = symbol.replace('e{0}'.format(k), self.subformula[k])
                    # get the trurh assignment
                    truth_table = self.get_truth_assignment(symbol)
                    # infeasible transition
                    if not truth_table: continue
                    # add edge
                    self.buchi_graph.add_edge(state, next_state, truth=truth_table, symbol=sym)
            else:
                state_skip = re.findall(state + r'(.*?)skip\n', output, re.DOTALL)
                if state_skip:
                    self.buchi_graph.add_edge(state, state, truth='1')

    def get_truth_assignment(self, symbol):
        """
        get one set of truth assignment that makes the symbol true
        :param symbol: logical expression which controls the transition
        :return: a set of truth assignment enables the symbol
        """
        # empty symbol
        if symbol == '(1)':
            return '1'
        # non-empty symbol
        else:
            exp = symbol.replace('||', '|').replace('&&', '&').replace('!', '~')
            exp_dnf = to_dnf(exp).__str__()
            # loop over each clause
            for clause in exp_dnf.split(' | '):
                truth_table = dict()
                clause = clause.strip('(').strip(')')
                literals = clause.split(' & ')
                # loop over each literal
                for literal in literals:
                    if '~' not in literal:
                        truth_table[literal] = True
                    else:
                        truth_table[literal[1:]] = False
                # whether exist a literal with positive and negative version
                if len(literals) != len(truth_table):
                    continue
                else:
                    # exist a robot with two positive literals
                    true_key = [truth.split('_')[1] for truth in truth_table.keys() if truth_table[truth]]
                    if len(true_key) != len(set(true_key)):
                        continue
                    else:
                        # print(clause, truth_table)
                        return truth_table
            return dict()


    def get_minimal_length(self):
        """
        search the shortest path from a node to another, i.e., # of transitions in the path
        :return: 
        """
        # loop over pairs of buchi states
        for head_node in self.buchi_graph.nodes():
            for tail_node in self.buchi_graph.nodes():
                # head_node = tail_node, and tail_node is an accepting state
                if head_node != tail_node and 'accept' in tail_node:
                    try:
                        length, _ = nx.algorithms.single_source_dijkstra(self.buchi_graph,
                                                                         source=head_node, target=tail_node)
                    # couldn't find a path from head_node to tail_node
                    except nx.exception.NetworkXNoPath:
                        length = np.inf
                    self.min_length[(head_node, tail_node)] = length
                # head_node != tail_node and tail_node is an accepting state
                # move 1 step forward to all reachable states of head_node then calculate the minimal length
                elif head_node == tail_node and 'accept' in tail_node:
                    length = np.inf
                    for suc in self.buchi_graph.succ[head_node]:
                        try:
                            len1, _ = nx.algorithms.single_source_dijkstra(self.buchi_graph,
                                                                           source=suc, target=tail_node)
                        except nx.exception.NetworkXNoPath:
                            len1 = np.inf
                        if len1 < length:
                            length = len1 + 1
                    self.min_length[(head_node, tail_node)] = length

    def get_feasible_accepting_state(self):
        """
        get feasbile accepting/final state, or check whether an accepting state is feaasible
        :return:
        """
        accept = self.buchi_graph.graph['accept']
        self.buchi_graph.graph['accept'] = []
        for ac in accept:
            for init in self.buchi_graph.graph['init']:
                if self.min_length[(init, ac)] < np.inf and self.min_length[(ac, ac)] < np.inf:
                    self.buchi_graph.graph['accept'].append(ac)
                    break
        if not self.buchi_graph.graph['accept']:
            print('No feasible accepting states!!!!!!!!! ')
            exit()

    def robot2region(self, symbol):
        """
        pair of robot and corresponding regions in the expression
        :param symbol: logical expression
        :return: robot index : regions
        eg: input:  exp = 'l1_1 & l3_1 & l4_1 & l4_6 | l3_4 & l5_6'
            output: {1: ['l1_1', 'l3_1', 'l4_1'], 4: ['l3_4'], 6: ['l4_6', 'l5_6']}
        """

        robot_region = dict()
        for r in range(self.number_of_robots):
            findall = re.findall(r'(l\d+?_{0})[^0-9]'.format(r + 1), symbol)
            if findall:
                robot_region[str(r + 1)] = findall

        return robot_region
