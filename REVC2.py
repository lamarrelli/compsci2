def rc(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    r_c = ''.join(complement[x] for x in dna[::-1])
    return r_c

dna= "GGATAGTGGAGATCTTTGTGTTGGGGAATCGGCGTGCTAGTTTTTGGATCTATCCTTGTCTAGCATGCTTCCTTGGTGGACGTGACGTGACGTTTAAACCGCGCTGCTGTGGCACCTCAGACACATGGGCTCAAAGGTTAGTTTGGGGATGCAAACCCCTATCCATGGGGGTCTACGCACCGAAAACCTCCTAGTAGAGTCTCGATAGAACGCGCAATGTCGAAGAAAATCACGGAGGACGGTAACAGACTAAGAATGCAATCCAAGAGCAAGAGCCTTATCTGGCCGAGTACTCTAACCATGGCTCTAAATGCTTTCCACTTGTAACCTGGACTAAAGCTAATGACCGCGGATTTAGTCTTCGTTGAACAAATCGGCTCTGTAGCTGTTTGTAACATTAGCTAGAAGTGTGCCACAAAAGTGAGAGCAGGATTTTACCACCCAGTCTCATGGACGCAGGCAATCCCCTCCATCTTGGCCGTGGCCCCGCCGCTGTGGCATGAATATGTCGTGCGGAAGCGAGTGCTCAGGAGTGTGGTAAGACTTGCGCATACGAGGTATCCGGTGTGATCGTCACTTATGCGGTCGCCGGCGCGGAGAATTTTGCAGGGGTGGCGCGGCCGCTCTTCTGGCCCTCCCCAACCGTCTGGTCGTTGCATCTCAAACGAGACGTCTAGGGATCAATTGGTGATCACATCATCACTCCTCAGCTACTAGTCGCAAGTACCAATCAGTGAGTTCGAACCATCGCAGTCCTAGCCAGTTCTACTGTTGTAATAACGCCTCGATGTACGCCGAGCACG"
revc = rc(dna)

print(revc)

#rc caput mundi :D