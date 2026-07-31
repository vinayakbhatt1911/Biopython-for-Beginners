from Bio import SeqIO

for i in SeqIO.parse(
    r"C:\Users\DELL\OneDrive\Desktop\sample.fasta",
    "fasta"
):
    seq=i.seq
    print("Id:",i.id)
    print("Sequence:",i.seq)
    print("Lenght:",(len(i.seq)))
    

    print("A:",seq.count("A"))
    print("T:",seq.count("T"))
    print("G:",seq.count("G"))
    print("C:",seq.count("C"))

    gc=seq.count("G")+seq.count('C')
    gc_percent=(gc/len(seq))*100
    print("GC conntent:",round(gc_percent,2),"%")
