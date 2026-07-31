from Bio import SeqIO

for record in SeqIO.parse(
    r"C:\Users\DELL\OneDrive\Desktop\sample.fasta",
    "fasta"
):

    seq = record.seq

    print("ID:", record.id)

    print("Sequence:", seq)

    print("Length:", len(seq))

    print("A:", seq.count("A"))
    print("T:", seq.count("T"))
    print("G:", seq.count("G"))
    print("C:", seq.count("C"))

    gc = seq.count("G") + seq.count("C")
    gc_percent = (gc / len(seq)) * 100

    print("GC Content:", round(gc_percent, 2), "%")

    print("Reverse Complement:")
    print(seq.reverse_complement())

    print("RNA:")
    print(seq.transcribe())

    print("Protein:")
    print(seq.translate())

    print("-" * 50)