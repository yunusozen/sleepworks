import mne
import pickle
annot = mne.read_annotations("data.edf", uint16_codec = "utf8")
with open('annot.pickle', 'wb') as handle:
    pickle.dump(annot, handle, protocol=pickle.HIGHEST_PROTOCOL)

