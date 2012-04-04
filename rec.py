import itertools
import pyaudio
import numpy as np
import pickle
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 1024*10
DTYPE = '<i2'

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=chunk)
_min = 0
_max = 0
last = -1
count = 0


def get_data():
    while True:
        data = stream.read(chunk)
        data = np.frombuffer(data, dtype=DTYPE)
        yield data

q = get_data()
iter = 10

sigs = np.zeros((iter,chunk))
for i in range(iter):
    sigs[i] = q.next()

print sigs.shape
pickle.dump(sigs, open("recording.data", "wb"))


stream.close()
p.terminate()

