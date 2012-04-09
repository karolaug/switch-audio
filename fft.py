# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author:
#     Karol Augustin <karol@augustin.pl>
# git repository: http://git.nimitz.pl


import itertools
import pyaudio
import numpy as np
import time
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 1024*8
DTYPE = '<i2'

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=chunk)

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
    #print np.shape(fft)
    #t = np.linspace(0, 44100/2, chunk/2+1)
    ax2.plot(fft)
    f2.canvas.draw()

stream.close()
p.terminate()

