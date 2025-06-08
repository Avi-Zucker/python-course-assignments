from collections import Counter
from codon_table import codon_to_amino
import sys

# make sure we got the file
if len(sys.argv) < 2:
    print("Usage: python count_amino_acids.py <file>")
    sys.exit(1)

# read the file
filename = sys.argv[1]
with open(filename, 'r') as file:
    lines = file.readlines()
    sequence = ''.join(line.strip() for line in lines if not line.startswith('>')).upper()

amino_acids = []
for i in range(0, len(sequence) - 2, 3):
    codon = sequence[i:i+3]
    aa = codon_to_amino.get(codon, None)
    if aa:  # skip unknown codons
        amino_acids.append(aa)

counts = Counter(amino_acids)

for aa in sorted(counts):
    print(f"{aa}: {counts[aa]}")