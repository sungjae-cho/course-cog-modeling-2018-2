# -*- coding: utf-8 -*-
"""
Assignment 10: Implement the examplar model in the textbook (p.23-26)
Textbook: Busemeyer, J. R., & Diederich, A. (2010). Cognitive Modeling. SAGE.
Course: The Fundamentals and Applications of Cognitive Modeling
Author: Sungjae Cho
"""
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

sigma = 3
b = 1
alpha = 0.25
c = 1
beta = 1

def main():
    n_categories = 2
    stimulus1 = 3.0
    stimulus2 = 7.0
    category_feedbacks = np.array([0., 1.])

    max_s1 = 12.0
    max_s2 = 12.0
    min_s1 = 0.0
    min_s2 = 0.0
    m = 121
    s1_detectors = np.zeros((m,m))
    s2_detectors = np.zeros((m,m))
    #weights = np.random.rand(n_categories, m,m)
    weights = np.ones((n_categories, m,m))
    for i_s1_axis in range(0, m):
        for i_s2_axis in range(0, m):
            s1_detectors[i_s1_axis, i_s2_axis] = i_s1_axis * (max_s1 - min_s1) / (m - 1)
            s2_detectors[i_s1_axis, i_s2_axis] = i_s2_axis * (max_s2 - min_s2) / (m - 1)

    activations = get_activations(stimulus1, stimulus2, s1_detectors, s2_detectors)
    category_prob, category_activations = get_category_prob(activations, weights)

    print("Activations:")
    print("Shape: {}".format(activations.shape))
    print(activations)

    print("Category probability:")
    print("Shape: {}".format(category_prob.shape))
    print(category_prob)

    print("Weights before the delta rule update:")
    print(weights)

    weights = delta_rule_update(weights, category_feedbacks, category_activations, activations)

    print("Weights after the delta rule update:")
    print(weights)

    plot_activations(s1_detectors, s2_detectors, activations)

def get_similarity(stimulus1, stimulus2, s1_detector, s2_detector):
    return np.exp(-((s1_detector - stimulus1) / sigma)**2) * np.exp(-((s2_detector - stimulus2) / sigma)**2)

def get_activations(stimulus1, stimulus2, s1_detector, s2_detector):
    similarity = get_similarity(stimulus1, stimulus2, s1_detector, s2_detector)
    return similarity / np.sum(similarity)

def get_category_prob(activations, weights):
    activations = activations.reshape((1,activations.shape[0],activations.shape[1]))
    category_activations = np.sum(weights * activations, axis=(1,2)) # element-wise product and sum over for each category
    exp_category_activations = np.exp(b * category_activations)
    sum_exp_category_activations = np.sum(exp_category_activations)
    category_prob = exp_category_activations / sum_exp_category_activations
    return category_prob, category_activations

def delta_rule_update(weights, category_feedbacks, category_activations, activations):
    weights = weights + alpha * (category_feedbacks - category_activations).reshape((-1,1,1)) * activations.reshape((1,activations.shape[0],activations.shape[1]))
    return weights

def plot_activations(X, Y, Z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)

    # Set axis labels
    ax.set_xlabel('s1')
    ax.set_ylabel('s2')
    ax.set_zlabel('activation', labelpad=20)
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.1E'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

if __name__ == "__main__":
    # execute only if run as a script
    main()
