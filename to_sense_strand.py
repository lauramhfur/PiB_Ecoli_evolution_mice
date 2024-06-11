""" 
Converts an antisense strand to sense strand.
"""

def to_sense_strand(antisense_strand):
    sense_strand = ''
    dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    for i in antisense_strand:
        sense_strand = sense_strand + dict[i]
    return sense_strand
