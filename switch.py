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

