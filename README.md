pysulfite
===========
A collection of simple scripts to handle genomic methylation data. 


# 1. Installation

pysulfite is purely based on **Python > 3**.

    sudo apt-get update
    sudo apt-get install python3.6


# 2. Example: Find the genomc binding site of a meth primer (e.g. for qMSP)

# Step 1: Enter the directory of your fasta files

    mother_dir = "/home/yourname/fastas/"

# Step 2: Modify the "fasta dict" in order to specify which gene/region you're provide the fasta for

Let's assume you know which gene the primers are targetting: simply provide the entire genomic region of
interest as a fasta.

    fasta_dict = {
        "ACTB":f"{mother_dir}Homo_sapiens_ACTB_sequence.fa",
        "SOX2": f"{mother_dir}Homo_sapiens_SOX2_sequence.fa",
        }

# Step 3: Enter the primers for methylated bisulfite converted PCR product (preserved CG):

Important note: You need to reverse complement the reverse primer.
These sequences are fully made up and serve as an example only. Order: fwd, rev (but doesn't affect the result yet)

    primer_dict = {
        "ACTB":["TTTTCCCCTTTTTCCCC", "ATGCTTATTATATATTAT"],
        "SOX2":["TTTTCCCCAAAACCCC", "ATGCTTATAAAATATTAT"],
      }

# Step 4: Run the script 

In your terminal:
    python3 pysulfite/find_where_qMSP_primer_binds.py
    
In your IDE: click run


# Step 5: View result!

pysulfite will tell you the original DNA sequence your primer binds, but only if your primer sequence is actually targeting in the fasta you provided.

Example output:


        -------- ACTB
        --- Forward primer
        Found mPrimer in bisulfite-converted sequence at pos: 32278
        mPrimer: GGGGTTTTATTGCGGAGTGC
        origin.: GGGGCCCCACTGCGGAGTGC <- Please reverse compl if this is rev primer
        uPrimer: GGGGTTTTATTGTGGAGTGT


# 3. Authors

* **Anja Hess** - *Initial work* 



# 4. Citing

Please cite this github repo whenever used in your work.


# 5. License

This project is licensed under the GPL3 License - see the [LICENSE](LICENSE) file for details.



