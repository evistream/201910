import h5py
import numpy as np
from scipy.signal import butter, filtfilt

from maxone_code.util import SAMPLING_FREQ

class BandPassFilter:
    def __init__(self, lowcut, highcut, fs, order=5):
        fs = SAMPLING_FREQ # Sampling frequency
        #nyq = 0.5 * 0.95 * fs
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        self.b, self.a = butter(order, [low, high], btype='band')

    def filter(self,data):
        y = filtfilt(self.b, self.a, data)
        return y
