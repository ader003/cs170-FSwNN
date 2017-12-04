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
    curr_set_of_features = []
    start_time = time.time()
    global_best_acc = 0.0 # global best accuracy
    overall_best_feat_set = [] # global best feature 
    for i in range(1, len(data[0]) - 1): # acts as a multiplier; how many times to run the inner loop
        feat_to_add = 0
        local_best_acc = 0.0 # best recorded accuracy for local levels
        for k in range(1, len(data[0] - 1)): # runs through the features and calculates accuracy based on the current set with the new addition
            if k not in curr_set_of_features:
                # acc = random.random()
                acc = find_accuracy(curr_set_of_features, data, k)
                if acc > local_best_acc:
                    local_best_acc = acc
                    feat_to_add = k
        curr_set_of_features.append(feat_to_add) # appends feature selected by inner for loop
        if local_best_acc > global_best_acc: # check for decrease in accuracy
            global_best_acc = local_best_acc
            overall_best_feat_set = list(curr_set_of_features)
        print("Set of current features (still running): ", curr_set_of_features)
        print("Accuracy at current level: ", local_best_acc)
    end_time = time.time()
    print("Set of features used: ", overall_best_feat_set, "At accuracy: ", global_best_acc, '\n', "Elapsed time: ", end_time - start_time)


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
def find_accuracy(set_of_features, data, test_feature):
    test_feat_set = list(set_of_features)
    test_feat_set.append(test_feature)
    num_correct_classifications = 0
    local_shortest_distance = math.inf
    result = 0 # will be either 1 or 2
    for i in data:
        local_shortest_distance = math.inf
        for h in data:
            if not np.array_equal(h, i): #checks if h and i are not the same row (aka, data point)
                distance = 0
                for j in test_feat_set:
                    distance += pow((i[j] - h[j]), 2.0) # n-space Euclidean distance formula
                if math.sqrt(distance) < local_shortest_distance:
                    local_shortest_distance = math.sqrt(distance)
                    result = h[0] # the result "guessed" by the algorithm
        if result == i[0]:
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
