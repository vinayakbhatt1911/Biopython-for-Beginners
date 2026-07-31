from Bio.Seq import Seq
DNA=Seq("ATGGCT")
Protein=DNA.translate()
print(DNA)
print(Protein)