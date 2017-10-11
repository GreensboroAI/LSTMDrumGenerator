import sys
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

filename = "C:\\Users\\DanJas\\Desktop\\MusicGenerator\\input\\snare.txt"

raw_hits = raw_text = open(filename).read()

print(raw_hits)

chars = chars = sorted(list(set(raw_hits)))

print(chars)

n_chars = len(raw_hits)
n_vocab = len(chars)

seq_length = 16

dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
	seq_in = raw_hits[i:i + seq_length]
	seq_out = raw_hits[i + seq_length]
	dataX.append([char for char in seq_in])
	dataY.append(seq_out)

n_patterns = len(dataX)

print ("Total Patterns: ", n_patterns)

# reshape X to be [samples, time steps, features]
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))

# normalize
#X = X // float(n_vocab)

# one hot encode the output variable
y = np_utils.to_categorical(dataY)

# define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))

# load the network weights
#filename = "C:\\Users\\DanJas\\Desktop\\TextGenerator\\weights-improvement-19-1.9315.hdf5"
#model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')

#---------------------TRAIN---------------------------------------------------------------------
# define the checkpoint
filepath="C:\\Users\\DanJas\\Desktop\\MusicGenerator\\weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]
# fit the model
model.fit(X, y, epochs=20, batch_size=128, callbacks=callbacks_list)

#-----------------------TEST----------------------------------------------------------

# pick a random seed
start = numpy.random.randint(0, len(dataX)-1)
pattern = dataX[0]
print ("Seed:")
print ("\"", ''.join([value for value in pattern]), "\"")
# generate characters
for i in range(200):
	x = numpy.reshape(pattern, (1, len(pattern), 1))
	#x = x / float(n_vocab)
	prediction = model.predict(x, verbose=0)
	index = numpy.argmax(prediction)
	result = index
	seq_in = [value for value in pattern]
	sys.stdout.write(result.tostring().decode())
	pattern.append(index)
	pattern = pattern[1:len(pattern)]
print ("\nDone.")
print(pattern)
