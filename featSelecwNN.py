import numpy as np
import math
import random
import time


def select_algorithm():
    algorithm = input("Select the algorithm you wish to use: " + '\n' +
                      "1. Forward Selection" + '\n' +
                      "2. Backwards Elimination" + '\n' +
                      "3. Propinqua Algorithm" + '\n'
                      )  # "Propinquus" is latin for "near/neighboring"

    # print("Please hold while the data is normalized.")
    # normalize_data()
    return algorithm


def normalize_data(data):
    print("Please hold while data is normalized.")
    data = (data - np.mean(data)) / np.std(data)
    print("... Done!")
    return data


def forward_selection(data):
    curr_set_of_features = []
    global_best_acc = 0.0 # global best accuracy
    overall_best_feat_set = [] # global best feature
    start_time = time.time()
    for i in range(1, len(data[0])): # acts as a multiplier; how many times to run the inner loop
        feat_to_add = 0
        local_best_acc = 0.0 # best recorded accuracy for local levels
        for k in range(1, len(data[0])): # runs through the features and calculates accuracy based on the current set with the new addition
            if k not in curr_set_of_features:
                print("--Considering adding feature ", k)
                acc = find_accuracy(curr_set_of_features, data, k, 1)
                if acc > local_best_acc:
                    local_best_acc = acc
                    feat_to_add = k
        curr_set_of_features.append(feat_to_add) # appends feature selected by inner for loop
        print("On level ", i, " feature ", feat_to_add, " was added to the current set")
        print("With ", len(curr_set_of_features), " features, the accuracy is: ", local_best_acc * 100, "%")
        if local_best_acc >= global_best_acc: # check for decrease in accuracy
            global_best_acc = local_best_acc
            overall_best_feat_set = list(curr_set_of_features)
    end_time = time.time()
    print("Set of features used: ", overall_best_feat_set, "at accuracy: ", global_best_acc * 100, '\n', "Elapsed time: ", end_time - start_time)
    return


def backwards_elimination(data):
    global_best_acc = 0.0 # global best accuracy
    overall_best_feat_set = []
    curr_set_of_features = [i for i in range(1, len(data[0]))]
    start_time = time.time()
    for i in range(1, len(data[0]) - 1):
        feat_to_pop = 0
        local_best_acc = 0.0 # best recorded accuracy for local levels
        for k in range(1, len(data[0]) - 1):
            if k in curr_set_of_features:
                print("--Considering adding feature ", k)
                acc = find_accuracy(curr_set_of_features, data, k, 2)
                if acc > local_best_acc:
                    local_best_acc = acc
                    feat_to_pop = k
        if feat_to_pop in curr_set_of_features: 
            curr_set_of_features.remove(feat_to_pop) # removes feature selected by inner for loop
            print("On level ", i, " feature ", feat_to_pop, " was removed from the current set")
            print("With ", len(curr_set_of_features), " features, the accuracy is: ", local_best_acc * 100, "%")
        if local_best_acc >= global_best_acc: # check for decrease in accuracy
            global_best_acc = local_best_acc
            overall_best_feat_set = list(curr_set_of_features)
    end_time = time.time()
    print("Set of features used: ", overall_best_feat_set, "At accuracy: ", global_best_acc * 100, '\n', "Elapsed time: ", end_time - start_time)
    return

def propinqua(data): #forward selection with pruning
    print("You have selected the custom Propinqua Algorithm. Please note that only the best feature tests will be printed.")
    curr_set_of_features = []
    global_best_acc = 0.0 # global best accuracy
    overall_best_feat_set = [] # global best feature
    start_time = time.time()
    for i in range(1, len(data[0])): # acts as a multiplier; how many times to run the inner loop
        feat_to_add = 0
        local_best_acc = 0.0 # best recorded accuracy for local levels
        for k in range(1, len(data[0])): # runs through the features and calculates accuracy based on the current set with the new addition
            if k not in curr_set_of_features:
                acc = find_accuracy(curr_set_of_features, data, k, 1)
                if acc > local_best_acc:
                    local_best_acc = acc
                    feat_to_add = k
        if local_best_acc <= global_best_acc:
            if k == len(data[0]) - 1: # if the addition of any feature not yet included results in a decrease in accuracy, the best set has been found; break out of loop
                break
        if local_best_acc > global_best_acc: # check for decrease in accuracy
            curr_set_of_features.append(feat_to_add) # appends feature selected by inner for loop
            global_best_acc = local_best_acc
            overall_best_feat_set = list(curr_set_of_features)
        print("Set of current features (algorithm still in progress): ", curr_set_of_features)
        print("Accuracy at current level: ", local_best_acc * 100, "%")
    end_time = time.time()
    print("Set of features used: ", overall_best_feat_set, "At accuracy: ", global_best_acc * 100, "%", '\n', "Elapsed time: ", end_time - start_time)
    return


def read_in_data(filename):
    return np.loadtxt(filename)


def find_accuracy(set_of_features, data, test_feature, algorithm):
    test_feat_set = list(set_of_features)
    if algorithm == 1: #forward selection; Forward's Propinqua
        test_feat_set.append(test_feature)
    if algorithm == 2: #backwards elimination
        test_feat_set.remove(test_feature)
    num_correct_classifications = 0
    local_shortest_distance = math.inf
    result = 0 # will be either 1 or 2
    for i in data:
        local_shortest_distance = math.inf
        for h in data:
            if not np.array_equal(h, i): #checks if h and i are not the same row
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
       backwards_elimination(normalize_data(read_in_data(filename)))
    if algorithm == "3":
       propinqua(normalize_data(read_in_data(filename)))
    return

if __name__ == '__main__':
    main()
