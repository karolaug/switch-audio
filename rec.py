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

