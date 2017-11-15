import numpy as np
import NN.py
import heapq as queue


def select_algorithm():
    # print("For the sake of the assignment, Dr. Keogh has said that there will only be two classifications.", '\n')
    algorithm = input("Select the algorithm you wish to use: " + '\n' +
                      "1. Forward Selection" + '\n' +
                      "2. Backwards Elimination" + '\n' +
                      "3. Propinqua Algorithm" + '\n'
                      )  # "Propinquus" is latin for "near/neighboring"

    # print("Please hold while the data is normalized.")
    # normalize_data()

    if algorithm == "1":
        forward_selection()

    if algorithm == "2":
        backwards_elimination()

    if algorithm == "3":
        propinqua()


def create_feature_sets():  # pass in the number of features, or detect the number of features?
    # TODO: How to manage the overloaded operator?
    # TODO: CREATE TREE OF FEATURE SETS TO EXPLORE

    return queue


def normalize_data():
    return


def forward_selection():
    print("Beginning search.")
    return


def backwards_elimination():
    print("Beginning search.")
    return


def propinqua():
    print("Beginning search.")
    return


def __main__():

    return
