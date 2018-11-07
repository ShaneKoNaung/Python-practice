# word level one-hot hashing (toy example)

import numpy as np

samples = ['This is an example.', 'Word level one hot encoding.']

dimensionality = 1000
max_length = 1000

results = np.zeros(shape=(len(samples),
                         max_length,
                         dimensionality))

for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:max_length]:
        index = abs(hash(word)) % dimensionality
        results[i, j, index] = 1


