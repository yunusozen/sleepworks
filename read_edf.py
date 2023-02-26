
import mne
import pandas
import numpy as np
from scipy import signal
import csv

def print_edf_info(edf_file_path='data.edf'):

    data = mne.io.read_raw_edf(edf_file_path)

    print(data.info)
    print(data.info.ch_names)


def read_sleep_stages(edf_file_path='data.edf'):

    annots = mne.read_annotations(edf_file_path, uint16_codec = "utf8").to_data_frame()

    options=['Sleep stage W','Sleep stage N1','Sleep stage N2','Sleep stage N3', 'Sleep stage R']

    df=annots[annots['description'].isin(options)]

    return df['description'].tolist()



def read_sleep_stages_tsv(file_path):

    if not file_path: return None

    annots = []
    with open(tsv_file, 'r', newline='') as f:
        reader = csv.reader(f, delimiter='\t')

        annots = [annot for element in ]
        for row in reader:
            print(satir)

    annots = mne.read_annotations(edf_file_path, uint16_codec = "utf8").to_data_frame()

    options=['Sleep stage W','Sleep stage N1','Sleep stage N2','Sleep stage N3', 'Sleep stage R']

    df=annots[annots['description'].isin(options)]

    return df['description'].tolist()


def read_egg_from_edf(edf_file_path='data.edf', ch = 'Fpz'):

    raw = mne.io.read_raw_edf(edf_file_path, preload=True)
    
    fpz_data, times = raw.get_data(picks=ch, return_times=True)

    return fpz_data[0].tolist()




def resample_eeg_data(eeg_data, old_fs=512, new_fs=100):

    resampling_factor = new_fs / old_fs
    
    new_length = int(len(eeg_data) * resampling_factor)

    # new_times = np.arange(new_length) / new_fs
    
    resampled_eeg_data = signal.resample(eeg_data, new_length)
    
    return resampled_eeg_data.tolist()



def resample_eeg_data_mne(eeg_data, old_fs=512, new_fs=100):

    ch_names = ["EEG"] 
    ch_types = ["eeg"]

    info = mne.create_info(ch_names=ch_names, ch_types=ch_types, sfreq=old_fs)
    
    # Create a raw object from the EEG data and info object
    raw = mne.io.RawArray(np.array([eeg_data]), info)
    
    resampled_raw = raw.resample(sfreq=new_fs)
    
    # Extract the resampled EEG data as a numpy array
    resampled_eeg_data = resampled_raw.get_data()[0]
    
    return resampled_eeg_data.tolist()
