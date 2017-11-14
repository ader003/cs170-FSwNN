import Node as point
import math
import numpy

class DataPoint(point): 

        def __init__(self, one, two, three, four, five, six, seven, eight, nine, ten):
            # setting all the features' values
            self.one = one
            self.two = two
            self.three = three
            self.four = four
            self.five = five
            self.six = six
            self.seven = seven
            self.eight = eight
            self.nine = nine
            self.ten = ten

def create_queue_of_data_points(filename):
    # all the neighbors that needed to have their distances calculated
    queue = []
    return queue

def ten_feature_distance(node_a, node_b):
    distance = math.sqrt(pow((node_a.one - node_b.one), 2.0) +
                    (pow((node_a.two - node_b.two), 2.0) +
                     (pow((node_a.three - node_b.three), 2.0) +
                      (pow((node_a.four - node_b.four), 2.0) +
                       (pow((node_a.five - node_b.five), 2.0) +
                        (pow((node_a.six - node_b.six), 2.0) +
                         (pow((node_a.seven - node_b.seven), 2.0) +
                          (pow((node_a.eight - node_b.eight), 2.0) +
                           (pow((node_a.nine - node_b.nine), 2.0) +
                            (pow((node_a.ten - node_b.ten), 2.0))
    return distance

