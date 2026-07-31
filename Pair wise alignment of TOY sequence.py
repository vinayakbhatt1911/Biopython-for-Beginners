from Bio import Align

aligner=Align.PairwiseAligner()
aligner.match_score=1
aligner.mismatch_score=-1
aligner.open_gap_score=-1
aligner.extend_gap_score=-1

seq1 = "ATGCGT"
seq2 = "ATGAGT"

aligments=aligner.align(seq1,seq2)
print(aligments[0])
print(aligments[0].score)
print(len(aligments))


"""
Why use PairwiseAligner instead of a simple for loop?

1. A for loop can compare nucleotides only when both sequences have the same length.
2. If an insertion or deletion (gap) occurs, a for loop compares the wrong positions.
3. PairwiseAligner automatically introduces gaps and finds the optimal alignment using scoring (match, mismatch, and gap penalties).
4. aligner.align() returns all possible best alignments, so we store it in 'alignments' (plural) instead of 'alignment'. In this example, len(alignments) is 1 because only one optimal alignment exists.
"""

"""
Why do we use alignments[0]?

1. aligner.align(seq1, seq2) does not return a single alignment.
   It returns a collection of all possible optimal alignments.

2. Biopython automatically sorts these alignments by alignment score
   (highest score first).

3. Therefore:
   alignments[0] -> Best alignment (Highest Score)
   alignments[1] -> Second best alignment (if it exists)
   alignments[2] -> Third best alignment (if it exists)

4. In our example, len(alignments) = 1 because there is only one
   optimal alignment with the highest score.
"""