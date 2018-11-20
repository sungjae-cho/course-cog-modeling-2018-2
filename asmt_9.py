# -*- coding: utf-8 -*-
"""
Assignment 9: Implement the prototype model in the textbook (p.16-23)
Textbook: Busemeyer, J. R., & Diederich, A. (2010). Cognitive Modeling. SAGE.
Course: The Fundamentals and Applications of Cognitive Modeling
Author: Sungjae Cho
"""
import math
import numpy as np

sigma = 3
b = 1
alpha = 0.25
c = 1
beta = 1

def main():

    stimuli = np.array([[3.], [7.]])
    category_feedbacks = np.array([[0.], [1.]])

    X_detectors = [0., 6., 12.]
    Y_detectors = [0., 6., 12.]
    ideal_points = np.array([X_detectors, Y_detectors])

    weights = np.array([[1, 0.02, 0.01, 0.02, 0.01, 1],
                       [0.02, 1, 0.01, 0.01, 1, 0.02]])

    activations = get_activations(stimuli, ideal_points)
    category_prob, category_activations = get_category_prob(activations, weights)

    print("Activations:")
    print(activations)

    print("Category probability:")
    print(category_prob)

    print("Weights before the delta rule update:")
    print(weights)

    weights = delta_rule_update(weights, category_feedbacks, category_activations, activations)

    print("Weights after the delta rule update:")
    print(weights)
    print("If every wieght decreased, the implementation is correct.")

def get_similarity(stimulus, detector):
    return np.exp(-((detector - stimulus) / sigma)**2)

def get_activations(stimuli, ideal_points):
    similarity = get_similarity(stimuli, ideal_points)
    return similarity / np.sum(similarity, axis=1, keepdims=True)

def get_category_prob(activations, weights):
    activations = activations.reshape((-1,1))
    category_activations = np.matmul(weights, activations)
    exp_category_activations = np.exp(b * category_activations)
    sum_exp_category_activations = np.sum(exp_category_activations)
    category_prob = exp_category_activations / sum_exp_category_activations
    return category_prob, category_activations

def delta_rule_update(weights, category_feedbacks, category_activations, activations):
    weights = weights + alpha * (category_feedbacks - category_activations) * activations.reshape((1,-1))
    return weights

if __name__ == "__main__":
    # execute only if run as a script
    main()
