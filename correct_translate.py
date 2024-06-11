from fasta_functions import *
from translate_seq import *
from to_sense_strand import *

"""
Used to 
1) correct gene sequences such that they are sense strands,
and the transcription direction is from the beginning.
2) convert corrected sequences into amino acid sequences.

"""
def correct(fasta, outpath):
    header = get_fasta_header(fasta)
    gene, mouse = header.split('_', 1)
    gene_seq = ''.join(read_fasta(fasta))
    
    strand_type = None
    transcribe_from = None
    # Sense strand
    if gene_seq[-3:] in ['TAA', 'TAG', 'TGA']:
        strand_type = 'sense'
        transcribe_from = 'beginning'
    if gene_seq[:3] in ['AAT', 'GAT', 'AGT']:
        strand_type = 'sense'
        transcribe_from = 'end'
    
    # Antisesnse strand
    if gene_seq[-3:] in ['ATT', 'ATC', 'ACT']:
        strand_type = 'antisense'
        transcribe_from = 'beginning'
    if gene_seq[:3] in ['TTA', 'CTA', 'TCA']:
        strand_type = 'antisense'
        transcribe_from = 'end'

    if strand_type == 'sense':
        if transcribe_from == 'beginning':
            write_fasta(f"{header}", gene_seq, f"{outpath}/Nucleotide/{mouse}_{gene}.fasta")
            write_fasta(f"{header}", translate_seq(gene_seq), f"{outpath}/Protein/{mouse}_{gene}_Protein.fasta")
        if transcribe_from == 'end':
            write_fasta(f"{header}", gene_seq[::-1], f"{outpath}/Nucleotide/{mouse}_{gene}.fasta")
            write_fasta(f"{header}", translate_seq(gene_seq[::-1]), f"{outpath}/Protein/{mouse}_{gene}_Protein.fasta")
    
    if strand_type == 'antisense':
        sense = to_sense_strand(gene_seq)
        if transcribe_from == 'beginning':
            write_fasta(f"{header}", sense, f"{outpath}/Nucleotide/{mouse}_{gene}.fasta")
            write_fasta(f"{header}", translate_seq(sense), f"{outpath}/Protein/{mouse}_{gene}_Protein.fasta")
        if transcribe_from == 'end':
            write_fasta(f"{header}", sense[::-1], f"{outpath}/Nucleotide/{mouse}_{gene}.fasta")
            write_fasta(f"{header}", translate_seq(sense[::-1]), f"{outpath}/Protein/{mouse}_{gene}_Protein.fasta")

    return
