#!/usr/bin/env python3

import numpy as np

# training data
# - height (meters)
# - weight (kilograms)
# - sport
#   - 0: cycling
#   - 1: Swiss wrestling
#   - 2: skiing
#   - 3: sumo wrestling
#   - 4: long-distance runner
training_data = np.array([
    [1.86, 69, 0], # Chris Froome
    [1.75, 60, 0], # Egan Bernal
    [1.83, 71, 0], # Geraint Thomas
    [1.98, 150, 1], # Christian Stucki
    [1.94, 118, 1], # Arnold Forrer
    [1.82, 107, 1], # Joel Wicki
    [1.87, 87, 2], # Daniel Yule
    [1.83, 79, 2], # Marco Odermatt
    [1.73, 85, 2], # Beat Feuz
    [1.87, 175, 3], # Kisenosato Yutaka
    [1.86, 161, 3], # Kakuryū Rikisaburō
    [1.92, 235, 3], # Musashimaru Kōyō
    [1.67, 52, 4], # Eliud Kipchoge
    [1.64, 56, 4], # Haile Gebrselassie
    [1.80, 61, 4], # Galen Rupp
])

print(training_data)
