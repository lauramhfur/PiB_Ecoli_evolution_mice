"""
Translates nucleotide sequence into its corresponding amino acid sequence, 
accounting for multiple possible start codons in E. coli.
"""

def translate_seq(dna_strand):
    codons = []
    translated_seq = ''

    for i in range(0, len(dna_strand), 3):
        codon = dna_strand[i:i+3]
        if i == 0:
            if codon in ['ATG', 'GTG', 'TTG']:          # The possible start codons in E. coli.
                translated_seq = translated_seq + 'M'
                continue

        if len(codon) == 3:
            codons.append(codon)
        else:
            codons.append(i)

    codon_map = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
                 'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
                 'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
                 'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
                 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
                 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
                 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
                 'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
                 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                 'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
                 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
                 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
                 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
                 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
                 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}

    for codon in codons:
        if codon in codon_map:
            translated_seq = translated_seq + codon_map[codon]
    return translated_seq
