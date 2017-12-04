import numpy as np
import math
import random
import copy
import time


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


def normalize_data(data):
    data = (data - np.mean(data)) / np.std(data)
    return data


def forward_selection(data):
    # add features one by one until the most accurate set of features is found
    #print("FIRST LINE OF DATA: ", data[0], '\n') 
    #print("Length of data[0]: ", len(data[0]), '\n') CONSENSUS: Data is read in correctly; len(data[i]) = 11
    current_set_of_features = []
    considered_set_of_features = []
    print("Beginning search.")
    current_best_accuracy = 0.0
    start_time = time.time()
    for i in range(0, len(data)):
        for k in range(1, len(data[i])):
            if k not in current_set_of_features:
                current_set_of_features.append(k)
                considered_set_of_features.append(k)
                # accuracy = find_accuracy(current_set_of_features, data)
                accuracy = random.random()
                current_set_of_features.remove(k)
                if accuracy > current_best_accuracy:
                    current_best_accuracy = accuracy
                    feature_added_at_this_level = k
        if k not in current_set_of_features and k not in considered_set_of_features:
            current_set_of_features.append(feature_added_at_this_level)
        print(current_set_of_features)
    end_time = time.time()
    print("Current Best Accuracy: ", current_best_accuracy, "Using features: ", current_set_of_features, "On level: ", i) # REMOVE
    print("Time elapsed: ", end_time - start_time)
    return


def backwards_elimination(data):
    list_of_removed_features = []
    # begin with all features and delete them one by one, such that same minimum is found
    for i in data[0] in range(1, len(data[0])):
        current_set_of_features.append(i) #place all features in a list
        testing_set_of_features = copy.current_set_of_features
    current_best_accuracy = find_accuracy(data)
    for k in range(0, len(data[0])):
        if k in list_of_removed_features:
            pass
        else:
            testing_set_of_features.remove(h)
            if find_accuracy(testing_set_of_features, data) > current_best_accuracy:
                #if the accuracy without the feature is greater than with it, append the feature to the list detailing the removed features, and remove it from the set of features to check
                list_of_removed_features.append(h)
                current_set_of_features.remove(h)
            else:
                testing_set_of_features = copy.current_set_of_features() #TODO: MAKE MORE EFFICIENT
    print("Using features ", current_set_of_features, " accuracy is ", current_best_accuracy, "%")
    return

def propinqua():

    return


def read_in_data(filename):
    return np.loadtxt(filename)


# https://docs.scipy.org/doc/numpy-1.13.0/reference/index.html
def find_accuracy(set_of_features, data):
    num_correct_classifications = 0
    current_shortest_distance = math.inf
    result = 0 # will be either 1 or 2
    # n-space Euclidean distance formula
    for i in range(0, len(data)):
        for h in range(1, len(data)):
            if h != i:
                distance = 0
                current_shortest_distance = math.inf
                for j in set_of_features:
                    distance += pow((data[i][j] - data[h][j]), 2.0)
                #print("Distance: ", distance)
                if math.sqrt(distance) < current_shortest_distance:
                    current_shortest_distance = math.sqrt(distance)
                    result = data[h][0] # the result "guessed" by the algorithm
                if result == data[i][0]:
                    num_correct_classifications += 1

    return num_correct_classifications / (len(data) - 1)


def main():
    filename = input("Type in the name of the file to test: ")
    algorithm = select_algorithm()
    if algorithm == "1":
        forward_selection(normalize_data(read_in_data(filename)))
    if algorithm == "2":
       backwards_elimination(read_in_data(filename))
    if algorithm == "3":
       feature_search(read_in_data(filename))

    return

if __name__ == '__main__':
    main()
