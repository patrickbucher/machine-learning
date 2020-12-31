#!/usr/bin/env python

import numpy as np
import pandas as pd


def round_to(array, granularity):
    return (array * 1/granularity).round() * granularity


def main():
    df = pd.read_csv('movies.csv')
    ratings = df.iloc[:,1:7].to_numpy()

    print('Training Data')
    print(df)

    m_movies, n_users = ratings.shape
    n_genres = 5  # made up "genres"

    rated = np.ones((m_movies, n_users))
    not_rated = np.isnan(ratings)
    rated[not_rated] = 0

    genres = np.random.rand(m_movies, n_genres)
    theta = np.random.rand(n_users, n_genres)

    alpha = 1e-3
    iters = int(1e3)
    batch = iters / 10

    print('\nTraining')
    for i in range(iters):
        pred = genres.dot(theta.T)

        diff = pred - ratings
        diff[not_rated] = 0

        genre_grad = diff.dot(theta)
        theta_grad = diff.T.dot(genres)
        
        genres -= alpha * genre_grad
        theta -= alpha * theta_grad

        cost = (1/2) * np.sum(diff ** 2)
        if i % batch == 0:
            print(f'cost = {cost:8.3f}')

    predictions = round_to(genres.dot(theta.T), 0.1)
    predictions[~not_rated] = np.nan
    df.iloc[:,1:7] = predictions
    print('\nPredictions')
    print(df)


if __name__ == '__main__':
    main()
