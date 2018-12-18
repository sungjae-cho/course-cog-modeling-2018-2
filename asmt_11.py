# -*- coding: utf-8 -*-
"""
Assignment 11: Implement the retention model in the textbook (p.43-64)
Textbook: Busemeyer, J. R., & Diederich, A. (2010). Cognitive Modeling. SAGE.
Course: The Fundamentals and Applications of Cognitive Modeling
Author: Sungjae Cho
Specification
- Use the retention model with two parameters (p.50). v
- The two parameters {r, gamma} are the parameters to optimize. v
- Use the maximum-likelihood objective (p.57). v
- But instead of maximing the likilihood, minimizing G^2 (p.59). v
- Use the steepest-descent search (p.62). v
- Use the data in Table 3.1 (p.54). v
"""

import numpy as np
import time
from scipy.special import expit

def get_data():
    last_delay = 10
    delay = np.arange(last_delay + 1, dtype=np.longdouble)
    prob = np.asarray([
        .9538, .9107, .9204, .9029, .8515, .9197,
        .7970, .8228, .8191, .7277, .7276
    ], dtype=np.longdouble)
    return (delay, prob)


class RetentionModel:

    def __init__(self, r = 3, gamma = 0.8):
        self.r = r
        self.gamma = gamma # gamma is between 0 and 1.


    def get_r(self):
        return self.r


    def get_gamma(self):
        return self.gamma


    def retention_model(self, delay):
        prob = 1.0 / (1 + np.exp(- self.r * self.gamma**delay))

        return prob


    def get_likelihood(self, prob):
        likelihood = np.sum(np.log(prob))

        return likelihood


    def g2(self, prob_obsv, prob_pred):
        '''
        prob_obsv : numpy.ndarray.
        prob_pred : prob_pred.
        '''
        log_likelihood_saturated_model = self.get_likelihood(prob_pred)
        log_likelihood_retention_model = self.get_likelihood(prob_obsv)
        log_likelihood_ratio = log_likelihood_saturated_model - log_likelihood_retention_model
        result = 2 * log_likelihood_ratio

        return result


    def get_gradient(self, delay, prob_pred):
        '''
        This arises an overflow error.
        '''

        dr = 2 * np.sum(
            np.power(self.gamma, delay)
            / (1 + np.exp(self.r * np.power(self.gamma, delay)))
        )
        dgamma = 2 * np.sum(
            self.r
            * delay
            * np.power(self.gamma, delay - 1)
            / (1 + np.exp(self.r * np.power(self.gamma, delay)))
        )

        return (dr, dgamma)


    def get_gradient_hint(self, delay, prob_pred):
        m = self.retention_model(delay)
        dr = np.sum(
            len(delay) / self.retention_model(delay) * self.retention_model(delay) * (1 - self.retention_model(delay)) * np.power(self.gamma, delay)
        )
        dgamma = np.sum(
            len(delay) / m * m * (1 - m) * self.r * delay * np.power(self.gamma, delay - 1)
        )

        return (dr, dgamma)


    def operate_gradient_descent(self, learning_rate):
        delay, prob_obsv = get_data()
        prob_pred = self.retention_model(delay)
        (dr, dgamma) = self.get_gradient(delay, prob_pred)
        self.r = self.r - learning_rate * dr
        self.gamma = self.gamma - learning_rate * dgamma


def test():
    # Test for retention_model
    # Data from Table 3.2 (p.57)
    rm1 = RetentionModel(r=3, gamma=0.8)
    if round(rm1.retention_model(0), 4) != 0.9526:
        print("test failed")
    if round(1 - rm1.retention_model(0), 4) != 0.0474:
        print("test failed")
    if round(rm1.retention_model(2), 4) != 0.8721:
        print("test failed")
    if round(1 - rm1.retention_model(2), 4) != 0.1279:
        print("test failed")
    if round(rm1.retention_model(10), 4) != 0.5798:
        print("test failed")
    if round(1 - rm1.retention_model(10), 4) != 0.4202:
        print("test failed")
    print("Test passed! retention_model")


def main():
    '''
    Estimate parameters using gradient descent.
    '''
    #max_iteration = 10000000
    max_iteration = 3300000
    learning_rate = 0.0000001
    print_period = max_iteration // 10

    retention_model = RetentionModel(r = 3, gamma = 0.8)

    start_time = time.time()
    for i in range(1, max_iteration+1):
        retention_model.operate_gradient_descent(learning_rate)
        if i % print_period == 0:
            elapsed_time = time.time() - start_time
            print("Iterataions: {}".format(i))
            min = int(elapsed_time / 60)
            sec = int(elapsed_time % 60)
            print("Optimization time: {} min. {} sec.".format(min, sec))
            print(retention_model.get_r())
            print(retention_model.get_gamma())

    print("Optimization result =====")
    print("Total iterations: {}".format(i))
    print("r = {}".format(retention_model.get_r()))
    print("gamma = {}".format(retention_model.get_gamma()))


if __name__ == "__main__":
    main()
