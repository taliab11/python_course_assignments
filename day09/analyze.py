import argparse
import re

def process_seq(path):
    with open(path, 'r') as f:
        content = f.readlines()
    # If FASTA format, skip header lines starting with ">"
    if content[0].startswith(">"):
        content = content[1:]
    # If GenBank format, extract sequence from ORIGIN section
    if "ORIGIN" in content[0]:
        content = [line for line in content if not line.startswith("ORIGIN")]
        content = [re.sub(r'\d+|\s', '', line) for line in content]
    # Remove all non-sequence characters, join the lines and return the upper-case sequence:
    sequence = ''.join([re.sub(r'[^GATC]', '', line) for line in content])
    return sequence.upper()  

def duplicate(seq):
    # Finds the longest repeating subset in the sequence using binary search:
    low, high = 1, len(seq) // 2
    result = ''
    while low <= high :
        mid = (low + high) // 2
        regex = r'([GATC]{' + str(mid) + r'}).*\1'
        m = re.search(regex, seq)
        if m:
            result = m.group(1)
            low = mid + 1  # Try longer substrings
        else:
            high = mid - 1  # Try shorter substrings

    print("The longest subset sequence that repeats twice is", result)
    print("with the length of", len(result))

def stopcodon(seq):
    stopcodons = re.findall(r'TAA|TGA|TAG', seq)
    print("This sequence contains", len(stopcodons), "optional stop codons")


parser = argparse.ArgumentParser()
parser.add_argument('--path', required=True, type=str, help="Path to the gene sequence file (FASTA or GenBank)")
parser.add_argument('--duplicate', action='store_true', help="Find the longest duplicate subset in the sequence")
parser.add_argument('--stopcodon', action='store_true', help="Count the number of stop codons in the sequence")
args = parser.parse_args()

#Preprocessing the sequence:
seq = process_seq(args.path)

#Performing the requested analyses:
if args.duplicate:
    duplicate(seq)
if args.stopcodon:
    stopcodon(seq)