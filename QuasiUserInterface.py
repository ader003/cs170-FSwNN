import numpy as np
import NN
import random
import copy


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


def forward_selection(data):
    # add features one by one until the most accurate set of features is found
    #print("FIRST LINE OF DATA: ", data[0], '\n') 
    #print("Length of data[0]: ", len(data[0]), '\n') CONSENSUS: Data is read in correctly; len(data[i]) = 11
    current_set_of_features = []
    print("Beginning search.")
    for i in range(0, len(data)):
        print("On the ", i, "th ", "level of the search tree")
        feature_added_at_this_level = 0
        current_best_accuracy = 0.0
        for k in range(0, len(data[i])):
            if k in current_set_of_features:
                pass
            else:
                #print("--Considering adding the ", k, " feature")
                accuracy = random.random() # FUNCTION STUB; TODO: FIX
                #accuracy = find_accuracy(current_set_of_features)

            if accuracy > current_best_accuracy:
                current_best_accuracy = accuracy * 100
                feature_addded_at_this_level = k
        current_set_of_features.append(feature_added_at_this_level)
        print("On level ", i, " I added feature ", feature_added_at_this_level, " to the current set of features used.")
    print("Using features ", current_set_of_features, " accuracy is ", current_best_accuracy, "%")
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
            if find_accuracy(data, testing_set_of_features) > current_best_accuracy:
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
def find_accuracy(set_of_features, data): #TODO: Nearest neighbor
    classifications_correct = 0
    for i in data:
        # TODO : MATH GOES HERE
        result = 0 # THE RESULT GUESSED BY THE ALGORITHM
        if result == data[i]:
            classifications_correct = classifications_correct + 1
    return classifications_correct / len(data)

def main():
    filename = input("Type in the name of the file to test: ")
    algorithm = select_algorithm()
    if algorithm == "1":
        feature_search(read_in_data(filename), 1)
    if algorithm == "2":
       feature_search(read_in_data(filename), 2)
    if algorithm == "3":
       feature_search(read_in_data(filename), 3)

    return

if __name__ == '__main__':
    main()
