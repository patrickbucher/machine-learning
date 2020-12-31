#!/usr/bin/env python

import numpy as np
import pandas as pd


def round_to(arr, granularity):
    return (arr * 1/granularity).round() * granularity

movies = pd.read_csv('movies.csv')
ratings = movies.iloc[:,1:].to_numpy()

m, n = ratings.shape

# in (i,j) matrix, user i rated movie j
rated = np.ones((m, n))
rated[np.isnan(ratings)] = 0

xs = np.random.rand(m, 3) # two "categories", by movie
thetas = np.random.rand(n, 3) # no additional bias unit, by user
thetas[:,0] = 1

alpha = 1e-4
l = 1e-12
ys = ratings
for i in range(500_000):
    pred = xs.dot(thetas.transpose())
    pred[np.isnan(ratings)] = 0

    diff = pred - ys
    diff[np.isnan(ratings)] = 0

    xs_grad = diff.dot(thetas) + l * xs
    thetas_grad = diff.transpose().dot(xs) + l * thetas
    
    xs -= alpha * xs_grad
    thetas -= alpha * thetas_grad

    cost = (1/2) * (diff ** 2).sum() + (l/2) * (thetas ** 2).sum() + (l/2) * (xs ** 2).sum()
    if cost < 1e-12:
        print(f'finished with cost {cost} after {i} iterations')
        break
    last_cost = cost

predictions = xs.dot(thetas.transpose())
predictions[rated == 1] = 0
predictions = round_to(predictions, 0.5)
print(predictions)
