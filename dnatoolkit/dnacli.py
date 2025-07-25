# dnacli.py
import argparse
from dnatoolkit import validate_dna, gc_content, reverse_complement, transcribe

def main():
    parser = argparse.ArgumentParser(description="DNA Sequence Toolkit CLI")
    parser.add_argument("sequence", help="DNA sequence (A/T/C/G only)")
    parser.add_argument("--gc", action="store_true", help="Calculate GC content")
    parser.add_argument("--rev", action="store_true", help="Get reverse complement")
    parser.add_argument("--rna", action="store_true", help="Transcribe to RNA")
    
    args = parser.parse_args()
    seq = args.sequence.upper()

    if not validate_dna(seq):
        print("❌ Invalid DNA sequence! Only A, T, C, G are allowed.")
        exit(1)

    if args.gc:
        print("🧪 GC Content:", gc_content(seq), "%")
    if args.rev:
        print("🔁 Reverse Complement:", reverse_complement(seq))
    if args.rna:
        print("🧬 RNA Transcription:", transcribe(seq))

if __name__ == "__main__":
    main()
