import itertools
import pyaudio
import wave
import sys
import numpy as np
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
for i in itertools.count():
    data = stream.read(chunk)
    data = np.frombuffer(data, dtype=DTYPE)
    #print data
    #_min = min(_min, data.min())
    #_max = max(_max, data.max())
    #print data.min(), data.max()
    #print np.shape(np.where(data > 20000)[0])[0]
    if np.shape(np.where(data > 20000)[0])[0] > 0 and last  != 0:
	print 'on ' + str(count)
        count += 1
        #print data.max()
        last = 0
    if np.shape(np.where(data < -20000)[0])[0] > 0 and last != 1:
	print 'off ' + str(count)
        count += 1
        #print data.min()
        last = 1

stream.close()
p.terminate()

