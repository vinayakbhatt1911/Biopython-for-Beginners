from Bio import SeqIO

for record in SeqIO.parse(
    r"C:\Users\DELL\OneDrive\Desktop\Gene sequences fasta\ncbi_dataset\data\gene.fna",
    "fasta"
):
    seq=record.seq
    print("ID:",id)
    print("Description:",record.description)
    print("Seq:",seq)
    print("Length:",len(seq))
    gc=seq.count("G")+seq.count("C")
    gc_percent=((gc)/len(seq))*100
    print("GC Content:",round(gc_percent,2),"%")
