#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


sport_labels = {
    'Cycling': 0,
    'Swiss Wrestling': 1,
    'Alpine Skiing': 2,
    'Sumo Wrestling': 3,
    'Long-Distance Running': 4,
}
label_sports = {v: k for k, v in sport_labels.items()}
training_data = pd.read_csv('train.csv')

training_data['Label'] = training_data['Sport'].map(sport_labels)
print(training_data)

for label in training_data['Label'].unique():
    entries = training_data[training_data['Label'] == label]
    x = entries['Weight']
    y = entries['Height']
    plt.scatter(x, y, label=label_sports[label])
plt.legend()

plt.savefig('train.png')
