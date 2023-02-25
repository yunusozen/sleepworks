import matplotlib.pyplot as plt, pandas as pd, numpy as np
import random
import read_edf

lst=read_edf.read_sleep_stages("data.edf")

mapping = {'Sleep stage N3': 0, 'Sleep stage N2': 1, 'Sleep stage N1': 2, 'Sleep stage R': 3, 'Sleep stage W': 4}

lst = [mapping[i] for i in lst]

 
plt.plot(lst)
plt.yticks(range(len(mapping)), mapping.keys())
plt.show()