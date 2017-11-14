import Node as point
import math
import numpy as np


class DataPoint(point): 

        def __init__(self, one, two, three, four, five, six, seven, eight, nine, ten, eleven, filename, feature_set):
            # setting all the features' values
            self.one = one # the classification: a one or a two
            self.two = two
            self.three = three
            self.four = four
            self.five = five
            self.six = six
            self.seven = seven
            self.eight = eight
            self.nine = nine
            self.ten = ten
            self.eleven = eleven
            self.feature_set = feature_set
            create_float_line_data(filename)


def create_float_line_data(filename):
    line_data = []
    # all the neighbors that needed to have their distances calculated
    feature_data = open(filename, "r")  # r is the mode
    for line in feature_data:
        float_line = [float(x) for x in line.split()]  # list comprehension -- convert string to float
        line_data.append(float_line)
    return line_data


def find_distance(feature_set):

    return distance

