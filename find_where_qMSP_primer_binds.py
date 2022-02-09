"""

Script containing functions for - based on a given gene sequence - reveal the original DNA primer binding site
based on the meth-primer sequence designed to bind fully-methylated bisulfite-converted DNA.

Belongs to a suite covering everyday tasks handling methylation data and setup for simple
DNA-methylation related experiments.

@author Anja Hess

"""

def fasta2string(path_to_fasta):
    """
    This function will read a fasta file and convert it to str as a preprocessing
    measure for bisulfite conversion.
    :param path_to_fasta: str
    :return: str
    """

    f = open(path_to_fasta, "r").read()
    cleaned_seq = f.replace("\n", "")

    return cleaned_seq

def bisulfite(seq):
    """
    Simple function to convert a given sequence (DNA) to the bisulfite
    modified sequenced, assuming that all CpGs are methylated.
    Therefore, all "single" Cs will become Ts, unless the next letter is a G.

    :param seq: str
    :return: bis_seq: str
    """

    bis_seq = seq.replace("CG", "XX").replace("C", "T").replace("XX", "CG").replace("\n", "")

    return bis_seq


def find_primer(seq, bis_seq, primer_seq):
    """
    To find a primer (fwd) in bis_seq and provide the original sequence.
    :param seq:
    :param bis_seq:
    :param primer_seq:
    :return: print statements revealing the original sequence
    """

    unmethylated_primer = primer_seq.replace("C", "T")
    print("Found mPrimer in bisulfite-converted sequence at pos:", bis_seq.find(primer_seq))
    pos_primer_bis = bis_seq.find(primer_seq)

    print("mPrimer:", primer_seq)
    print("origin.:", seq[pos_primer_bis:pos_primer_bis+(len(primer_seq))], "<- Please reverse compl if this is rev primer")
    print("uPrimer:", unmethylated_primer)

    # END OF FUNCTION



############# USER INPUT #####################

# Step 1: Enter the directory of your fasta files
mother_dir = "/home/anja/Downloads/"

# Step 2: Modify the fasta dict in order specify which gene/region you're provide the fasta for
fasta_dict = {
    "ACTB":f"{mother_dir}Homo_sapiens_ACTB_sequence.fa",
    "SOX2": f"{mother_dir}Homo_sapiens_SOX2_sequence.fa",
}

# Step 3: Enter the primers for methylated bisulfite converted PCR product (preserved CG):
# Important note: You need to reverse complement the reverse primer.

# These sequences are fully made up and serve as an example only. Order: fwd, rev (but doesn't affect the result yet)
primer_dict = {
    "ACTB":["TTTTCCCCTTTTTCCCC", "ATGCTTATTATATATTAT"],
    "SOX2":["TTTTCCCCTTTTTCCCC", "ATGCTTATTATATATTAT"],
}

# Step 4: Run the script [eg. python3 pysulfite/find_where_qMSP_primer_binds.py or click run in your IDE]



# This is how the iterative screening goes:

for gene in primer_dict:
    # Load seq
    seq = fasta2string(fasta_dict[gene])
    # Bisulfite convert
    bis_seq = bisulfite(seq)
    print(f"-------- {gene}")

    # For each primer, reveal the sequence
    for i, e in enumerate(primer_dict[gene]):
        if i == 0:
            print("--- Forward primer")
        else:
            print("")
            print("--- Reverse primer (Reverse complement)")
        find_primer(seq, bis_seq, primer_seq=e)



# END OF FUNCTION