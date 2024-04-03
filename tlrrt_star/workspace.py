# -*- coding: utf-8 -*-

from shapely.geometry import Polygon, Point
import sys


def get_label(x, workspace):
    """
    generating the label of position component
    """
    point = Point(x)
    # whether x lies within obstacle
    for (obs, boundary) in iter(workspace.obs.items()):
        if point.within(boundary):
            return obs

    # whether x lies within regions
    for (region, boundary) in iter(workspace.regions.items()):
        if point.within(boundary):
            return region
    # x lies within unlabeled region
    return ''


class Workspace(object):
    """
    define the workspace where robots reside
    """
    def __init__(self):
        # dimension of the workspace
        self.length = 1
        self.width = 1
        self.workspace = (self.length, self.width)
        # define regions (eg, isosceles right triangle)
        length_of_side = 0.2  # float(sys.argv[1])
        # coordinates of the right angle point
        center = [(0.1, 0.7), (0.7, 0.7), (0.7, 0.3), (0.3, 0.3), (0, 0.1), (0, 0.4)]
        self.regions = {'l1': Polygon([(center[0][0], center[0][1]), (center[0][0] + length_of_side, center[0][1]),
                                       (center[0][0], center[0][1] + length_of_side)]),
                        'l2': Polygon([(center[1][0], center[1][1]), (center[1][0] + length_of_side, center[1][1]),
                                       (center[1][0], center[1][1] + length_of_side)]),
                        'l3': Polygon([(center[2][0], center[2][1]), (center[2][0] + length_of_side, center[2][1]),
                                       (center[2][0], center[2][1] + length_of_side)]),
                        'l4': Polygon([(center[3][0], center[3][1]), (center[3][0] + length_of_side, center[3][1]),
                                       (center[3][0], center[3][1] + length_of_side)]),
                        'l5': Polygon([(center[4][0], center[4][1]), (center[4][0] + length_of_side, center[4][1]),
                                       (center[4][0], center[4][1] + length_of_side)]),
                        'l6': Polygon([(center[5][0], center[5][1]), (center[5][0] + length_of_side, center[5][1]),
                                       (center[5][0], center[5][1] + length_of_side)]),
                        }

        # define obstacles (e.g., rectangle)
        self.obs = {'o1': Polygon([(0.3, 0.0), (0.7, 0.0), (0.7, 0.2), (0.3, 0.2)]),
                    'o2': Polygon([(0.4, 0.7), (0.6, 0.7), (0.6, 1.0), (0.4, 1.0)]),
                    # 'o3': Polygon([(0.55, 0.25), (0.65, 0.25), (0.65, 0.45), (0.55, 0.45)]),
                    # 'o4': Polygon([(0.2, 0.5), (0.9, 0.5), (0.9, 0.6), (0.2, 0.6)]),
                    }


        # define obstacles (e.g., rectangle)
        # self.obs = {'o1': Polygon([(0.3, 0.0), (0.7, 0.0), (0.7, 0.2), (0.3, 0.2)]),
        #             'o2': Polygon([(0.4, 0.7), (0.6, 0.7), (0.6, 1.0), (0.4, 1.0)]),
        #             'o3': Polygon([(0.55, 0.25), (0.65, 0.25), (0.65, 0.45), (0.55, 0.45)]),
        #             'o4': Polygon([(0.2, 0.5), (0.9, 0.5), (0.9, 0.6), (0.2, 0.6)]),
        #             }
        # center = [(0.95*20, 0.95*20)]
        # self.regions = {'l1': Polygon([(center[0][0]/20, center[0][1]/20), ((center[0][0] + 1)/20, center[0][1]/20),
        #                                ((center[0][0]+1)/20, (center[0][1] + 1)/20), (center[0][0]/20, (center[0][1] + 1)/20)])}
        # self.obs = dict()
        # # a = {'o1': (4, 4), 'o2': (14, 4), 'o3': (4, 14), 'o4': (14, 14)}
        # # for k, v in a.items():
        # #     self.obs[k] = Polygon([(v[0]/20, v[1]/20), ((v[0]+2)/20, v[1]/20),
        # #                                              ((v[0]+2)/20, (v[1]+2)/20), (v[0]/20, (v[1]+2)/20)])
        #
        # self.obs['o1'] = Polygon([(0.45, 0.45), (0.55, 0.45), (0.55, 0.55), (0.45, 0.55)])
        # self.obs['o1'] = Polygon([(10/20, 12/20), (12/20, 12/20), (12/20, 14/20), (10/20, 14/20)])
        # self.obs['o2'] = Polygon([(7/20, 4/20), (9/20, 4/20), (9/20, 6/20), (7/20, 6/20)])
        # self.obs['o3'] = Polygon([(0/20, 19.1/20), (17/20, 19.1/20), (17/20, 20/20), (0/20, 20/20)])
        # self.obs['o4'] = Polygon([(8/20, 16/20), (9/20, 16/20), (9/20, 19/20), (8/20, 19/20)])
        # self.obs['o5'] = Polygon([(0/20, 15/20), (17/20, 15/20), (17/20, 15.9/20), (0/20, 15.9/20)])