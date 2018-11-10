# word embedding with keras
# This is a tutorial from machinelearningmastery (https://machinelearningmastery.com/use-word-embedding-layers-deep-learning-keras/)
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense
import numpy as np


# define documents
docs = ['Well done!',
		'Good work',
		'Great effort',
		'nice work',
		'Excellent!',
		'Weak',
		'Poor effort!',
		'not good',
		'poor work',
		'Could have done better.']


# define class labels
labels = np.array([1,1,1,1,1,0,0,0,0,0])

# integer encode the document
vocab_size = 50
encoded_docs = [one_hot(d, vocab_size) for d in docs]
print(encoded_docs)

# pad document to a max length of 4 words
max_length = 4
padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')
print(padded_docs)

# define the model 

model = Sequential()
model.add(Embedding(vocab_size, 8, input_length=max_length))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['acc'])

print(model.summary())

model.fit(padded_docs, labels, epochs=200)

loss, accuracy = model.evaluate(padded_docs, labels)
print('Accuracy :', accuracy)
