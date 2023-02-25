import numpy as np
from tensorflow.keras.models import load_model
from read_edf import read_egg_from_edf, resample_eeg_data_mne

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
        
        predicted_label = np.argmax(model.predict(eeg_chunk))
        
        predicted_labels.append(predicted_label)
    
    return predicted_labels



if __name__ == "__main__":

    original_eeg = read_egg_from_edf()

    eeg_data = resample_eeg_data_mne(original_eeg)
    
    model_path = "./model_c12022-02-28_1738-21"  
    
    predicted_labels = predict_eeg_data(eeg_data, model_path)
    
    print(predicted_labels)
