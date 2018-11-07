# word level one-hot encoding (toy example)

import numpy as np

# initial data
samples = ['This is an example.', 'Word level one hot encoding.']

# Index for the tokens in the samples
token_index = {}

# tokenize and assign unique index to each unique token
for sample in samples:
    for token in sample.split():
        if token not in token_index:
            token_index[token] = len(token_index) + 1

print(token_index)

# Vectorize the sample shape : (len(samples), max_length, max(token_index) + 1)
max_length = 10

results = np.zeros(shape=(len(samples),
                          max_length,
                          len(token_index)+ 1))

for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()) )[:max_length]:
        index = token_index.get(word)
        results[i, j, index] = 1

print(results)