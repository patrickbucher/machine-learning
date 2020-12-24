#!/usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def normalize(arr):
    cols = arr.shape[1]
    for c in range(cols):
        arr[:,c] = (arr[:,c] - arr[:,c].mean()) / arr[:,c].std()
    return arr

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


def calculate_distortion(points, clusters, centroids):
    total_distances = 0.0
    m = len(points)
    for i in range(m):
        point = points[i] 
        point_cluster = clusters[i][0]
        centroid = centroids[point_cluster]
        total_distances += euclidian_distance(point, centroid)
    return total_distances / m


def main():
    # read and reduce data
    athletes = pd.read_csv('athletes.csv')
    bodies = athletes.loc[:,['Height', 'Weight']].to_numpy()
    bodies = normalize(bodies)

    # K-means: initialize
    K = 5
    initializations = 20
    iterations = 1000
    m, n = bodies.shape

    lowest_cost = 1e9
    best_centroids = None
    best_clusters = None

    for _ in range(initializations):

        # random initialization
        rand_indices = np.random.randint(m, size=K)
        centroids = np.zeros((K, n))
        centroids = bodies[rand_indices,:]
        clusters = np.zeros((m, 1), dtype=int)

        for _ in range(iterations):

            # step 1: cluster assignment by proximity
            for i in range(m):
                closest_index = find_closest(bodies[i,:], centroids)
                clusters[i] = closest_index

            # step 2: move centroid
            for k in range(K):
                k_points = bodies[(clusters == k)[:,0]]
                if len(k_points) > 0:
                    centroids[k] = k_points.sum(axis=0) / k_points.shape[0]

        cost = calculate_distortion(bodies, clusters, centroids)
        if cost < lowest_cost:
            lowest_cost = cost
            best_centroids = centroids
            best_clusters = clusters

    centroids = best_centroids
    clusters = best_clusters

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
        plt.scatter(centroids[k,0], centroids[k,1], marker='x', s=128, color=color)
    plt.legend()
    plt.xlabel('height [m]')
    plt.ylabel('weight [kg]')
    plt.savefig('clusters.svg', dpi=300)
    plt.savefig('clusters.png', dpi=300)
    plt.show()


if __name__ == '__main__':
    main()
