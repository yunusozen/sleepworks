import csv

tsv_file = './12649_7864.tsv'

with open(tsv_file, 'r', newline='') as f:
    reader = csv.reader(f, delimiter='\t')

    annots = [element[2] for element in reader]
    options=['Sleep stage W','Sleep stage N1','Sleep stage N2','Sleep stage N3', 'Sleep stage R', 'Sleep stage ?']
    annots  = [item for item in annots if item in options]
    [print(element) for element in annots]