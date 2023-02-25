import numpy as np
from tensorflow.keras.models import load_model
from read_edf import read_egg_from_edf, resample_eeg_data_mne, print_edf_info
from scipy.stats import zscore
import matplotlib.pyplot as plt

def predict_eeg_data(eeg_data, model_path):
    
    model = load_model(model_path)
    
    predicted_labels = []
    
    num_chunks = len(eeg_data) // 3000

    for i in range(num_chunks):
        chunk_start = i * 3000
        chunk_end = (i + 1) * 3000
        
        eeg_chunk = eeg_data[chunk_start:chunk_end]
        
        # Reshape the EEG chunk into a 3D tensor with one channel (for the CNN model)
        eeg_chunk = np.expand_dims(eeg_chunk, axis=-1)
        
        eeg_chunk = np.expand_dims(eeg_chunk, axis=0)
        
        predicted_label = np.argmax(model.predict(eeg_chunk, verbose=0)) 
        
        predicted_labels.append(predicted_label)

    return predicted_labels



if __name__ == "__main__":

    
    print_edf_info(edf_file_path="SC4041E0-PSG.edf")

    
    original_eeg = read_egg_from_edf(edf_file_path="SC4041E0-PSG.edf", ch="EEG Fpz-Cz")

    # eeg_data = resample_eeg_data_mne(original_eeg)
    
    eeg_data =  zscore(original_eeg)

    model_path = "./model_c12022-02-28_1738-21"  
    
    predicted_labels = predict_eeg_data(eeg_data, model_path)
    
    mapping = {3: 0, 2: 1, 1: 2, 4: 3, 0: 4}

    predicted_labels = [mapping[i] for i in predicted_labels]

    print(predicted_labels)
    
    mapping = {'Sleep stage N3': 0, 'Sleep stage N2': 1, 'Sleep stage N1': 2, 'Sleep stage R': 3, 'Sleep stage W': 4}

    plt.plot(predicted_labels)
    plt.yticks(range(len(mapping)), mapping.keys())
    plt.show()
