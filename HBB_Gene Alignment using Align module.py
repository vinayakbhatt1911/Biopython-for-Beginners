from  Bio import SeqIO
from Bio import Align

records=list(SeqIO.parse(r"C:\Users\DELL\OneDrive\Desktop\Gene sequences fasta\ncbi_dataset\data\gene.fna",
    "fasta"
))

seq1=records[0].seq
seq2=records[1].seq

alingner=Align.PairwiseAligner()
alingner.match_score=1
alingner.mismatch_score=-1
alingner.open_gap_score=-1
alingner.extend_gap_score=-1

alignments=alingner.align(seq1,seq2)
print("Best alignment:",alignments[0])
print("Score:",alignments[0].score)


