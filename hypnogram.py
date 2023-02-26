import matplotlib.pyplot as plt, pandas as pd, numpy as np
import random
import read_edf
import argparse



def plot_hypnogram(edf_file_path="data.edf"):

    stages=read_edf.read_sleep_stages(edf_file_path=edf_file_path)

    mapping = {'Sleep stage N3': 0, 'Sleep stage N2': 1, 'Sleep stage N1': 2, 'Sleep stage R': 3, 'Sleep stage W': 4}

    mapped_stages = [mapping[i] for i in stages]

    
    plt.plot(mapped_stages)
    plt.yticks(range(len(mapping)), mapping.keys())
    plt.show()

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='Takes an edf file path and plots hypnogram')
    arg_parser.add_argument('--file_path', type=str, help='edf file path')
    args = arg_parser.parse_args()
    file_path = args.file_path

    plot_hypnogram(edf_file_path=file_path)