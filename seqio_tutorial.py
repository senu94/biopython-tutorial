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

# counting bases can be done with overlap considered or not
from Bio.Seq import Seq
sequence = Seq("AAGGGGAATCCTATGTTAACCCGGG")
# overlapping count
sequence.count("GG")
sequence.count_overlap("GG")

# calculate the GC content
from Bio.SeqUtils import GC
GC(sequence)

# get template strand from coding strand
coding_strand = Seq("AATTTGGGCCCATGCATGCGTAGGGGAAAA")
template_strand = coding_strand.reverse_complement()

# for transcribing
messenger_rna = coding_strand.transcribe()

# you could also back transcribe the messenger rna in to coding dna
coding_strand_from_rna = messenger_rna.back_transcribe()

# you could translate either the messenger rna or the coding strand in to amino acids
messenger_rna.translate()
coding_strand.translate()


