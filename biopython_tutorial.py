# Senuri Piyatissa (following Lana Caldarevic tutorial (https://www.youtube.com/watch?v=ocA2IMe7dpA))
# 05.07.2022
# using BioPython to analyze sequences

from Bio import SeqIO

# setup an empty list
sequences = []

for seq_record in SeqIO.parse("ls_orchid.fasta","fasta"):
    # add sequences to list one by one
    sequences.append(seq_record.seq)
    # print details of each record
    print(seq_record.id)
    print(len(seq_record))
    print(seq_record.seq)

