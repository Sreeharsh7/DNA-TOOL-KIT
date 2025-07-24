import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from dnatoolkit import validate_dna, gc_content, reverse_complement, transcribe

class TestDNAToolkit(unittest.TestCase):
    def test_validate_dna(self):
        self.assertTrue(validate_dna("ATCG"))
        self.assertFalse(validate_dna("ATXG"))

    def test_gc_content(self):
        self.assertEqual(gc_content("GCGC"), 100.0)
        self.assertEqual(gc_content("ATAT"), 0.0)

    def test_reverse_complement(self):
        self.assertEqual(reverse_complement("ATCG"), "CGAT")

    def test_transcribe(self):
        self.assertEqual(transcribe("ATCG"), "AUCG")

if __name__ == "__main__":
    unittest.main()
