from Bio import SeqIO

# Specify the path to your genome file in FASTA format
genome_file = "/path/to/file.fasta"

# Read the genome sequence
with open(genome_file, "r") as file:
    genome_record = SeqIO.read(file, "fasta")

# Extract the sequence and calculate its length
genome_length = len(genome_record.seq)

# Output the genome length
print(f"Genome Length: {genome_length} bases")
