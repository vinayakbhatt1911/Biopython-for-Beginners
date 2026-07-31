from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

record=SeqRecord(
    Seq("ATGCGT"),
    id="Human_DNA",
    name="HBB",
    description="Human Hemoglobin Beta Gene"

)
print(record)
SeqIO.write(record,
            "output.fasta",#filename
            "fasta")#file format

"""ID          → Unique identifier
Name        → Short gene/protein name
Description → Complete information
Features    → Biological annotations
Seq         → Actual DNA/RNA/Protein sequence"""