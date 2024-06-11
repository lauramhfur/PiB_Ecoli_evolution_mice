from fasta_functions import *

def slice(ref_genome, mutations_df, outpath_ref, outpath_wt, ref_name):
    mice = list(mutations_df['host'].unique())
    for mouse in mice:
        mouse_df = mutations_df.query(f"host == '{mouse}' and mutation_type == 'snp'")
        for gene in mouse_df['gene'].unique():
            gene_df = mouse_df.query(f"gene == '{gene}'")
            start = gene_df['gene_start'].iloc[0]
            end = gene_df['gene_end'].iloc[0]
            gene_seq = ref_genome[start-1:end]

            write_fasta(f"{gene}", ''.join(gene_seq), f"{outpath_ref}/{ref_name}_{gene}.fasta")      # Reference gene
            for _, row in gene_df.iterrows():
                p, m = row['mutation_position'], row['mutation']
                i = start
                while i <= end:
                    if i == p:
                        gene_seq[i-start] = m
                        i += 1
                    i += 1
            write_fasta(f"{gene}_{mouse}", ''.join(gene_seq), f"{outpath_wt}/{mouse}_{gene}.fasta")  # Gene with SNPs
    return
