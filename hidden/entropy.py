# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 16:34:59 2017

@author: Carmen
"""

# entropy

import numpy as np

def calc_entropy(probs):
    return -sum(p * np.log2(p) for p in probs if p != 0)
    

def get_branch_probs(branch_splits):
    N = sum(sum(np.asarray(branch_splits)))
    probs = np.asarray([sum(np.asarray(branch)) / N for branch in branch_splits])
    return np.asarray(probs)
    #for branch in branch_splits:
    #    print(np.asarray(branch), sum(np.asarray(branch)))
    #return [np.asarray(branch) / sum(np.asarray(branch)) for branch in branch_splits]

def get_branch_entropies(branch_splits):
    #N = sum(sum(np.asarray(branch_splits)))
    #entropies = np.asarray([sum(np.asarray(branch)) / N for branch in branch_splits])
    #return np.asarray([calc_entropy(branch) for branch in branch_splits])
    probs = [np.asarray(branch) / sum(np.asarray(branch)) for branch in branch_splits]
    entropies = np.asarray([calc_entropy(p) for p in probs])
    return entropies
    
def calc_info_gain(probs, entropies, e0 = 1):
    entropy = np.asarray(probs).dot(entropies)
    return entropy, e0 - entropy 
    
def run(branch_splits, label=None, only_gain=True):
    branch_probs = get_branch_probs(branch_splits)
    branch_entropies = get_branch_entropies(branch_splits)
    entropy, info_gain = calc_info_gain(branch_probs, branch_entropies)
    if label:
        print("\nBranch label:", label)
        print("---------------------------")
    if only_gain:
        print("Information gain:     ", info_gain)
    else:
        print("Branch probabilities: ", branch_probs)
        print("Branch entropies:     ", branch_entropies)
        print("Entropy:              ", entropy)
        print("Information gain:     ", info_gain)

    

# %%
#  Example from: https://www.youtube.com/watch?v=APt10bLswro
position = [[3, 1], [1, 1], [0, 2]]
name = [[1,0], [1,1], [1,0], [1,1], [0,1], [0,1]]
college = [[2,0], [1,0], [1,2], [0,1], [0,1]]
age = [[4,0], [0,4]]

run(age, label='age')

# %%
# Example from: https://www.youtube.com/watch?v=l7R9NHqvI0Y
outlook = [[2,3], [4,0], [3,2]]
windy = [[6,2], [3,3]]
humidity = [[3,4], [6,1]]
temperature = [[2,2], [4,2], [3,1]]

run(outlook, 'outlook', only_gain=False)
#run(windy, 'windy')
#run(humidity, 'humidity')
#run(temperature, 'temperature')