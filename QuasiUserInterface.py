import numpy as np
import NN
import random
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
    return algorithm


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


def read_in_data(filename):
    return np.loadtxt(filename)


def feature_search(data, search_algorithm):
    current_set_of_features = []
    for i in size(data, 2) - 1:
        print("On the ", i, "th ", "level of the search tree")
        feature_to_add_at_this_level = []
        current_best_accuracy = 0
        for k in size(data, 2) - 1:
            if k in current_set_of_features:
                pass
            else:
                print("--Considering adding the ", i, " feature")
                accuracy = random.random() # FUNCTION STUB; TODO: FIX
                # if algorithm == 1:
                #     forward_selection()
                # if algorithm == 2:
                #     backwards_elimination()
                # if algorithm == 3:
                #    propinqua()

            if accuracy > current_best_accuracy:
                current_best_accuracy = accuracy * 100
                feature_to_add_at_this_level = k
        current_set_of_features[i] = feature_to_add_at_this_level
        print("On level ", i, " I added feature ", feature_to_add_at_this_level, " to the current set of features used.")


def main():
    filename = input("What file's data will be used?")
    algorithm = select_algorithm()
    if algorithm == "1":
        feature_search(read_in_data(filename, 1))
    if algorithm == "2":
       feature_search(read_in_data(filename, 2))
    if algorithm == "3":
       feature_search(read_in_data(filename, 3))

    return

if __name__ == '__main__':
    main()
