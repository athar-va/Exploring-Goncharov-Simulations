import numpy as np

def fetch_gradient(X):
    # Finds the gradient of the function to be maximised with respect to X
    gradient = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(i + 1, X.shape[0]):
            distance = np.linalg.norm(X[i] - X[j])
            if distance == 0:
                continue
            gradient[i] += 2 * (X[i] - X[j]) / distance
            gradient[j] += 2 * (X[j] - X[i]) / distance
    return gradient


def grad_descent(X, lr=0.01, iterations=7000):
    # Performs Next = Current + lr*gradient(objective_fucntion)
    for i in range(iterations):
        grad = fetch_gradient(X)
        X += lr * grad
        X /= np.linalg.norm(X, axis=1)[:, np.newaxis]

    return X


def run_optimizer(d, n):
    # Initialize the points randomly on the unit sphere
    random_points = np.random.normal(size=(n, d))

    # Normalize the points for them to lie on a unit sphere
    random_points /= np.linalg.norm(random_points, axis=1)[:, np.newaxis]

    # Find the optimal location of the points
    farthest_points = grad_descent(random_points)

    return farthest_points

def pair_dist_print(array_of_points):
    dist={}
    for i in range(len(array_of_points)):
        for j in range(i, len(array_of_points)):
            if i != j:
                val=np.linalg.norm(array_of_points[i] - array_of_points[j])
                dist[tuple([i,j])] = val
                # print(f'Dist ({i}, {j}) = {val}')

    return dist