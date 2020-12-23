#!/usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def euclidian_distance(a, b):
    assert a.shape[0] == b.shape[0]

    distance = 0.0
    for i in range(a.shape[0]):
        distance += (a[i] - b[i]) ** 2

    return distance


def find_closest(point, centroids):
    assert point.shape[0] == centroids.shape[1]

    min_index = -1
    min_distance = 1e9
    for i in range(centroids.shape[0]):
        centroid = centroids[i]
        distance = euclidian_distance(point, centroid)
        if distance < min_distance:
            min_distance = distance
            min_index = i

    return min_index


def main():
    # read and reduce data
    athletes = pd.read_csv('athletes.csv')
    bodies = athletes.loc[:,['Height', 'Weight']].to_numpy()

    # K-means: initialize
    K = 5
    m, n = bodies.shape
    centroids = np.zeros((K, n))
    rand_indices = np.random.randint(m, size=K)
    centroids = bodies[rand_indices,:]
    clusters = np.zeros((m, 1))

    for _ in range(1000):

        # step 1: cluster assignment by proximity
        for i in range(m):
            closest_index = find_closest(bodies[i,:], centroids)
            clusters[i] = closest_index

        # step 2: move centroid
        for k in range(K):
            k_points = bodies[(clusters == k)[:,0]]
            if len(k_points) > 0:
                centroids[k] = k_points.sum(axis=0) / k_points.shape[0]

    # textual output
    for k in range(K):
        k_indices = np.argwhere(clusters == k)[:,0]
        print(f'Athletes belonging to Cluster {k+1}:\n')
        print(athletes.iloc[k_indices,:])
        print('\n')

    # plot
    colors = plt.cm.get_cmap('hsv', K+1)
    for k in range(K):
        points = bodies[(clusters == k)[:,0]]
        height_x = points[:,0]
        weight_y = points[:,1]
        color = colors(k)
        plt.scatter(height_x, weight_y, label=k+1, marker='o', color=color)
        plt.scatter(centroids[k,0], centroids[k,1], marker='x', color=color)
    plt.legend()
    plt.xlabel('height [m]')
    plt.ylabel('weight [kg]')
    plt.savefig('clusters.png')
    plt.show()


if __name__ == '__main__':
    main()
