import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob

import librosa as lr

data_dir = './data/data_test'

audio_files = glob(data_dir + '/*.wav')

print(len(audio_files))
print("processing...")

loudness_list = []
for file_name in audio_files:
    """ iterates over files in the directory, calculating the average loudness for each """
    print(f"Processing: {file_name}")
    audio, sfreq = lr.load(file_name)
    time = np.arange(0, len(audio)) / sfreq
    loudness_list.append(sum(audio) / time[len(time)-1])


fig, ax = plt.subplots()
ax.plot([f"file: {round(n)}" for n in range(
    len(audio_files))], loudness_list)
ax.set(xlabel='File Name', ylabel="Average Loudness")

for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(5)

ax.xaxis.label.set_size(10)
plt.show()

# fig, ax = plt.subplots()
# ax.plot(time, audio)
# ax.set(xlabel='time (s)', ylabel='Sound Amplitude')
# plt.show()
