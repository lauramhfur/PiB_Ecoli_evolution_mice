from Bio import SeqIO

"""
Fasta functions - reading, writing and extracting header of fasta files.
"""

def read_fasta(fasta_file):
    sequence = ''
    with open(fasta_file, 'r') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            sequence += str(record.seq)
    return list(sequence)

def write_fasta(header, sequence, filename):
    with open(filename, 'w') as file:
        file.write('>' + header + '\n')
        for i in range(0, len(sequence), 80):    # Writing sequences in lines of 80 characters
            file.write(sequence[i:i+80] + '\n')
    return

def get_fasta_header(filename):
    with open(filename, "r") as fasta_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
            return record.description
