from collections import defaultdict
import gzip

import seaborn as sns
import matplotlib.pyplot as plt

from Bio import SeqIO

recs = SeqIO.parse()
rec = next(recs)
print(rec.id, rec.description, rec.letter_annotations) # quality score of our reads per letter