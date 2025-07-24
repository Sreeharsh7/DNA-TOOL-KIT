# dnatoolkit/__init__.py

def validate_dna(seq):
    """Check if the sequence contains only A, T, C, G."""
    return all(base in "ATCG" for base in seq.upper())

def gc_content(seq):
    """Calculate GC content percentage of the DNA sequence."""
    seq = seq.upper()
    gc_count = seq.count("G") + seq.count("C")
    return round(gc_count / len(seq) * 100, 2)

def reverse_complement(seq):
    """Return the reverse complement of the DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(seq.upper()))

def transcribe(seq):
    """Transcribe DNA to RNA (replace T with U)."""
    return seq.upper().replace("T", "U")
