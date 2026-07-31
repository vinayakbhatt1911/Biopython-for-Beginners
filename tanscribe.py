from Bio.Seq import Seq
dna=Seq("ATGGCT")
rna=dna.transcribe()
print(dna)
print(rna)
