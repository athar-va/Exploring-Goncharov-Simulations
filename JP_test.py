import math
import numpy as np
from matplotlib import pyplot as plt

def fetch_norm_dist(shape, mu=0, sigma=1):
    return np.random.normal(mu, sigma, shape)

def norms(vector):
    return vector / np.linalg.norm(vector, 2)

def pair_dist_print(array_of_points):
    for i in range(len(array_of_points)):
        for j in range(i, len(array_of_points)):
            if i != j:
                print(f'Dist ({i}, {j}) = {np.linalg.norm(array_of_points[i] - array_of_points[j])}')

def fetch_gradient(points, i, penalty_factor):
    total = np.zeros(len(points[i]))

    for j in range(len(points)):
        if i == j:
            continue
        x_ij = points[i] - points[j]
        total = total - 2 * (x_ij) / math.pow(np.linalg.norm(x_ij, 2), 4)

    total = total + penalty_factor * (np.linalg.norm(points[i]) - 1) * points[i]
    return total


def minimize(points, alpha, iterations, gradient=fetch_gradient):
    new_points = []

    for penalty_factor in range(1, 50):

        for iteration in range(iterations):

            for i in range(len(points)):
                delta = gradient(points, i, penalty_factor)
                new_p = points[i] - alpha * delta

                new_points.append(new_p)

            points = new_points
            new_points = []

    return points


dimensions = 3
n = 3
points = [norms(fetch_norm_dist((dimensions))) for i in range(n)]

points = minimize(points, 0.0002, 3000)
print(points)
pair_dist_print(points)
