
import mne
import pandas
import numpy as np
from scipy import signal

def print_edf_info(edf_file_path='data.edf'):

    data = mne.io.read_raw_edf(edf_file_path)

    print(data.info)
    print(data.info.ch_names)


def read_sleep_stages(edf_file_path='data.edf'):

    annots = mne.read_annotations(edf_file_path, uint16_codec = "utf8").to_data_frame()

    options=['Sleep stage W','Sleep stage N1','Sleep stage N2','Sleep stage N3', 'Sleep stage R']

    df=annots[annots['description'].isin(options)]

    df=df['description'].tolist()

    return df


def read_egg_from_edf(edf_file_path='data.edf', ch = 'Fpz'):

    raw = mne.io.read_raw_edf(edf_file_path, preload=True)
    
    fpz_data, times = raw.get_data(picks=ch, return_times=True)

    return fpz_data[0].tolist()




def resample_eeg(eeg_data, old_fs=512, new_fs=100):

    resampling_factor = new_fs / old_fs
    
    new_length = int(len(eeg_data) * resampling_factor)

    # new_times = np.arange(new_length) / new_fs
    
    resampled_eeg_data = signal.resample(eeg_data, new_length)
    
    return resampled_eeg_data.tolist()


