dna_bastiao = "ATCGAT"
dna_jose = "ACGTA"
dna_maria_clara = "TCGA"

def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

print("Getting the DNA length:")
print(get_length(dna_maria_clara))
print(get_length(dna_jose))
print(get_length(dna_bastiao))
print("========================")

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    longer_comparation = dna1 > dna2
    
    if longer_comparation:
        return True
    else:
        return False

print("Checking if the first DNA is longer than the second one:")        
print(is_longer(dna_bastiao, dna_jose))
print(is_longer(dna_maria_clara, dna_bastiao))
print(is_longer(dna_jose,dna_bastiao))
print("========================")

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    
    return dna.count(nucleotide)
  
print("Counting the number of times a nucleotide occurs in the DNA:") 
print(count_nucleotides(dna_bastiao, 'G'))
print(count_nucleotides(dna_bastiao, 'T'))
print(count_nucleotides(dna_maria_clara, 'C'))
print("========================")

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    
    return dna2 in dna1

print("Checking if the DNA has a specific sequence of nucleotides:")
print(contains_sequence(dna_maria_clara, "AT"))
print(contains_sequence(dna_jose, "AC"))
print(contains_sequence(dna_bastiao, "CG"))
print("========================")

def is_valid_sequence(dna):
    '''(str) -> bool
        
    Return True if and only if the DNA sequence is valid (that is, it contains no characters other than 'A', ’T’, 'C' and 'G').         
        
    >>> is_valid_sequence('ATGCCT')
    True
    >>> is_valid_sequence('ACGT')
    True
    >>>is_valid_sequence('AGCUAT')
    False
    '''
    valid_nucleotides = {'A', 'T', 'C', 'G'}
    
    for nucleotide in dna:
        if nucleotide not in valid_nucleotides:
            return False
    return True

print("Checking if it is a valid DNA sequence:")
print(is_valid_sequence(dna_bastiao))
print(is_valid_sequence('ATXCG'))
print(is_valid_sequence('GDADP'))
print(is_valid_sequence(dna_maria_clara))
print("========================")

def insert_sequence(dna1, dna2, index):
    '''(str, str, int) -> str
    
    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index.
    
    >>>insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>>insert_sequence('GATC', 'CG', 3)
    'GATCGC'
    '''
    
    return dna1[:index] + dna2 + dna1[index:]

print("Creating a DNA sequence:")
print(insert_sequence('CCGG','AT',2))
print(insert_sequence('GATC', 'CG', 3))
print(insert_sequence('AGTA','TC',0))
print("========================")

def get_complement(nucleotide):
    '''(str) -> str
    
    Return the nucleotide complement.
    
    >>>get_complement('C')
    'G'
    >>>get_complement('A')
    'T'
    '''
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return complements[nucleotide]

print("Getting the complement of a nucleotide:")
print(get_complement('A'))
print(get_complement('T'))
print(get_complement('C'))
print(get_complement('G'))
print("========================")

def get_complementary_sequence(dna):
    '''(str) -> str
    
    Return the DNA sequence that is complementary to the given DNA sequence.
    
    >>>get_complementary_sequence('ATCGC')
    TAGCG
    >>>get_complementary_sequence('TATACG')
    ATATGC
    '''
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complementary_sequence = ''.join([complements[nucleotide] for nucleotide in dna])
    return complementary_sequence
    
print("Getting the DNA sequence its complementary sequence:")
print(get_complementary_sequence(dna_maria_clara))
print(get_complementary_sequence(dna_bastiao))
print(get_complementary_sequence(dna_jose))
print("========================")