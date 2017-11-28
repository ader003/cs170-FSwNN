import heapq as point
import math
import numpy as np


class DataPoint:

        def __init__(self, feature_set):
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


def find_smallest_distance(): #PUT IN DISTANCE FORMULA FOR MULTIPLE FEATURES + ACTUAL MATH
    smallest_distance = 0
    return smallest_distance, most_accurate_feature #returns the smallest distance and most accurate feature


# takes in the set of features
def find_nearest_neighbor(feature_set): #TODO: PUT IN LEGITIMATE MATH
    smallest_distance = 0
    for i in feature_set:
        first_feature = smallest_distance(feature_set)[1]
        for j in feature_set:
            if j is not first_feature:
                distace_to_root += pow(j - i, 2.0)


    smallest_distance = sqrt(distance_to_root)
    return smallest_distance


def expand_children(current_list_of_unsused_features):
    return


def pop_feature(current_list_of_unused_features):
    return

