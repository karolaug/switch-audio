import itertools
import pyaudio
import wave
import sys
import numpy as np
import time
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
DTYPE = '<i2'

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=chunk)

print "* recording"

from matplotlib import pyplot
pyplot.ion()
f = pyplot.figure()
ax = f.gca()
first = np.empty(chunk, dtype=DTYPE)
lines, = ax.plot(first)
f.show()

_min = 0
_max = 0

f2 = pyplot.figure()
ax2 = f2.gca()
f2.show()

for i in itertools.count():
    data = stream.read(chunk)
    data = np.frombuffer(data, dtype=DTYPE)
    print data
    lines.set_ydata(data)
    _min = min(_min, data.min())
    _max = max(_max, data.max())
    ax.set_ylim(_min, _max)
    ax.set_title('%.2f' % time.time())
    f.canvas.draw()

    fft = np.fft.rfft(data)
    ax2.clear()
    ax2.plot(fft)
    f2.canvas.draw()

print "* done recording"

stream.close()
p.terminate()

