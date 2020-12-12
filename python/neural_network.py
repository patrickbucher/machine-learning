#!/usr/bin/env python3

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def sigmoid(z):
    return 1 / (1 + math.e ** -z)


def add_bias_to_vector(x):
    y = np.ones(x.shape[0]+1)
    y[1:] = x
    return y

def add_bias_to_matrix(x):
    y = np.ones((x.shape[0], x.shape[1]+1))
    y[:,1:] = x
    return y

# read data
training_data = pd.read_csv('train.csv')

# label categories
sport_labels = {
    'Cycling': 0,
    'Swiss Wrestling': 1,
    'Alpine Skiing': 2,
    'Sumo Wrestling': 3,
    'Long-Distance Running': 4,
}
label_sports = {v: k for k, v in sport_labels.items()}
training_data['Label'] = training_data['Sport'].map(sport_labels)

# plot
for label in training_data['Label'].unique():
    entries = training_data[training_data['Label'] == label]
    x = entries['Weight']
    y = entries['Height']
    plt.scatter(x, y, label=label_sports[label])
plt.legend()
plt.xlabel('Weight [kg]')
plt.ylabel('Height [m]')
plt.savefig('train.png')

# extract numerical data
inputs = training_data[['Weight', 'Height']].to_numpy()
labels = training_data['Label'].to_numpy()

# neural network: L=3, K=5
# input   hidden  output
#         (+1)
#         (a2_1)    (  )
# (+1)    (a2_2)    (  )
# (x1)    (a2_3)    (  )
# (x2)    (a2_4)    (  )
#         (a2_5)    (  )
#         (a2_6)


# add bias unit to inputs
rows = inputs.shape[0]
cols = inputs.shape[1] + 1
x = add_bias_to_matrix(inputs)
y = labels
y_one_hot = np.array([(y == l).astype(int) for l in training_data['Label'].unique()]).transpose()

theta1 = np.random.rand(6, 2+1) # 6 outputs, 2+1 inputs
theta1 = theta1 * 2 - 1

theta2 = np.random.rand(5, 6+1) # 5 outputs, 6+1 inputs

for i in range(len(x)):
    pass

    # TODO: try to implement
    a1 = x[i]

    z2 = theta1.dot(a1)
    a2 = sigmoid(z2)

    a2 = add_bias_to_vector(a2)

    z3 = theta2.dot(a2)
    a3 = sigmoid(z3)

    d3 = a3 - y[i]

    d2 = theta2.transpose().dot(d3) * a2 * (1 - a2)
    # TODO: continue...?

# vectorized
a1 = x

z2 = a1.dot(theta1.transpose())
a2 = sigmoid(z2)

a2bias = add_bias_to_matrix(a2)

z3 = a2bias.dot(theta2.transpose())
a3 = sigmoid(z3)

d3 = a3 - y_one_hot

d2 = d3.dot(theta2) * a2bias * (1 - a2bias)
d2 = d2[:,1:]

# no d1: input layer has no error

D2 = a2.transpose().dot(d3)
D1 = a1.transpose().dot(d2)

print(D2, D2.shape)
print(D1, D1.shape)
