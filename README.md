# Code for qPCR-based Assay to derive _oriC:ter_ Ratios

This section outlines the code used to derive genome lengths and identify oriC regions in our project, utilizing the ORCA tool (Meel and Baaijens, 2024).

**Genome Lengths**

<p> To obtain the genome lengths of the microbial strains used in our study (Escherichia coli and Bacteroides thetaiotaomicron), we used the genome_length.py script. This script processes the genomic sequences provided in FASTA format and calculates the genome length for each microbe sequence. </p>

**Running ORCA**

<p> The code used for oriC identification was derived from the ORCA paper and the accompanying GitHub repository (Meel and Baaijens, 2024). To run ORCA locally, you can use the following command line code, which requires the accession number of the microbial genome:</p>

`python orca.py <accession_number>` 

Ensure that the ORCA tool and its dependencies are installed before executing the script. The tool will identify the origin of replication (oriC) in the provided genome sequence and output the corresponding genomic coordinates. The ORCA GitHub repository has extensive information about how to install and use ORCA.
