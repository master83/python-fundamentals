def is_valid_sequence(dna):
    '''(str) -> bool
    >>> is_valid_sequence('atcg')
    True
    >>> is_valid_sequence('racc')
    False
    '''
    for c in dna:
        if not c in 'atcgATCG':
            return False
    return True;
        
def insert_sequence(dna1, dna2, index):
    '''(str, str, int) -> str
    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    '''
    return dna1[:index] + dna2 + dna1[2:]
    
def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


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

def get_complement(nuc):
    '''(str) -> str
    >>> get_complement('A')
    T
    >>> get_complement('C')
    G
    '''
    if nuc == 'A':
        return 'T'
    elif nuc == 'T':
        return 'A'
    elif nuc == 'C':
        return 'G'
    elif nuc == 'G':
        return 'C'

def get_complementary_sequence(dna):
    '''(str) -> str
    >>> get_complementary_sequence('ATA')
    TAT
    >>> get_complementary_sequence('CGC')
    GCG
    '''
    out = ''
    if not is_valid_sequence(dna):
        return False
                   
    for char in dna:
        out = out + get_complement(char)

    return out
                   
                   
                
                   
                   
    


