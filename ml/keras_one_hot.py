from keras.preprocessing.text import Tokenizer

# initial data
samples = ['This is an example.', 'Word level one hot encoding.']

# create tokenizer, and configure it to take 1000 most common words
tokenizer = Tokenizer(num_words=1000)

# create word index
tokenizer.fit_on_texts(samples)

# string -> list of indices
sequences = tokenizer.texts_to_sequences(samples)

# vectorization
one_hot_results = tokenizer.texts_to_matrix(samples, mode='binary')

word_index = tokenizer.word_index

print(word_index)
print(sequences)
print(one_hot_results)
