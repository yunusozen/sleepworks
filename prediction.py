import numpy as np
from tensorflow.keras.models import load_model
from read_edf import read_egg_from_edf, resample_eeg_data_mne, print_edf_info, read_sleep_stages
from scipy.stats import zscore
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def predict_eeg_data(eeg_data, model_path):
    
    print("leneegpred", len(eeg_data))
    model = load_model(model_path)
    
    predicted_labels = []
    
    num_chunks = len(eeg_data) // 3000

    print("num c", num_chunks)


    for i in range(num_chunks):
        chunk_start = i * 3000
        chunk_end = (i + 1) * 3000
        
        eeg_chunk = eeg_data[chunk_start:chunk_end]
        
        # Reshape the EEG chunk into a 3D tensor with one channel (for the CNN model)
        eeg_chunk = np.expand_dims(eeg_chunk, axis=-1)
        
        eeg_chunk = np.expand_dims(eeg_chunk, axis=0)
        
        predicted_label = np.argmax(model.predict(eeg_chunk, verbose=0)) #verbose=0 
        
        predicted_labels.append(predicted_label)

    print("pred l", len(predicted_labels))
    return predicted_labels




if __name__ == "__main__":

    edf_file_path = "data.edf"

    ch_name = "Fpz"
    resample = True
    model_path = "./model_c12022-02-28_1738-21"      
    
    print_edf_info(edf_file_path=edf_file_path)

    
    original_eeg = read_egg_from_edf(edf_file_path=edf_file_path, ch=ch_name)
    print("orig", len(original_eeg))
    if resample:
        eeg_data = resample_eeg_data_mne(original_eeg)
    else:
        eeg_data = original_eeg

    print("eeg",len(eeg_data))
    eeg_data =  zscore(eeg_data)
    print("zscore", len(eeg_data))
  
    
    predicted_labels = predict_eeg_data(eeg_data, model_path)
    
    print("predicted", len(predicted_labels))

    mapping = {3: 0, 2: 1, 1: 2, 4: 3, 0: 4}

    predicted_labels = [mapping[i] for i in predicted_labels]

    print(predicted_labels)
    
    mapping = {'Sleep stage N3': 0, 'Sleep stage N2': 1, 'Sleep stage N1': 2, 'Sleep stage R': 3, 'Sleep stage W': 4}

    plt.plot(predicted_labels)
    plt.yticks(range(len(mapping)), mapping.keys())
    plt.show()


    hypnograms = read_sleep_stages(edf_file_path)

    hypnograms = [mapping[i] for i in hypnograms]

    print(len(hypnograms))
    print(len(predicted_labels))

    cm = confusion_matrix(hypnograms, predicted_labels)

    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()

    plt.show()

