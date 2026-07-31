from Bio import SeqIO

for record in SeqIO.parse(
    r"C:\Users\DELL\OneDrive\Desktop\sample.fasta",
    "fasta"
):
    print(record.id)
    print(record.seq)