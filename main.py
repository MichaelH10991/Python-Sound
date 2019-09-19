import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob

import librosa as lr

data_dir = './data/set_a'

audio_files = glob(data_dir + '/*.wav')

print(len(audio_files))

for file_name in audio_files:
    """ iterates over files in the directory, calculating the average loudness for each """
    audio, sfreq = lr.load(file_name)
    time = np.arange(0, len(audio)) / sfreq

    avg_loudness = sum(audio) / time[len(time)-1]
    print(f"avg loudness {avg_loudness}")

fig, ax = plt.subplots()
ax.plot(time, audio)
ax.set(xlabel='time (s)', ylabel='Sound Amplitude')
# plt.show()

zip()
