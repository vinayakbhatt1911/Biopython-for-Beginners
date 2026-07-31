from Bio import SeqIO
records=list(SeqIO.parse(r"C:\Users\DELL\OneDrive\Desktop\Gene sequences fasta\ncbi_dataset\data\gene.fna",
    "fasta")) # HBB gene sequence record object is stored in a list so that we can use list function

seq1=records[0].seq
seq2=records[1].seq

print("Length:",len(seq1))
print("Length:",len(seq2))

if(seq1==seq2):
    print("Same")

else:
   print("Different")

for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        print(f"Position {i+1}: {seq1[i]} -> {seq2[i]}")
        print("-"*20)