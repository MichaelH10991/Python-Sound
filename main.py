import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob

import librosa as lr

data_dir = './data/data_test'

audio_files = glob(data_dir + '/*.wav')

# todo read file props and extract date

print(f"processing {len(audio_files)} files")


def get_props(file_name):
    """gets file properties such as length. This should be converted to a props class"""
    audio, sfreq = lr.load(file_name)
    time = np.arange(0, len(audio)) / sfreq
    return [audio, time]


def helper():
    """Helper function to do stuff"""
    loudness_list = []
    for file_name in audio_files:
        print(f"Processing: {file_name}")
        props = get_props(file_name)
        loudness_list.append(sum(props[0]) / props[1][len(props[1])-1])
    display(audio_files, loudness_list)


def display(audio_files, loudness_list):
    """show the graph"""
    fig, ax = plt.subplots()
    ax.plot([f"file: {round(n)}" for n in range(
        len(audio_files))], loudness_list)
    ax.set(xlabel='File Name', ylabel="Average Loudness")
    plt.show()


helper()
