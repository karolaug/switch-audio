import numpy as np
import pylab as py
import pickle



sigs = pickle.load(open("recording.data", "rb" ))
py.plot(sigs[5])
py.show()

