import mne
import pandas

file = "data.edf"
data = mne.io.read_raw_edf(file)

print(data.info)
print(data.info.ch_names)

annots = mne.read_annotations(file, uint16_codec = "utf8").to_data_frame()

print(annots.head())