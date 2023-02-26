# Automatic Sleep Stage Classification using Deep Learning

## Introduction

This repository provides a deep learning-based approach to automatically classify sleep stages using polysomnography (PSG) signals from European Data Format (EDF, EDF+) files. The model architectures provided consist of Convolutional Neural Network (CNN) and Convolutional LSTM models.

The repository includes Python scripts to extract PSG signals from EDF files, preprocess the signals, train and evaluate the deep learning model, and make predictions on new PSG data. The repository also includes a Jupyter notebook that demonstrates how to use the scripts.


## Data Set

This repository uses Polysomnography (PSG) data obtained during sleep. PSG data is a multi-channel time series data containing EEG, EOG, EMG, and other physiological signals taken during sleep. PSG data is commonly used in the diagnosis and treatment of sleep disorders.


## Requirements

- Python 3.x
- NumPy
- SciPy
- Matplotlib
- MNE-Python
- TensorFlow 2.x

## Usage

To use the repository, follow these steps:

1. Clone the repository:
```
git clone https://github.com/username/repository.git
```

2. Install the required libraries:

This repository was developed using Python 3.x, and pip can be used to install required dependencies. First, install the required libraries using the following command:

```
pip install -r requirements.txt
```

3. Extract PSG signals from EDF files using the extract_psg.py script:
```
python extract_psg.py /edf /psg
```

4. Preprocess the PSG signals using the preprocess_psg.py script:

Data preprocessing involves reading EDF files, signal processing, data scaling, and other preprocessing tasks.

EDF files are read using MNE (a Python library for Magnetoencephalography and Electroencephalography). PSG signals are sampled signals, and this sampling rate is resampled to a sampling rate determined in the preprocessing stage. The data is then scaled and processed.

```
python preprocess_psg.py /psg /prep --sampling_rate 100
```

5. Train the deep learning model using the train_model.py script:

This repository uses various deep learning models such as CNN, CNN-LSTM to predict sleep stages. After the data preprocessing is completed, a model is trained for classifying sleep stages.

```
python train_model.py /prep /train --epochs 50 --batch_size 32
```

6. Evaluate the trained model using the evaluate_model.py script:

After model training is completed, the trained model is used on test data, and its performance is evaluated on test data.

```
python evaluate_model.py /prep /models
```

7. Make predictions on new PSG data using the predict_psg.py script:
```
python predict.py --edf_file <edf_file_path> --model_path <model_path> --output_path <output_path>
```

## License

This project is licensed under the GNU GPL License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [PhysioNet](https://physionet.org) for providing the sleep dataset used in this project.
- MNE-Python development team for providing the EDF file reader and other helpful functions.


## Contributers
[Goksu Ozen](https://github.com/goksuozen43)