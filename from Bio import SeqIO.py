from Bio import SeqIO
"""SeqIO.parse() reads sequence records from a biological sequence file and returns them one by one."""

for record in SeqIO.parse(
    r"C:\Users\DELL\OneDrive\Desktop\sample.fasta",
 "fasta"
):
    
    print("ID:",record.id)
    print("Description:",record.description)
    print("Sequence:",record.seq)
    print("Length:",len(record.seq))

"""
Difference Between record.id and record.description

When a FASTA file is read using SeqIO.parse(), each sequence is stored as a record object.

record.id:
- Returns the unique identifier of the sequence.
- Usually contains only the first word after the '>' symbol in the FASTA header.
- Used for quick identification of sequences.

record.description:
- Returns the complete header line of the FASTA record.
- Includes the sequence ID along with any additional information.
- Provides more detailed information about the sequence.

Example FASTA Header:

>Human_HBB Human Hemoglobin Beta Gene

Output:

record.id
Human_HBB

record.description
Human_HBB Human Hemoglobin Beta Gene

Summary:
record.id          -> Short unique sequence identifier
record.description -> Complete FASTA header information
"""