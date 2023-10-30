def gc(dna):
    gc_count = dna.count('G') + dna.count('C')
    total_bases = len(dna)
    return (gc_count / total_bases) * 100

def highest_gc(dna_data):
    max_gc_id = ""
    max_gc_percentage = 0.0

    new_id = ""
    new_dna = ""

    for line in dna_data:
        if line.startswith('>'):
            if new_dna:     #For every new DNA sequence, we calculate GC and update only IF it's higher
                new_gc_percentage = gc(new_dna)
                if new_gc_percentage > max_gc_percentage:
                    max_gc_id = new_id
                    max_gc_percentage = new_gc_percentage
            new_id = line[1:].strip()
            new_dna = ""
        else:
            new_dna += line.strip()

    if new_dna:   #last dna
        new_gc_percentage = gc(new_dna)
        if new_gc_percentage > max_gc_percentage:
            max_gc_id = new_id
            max_gc_percentage = new_gc_percentage

    return max_gc_id, max_gc_percentage



data = [
">Rosalind_2210",
"GAGAATCGAGAAATGATGCCACACTCCAATCCGCGCTTAGTCTGCCCTCTCAATAAGTATACACCCGAAGAGTCCCCGCCTAGATAATGAATTGCGCTCATAGTGGCAGACCCGCGGCCTATGACGTTCTCAACGGTCATAGTAAGCTAACAAATATGGTGGACACACGTAAGCCCCACCTTTTACGCTTAAGAGTAGTCCGAACATAACCCAACCTAATTAGGACCTCATGGCCAATTATGGTAAGACTCCGAATTAGTCACGGGCGATGTGAAACGTCATGCAGCAAACACTCTATTATGCCGGAAACGTTCTTGCTTGGGCCAGGATTGCGGGTTACAATATCTGGATCCGCTTACAAGAGGCCTTATAAGTGGCTAGGAATGTCCGCCGGGATAACGTATTTCGAGTAGGGAACGTTCCATGGATGGGCACGATGTAGAGCGGGGTTTGTGAAACATTCGCGTACCCGAAGACCAGCTGGTTTGGCTTATTACAGATGGCATGTGTAAGGATTAACTTATCACTTCCTTCACCCTTCCTCTTAAGCCCTGAGTCTGGCGTGAGCCCGTCTTTAGATAATGCCTAGGATTCTGCGTTTCTCGCTAAGTGAGGAGCTCGAGCCGGCCACAAGTTGGGTTGACTGAGCTTGACTAACAGTGTTGGGGACCAATCTTGCCTGTCATTTTTTTTTTACTAGGTAAAACTGATTGCTGTTGCGACCTGTTCTCAAGACCTGCGCTGGTTCCGGGGAAGGAGTTCTGCTTTAAACAGGCTTGGTGTTCGCTCCCTCTAGCTAACGATTACTGTAATCGTACGCACTTCGTCGTCCAGCGTCGGCGGTTCAGGGACATTGGAGCCGTGATTTCAGTAAAAATTCTATGACCTCGGCGCACCCAAGGCAC",
">Rosalind_0478",
"GTCAAGCTTTTCAGACTTTCGGAAGCCCGTAAAAGCCTAGTTAAGACGTACGCTTCGACACTGTTCCTGCTCGCTTTTAAGAAACAGAGACCCGCTAAGTGCTAGCGCCCGGCGAGATGAGTTGCCCCCATATATATCTGCCACCGACAAGGGGCTACGGAACACCGCATCCCTAATTGTTACTCTATCATGACGTTCACACACCCCTTAGCCCCCAGTATCCCAACAAGTGTGCTAGACGGACCTAACACATAGAACAATCTATCGTCTTATCCGACGATTGCTTTTTGCGAGGTACAAAGGCTTGGTTTCGGAGTCATTATGCTTTCTGATCAAACGTCCATTGAAATCTGATACCTTGTTATAAGTGCGATGAGAATGTACTGACAGGTACTCACGCCGCTGTGCTCAAAGACTCCTAATATACCCCGATCGCAGCAAATTAATCAGTAATACTTTATAAGTCACAAAGTTTACAAGCCCTAAGCATATAGCACAACTAGGTATCACGTGCCCTACTCGTGGGTTGTCAGCTGATACACTGCTCTGTGACGCTGGAACTAACATAAGCGGGGATTCGGTTGGGCCTTACATTAGACACTCGGATCGGATTGGGAAGAACAAAATGCTATATGGCCTACACATGAAAAGGACATTTTAGCGTGTGTTGTGGATGATTTCCCCACCCGACTCAGCCGTACACATATAGATCAATGACCCGCCTTTGCCGTCTAGTGGAACAATCCAGGCACTAACGGGCTCTGGGAACCTGAGTCATATCAAGCCGACACTTCCAACGTATTCTTAGCA",
">Rosalind_5570",
"ACAACAGTAACATAAATATCATAGGGAGGGAGTTAAGGGTAGCAGCCGTACAATTCTAAGGAGCCATTTCGGCCCGGTGGCCGACAAATGCCTATGGCATCCATCGACGAACAATCAGTACCGCCACCACGGCGAGTAGTAGCGTGTTACCTACACAATATGGCGATTGAGTTATAAGGGATCTACGTCGATATGGTCGCTCTGTGCCGTTTCACAGATACGACTGCGAATCTTGATAGTGACGCAGACACCACGTAGCAGTTGCCGTACGTGCCCATTACAGTATCCACATTGATTTTAAAATGTTCCTATAGCCGTTTACCGTAGACCGTATGTGTAGGGTGTCGCACATTAACCCAAACAGGCACGACAGCAGTGGGCATACAGGTGTGGATACATAAACCTAATAACGAGGTCATCGTGGCATAACGTAAGTAGGGTACCACATCCATGTATTGAGTCCCTAGAGCCCAGTATAATGCCAAACTATTTAGCATAATCATATAAGCTCCTACGAAGCTCCGAGTGAGTGGTCACAAGTAGTAAACGGGTAGAGTCTCCTCACCCCAGTCTCGCCCGGAGATGGAACTTAGACCTATATGATTAGAAGGTAGATTTGCTAAGAAAATTTCAGAACCTTTTGCGTCAGGAGCGCTTCTAATATCCCTCTCGTCCTTAATTATGTATCTATCGCCTTCCGAGTCCGCTCCCTAGAGGATCTTTTTTCGTGATGTCTTAGCCATCAACAGTAGGGGAATGAAACGCGCTTGGAATTGGCTACACCTGCAGTCGGGAGGCCACCGATGCATCAATGGATGTCGCTCGCGAGCCGGTTGTCGGGTCGGT",
">Rosalind_9287",
"AATATACGGGTATCGTCCTTCAAGAGAGGTAACCACGATTTTAGAGGACCTCAGTGCGTGCCGCCAATTATTTGGTCGTATCCGCTGGTTGTGGGCCATGATACCACGCCTTGGAAACGGCCGTAGAAGTCTCGTTTAGACGAAGAACACAGCGATACATACGGTCTGTAGCAGGGTGTGTCAGGCCTGACTTACAGATGAGAAAAGTCGAAGTCCTTATCCGAGCGCCTACGCAAGCTTGCACCCGTCGCGCCACAAAGGGCATACTCCGAACGAACAGGAAGCACCGCATTGAGCTTACGACTATTAAACACATGGTTGAATTGCGCGAGTCATGAAACGTTCTGGAACGAGGGGTTTGCTTGTGCACTTAAATGTGCTATTGTCCCAGTACCTGATCCGGGTACAACGCAGAACTCTGCGATAAGGGCTCGATACCGGTACAGAGGACGTACTTAGATCCAAACATGGCAGCATCATTACAAAATCCCCTGTCGCAGATTCAAGTCCTAGAGCTCCTTGGTTCCACGTAGCCGCATGAAGGAAAACGCTTCGCCAGCGAACTGGGTCAGGCATTCATATAGCTAGAAGAGTGTTACTATATATAGAAAAGCAAGATTCCCGTTCTGTCATGGTTATACAAGTAATCGTGAAAGCATCATCTACCGTAGTTAACCCACGTATGAACGAACTGTCACTAAGCACAGCGCTAAGCGGTGGTTACACTAATATGCGCGTCAAGTCGATCGGTGGATCAGAGGGCACATGGACTGGCCGATCGTCCCCTCCCCGTTTACCGCAAAGCGGAATATACAGCCTGATCATACTGATGTCCAACTCTCGCAAAGTGTATACAACGAGATGCCATAGCTAGTAGTTATCGTACACGCGCAAGACGGGTGTCGACTCTTAAATCCTCACTGCCTGAAGGCGCTTACTGAAATCTGGCCATGGGGCCCTCACGGAAGTTAAATACAAACTGGGAGAGTACTAGCCTC",
">Rosalind_3686",
"GGGGCTGGCTATTTGTGACAATGGACCCTCCCGTTGTGCTGCGGAGTTTTAGCGCCTTCCGTAGGTCGTTGGTCGAACCTGGGTGTGTGATCCATCACCTCCGCGGGGTGCCTATTCCCGCGTCCGGACGGGTGACAACCTGCCGTGTCGTTTAATAAGTAAACTCTTACTCCTCGGCCCCGATAAGCGGTCAAAATATTCCGAAGCCAATCTCACTATCACCTAGTGCTCAGCATTTGATTTATGCCGAATCAGAGCCGTCCTCGTTCCGGAACCGATGAGTACTAGGAACATACTTTTTAAGCCGGCCACTCGCCTATCGGTGTATTCCTTTTGATCGGCGATCCTTTGCAACGTATGCCCCGCGACACACCGCACCCTCAGCCGCTAGGTCGATGTGACCGGGTGCACCATCAGCAACGATGAAAGAAAGTTAAGCAAGGGGTGAGTTGTTTGTCACCGGTGGTAAAGCTAAGAGGCTCGTGGCATAAGGGTTGTCTCGGGTACGAGCGTCGTTCGGGCAGAGGAGAAGTGCTCCCATGCTTACCCTAATAACACTATAACTAAGCGTAAGAATTATCCCCTGCCATGCGAAGACTACCTGAGGGGGAAGCATCTTATAATCTATAGGATTATTACCACGAGGGATTACGCGCGGCTATAACCAGATACATGGCATTTTGTCTCTTAGGCAATGTGAGGGGCGACTGAGGGCACAGATCCACGTTTACTATGCCTACAGCGTACCGCTGTCAGTCCTAGCCTCGCCTAAAATGTCGGGCGCCTTACGGGCCCAAACCTCTTTGAGGACTGTGGTCAA",
">Rosalind_1119",
"GGTATCCATTCCCCGGGTGTTTCACCCCGTATCAGTCCTTACGCTACATATGCTGGTTCAGCGTCGAATTACGTATATGTTTCTACAGGGCGCCACTACTCTTGGATATCCTTCTATTGTCACCCCACCTTAATGCACGGGTCTGTGACAGGTGAATCCGTGGTATTACATCACATCTGTCCTGATTGTGGGAGTCCTGATATAAGATATGTGCGGTAAATCAGCGCTATCATAACGCTACGCCGCCTTCCACTTTGCACACGTATTGCCCGGGTATGCGTGCGGATACTTCTCATCTGGAGTTTCATCGTCTAGTTCCTTACTGATTAACTAGAGCACTATGAGCAAACGGACGGGATGCGAACTCGGTGGAGCAAACATGTTAACTTAAACAGCTCACGAAGGTGACCACAAAGCACATGTATTGGGTAGGTAGATCACATGCTTGCTGTCTGTGCGAAGATTCTCGACACATCGACAGAACGCAGTGTGGCGCACTTTAGTGTTAGACTCGGAAATGTAATAGAGGGCTGAAAAGGCCAAAACGTCTCTTTACTGGCCGACGTCAGGTCTGATCCGCCATGATCACAGTGACTATGCGTGATGCATTTGCATCCTCGGCTTGTGTAATAACTAGGGTCGTACGCGTATAGGCTAGCCTCACTCACAGCGCACTTTGTGTGAAGGTGCGGCCAGTTCAGTCTCTTCATTTCCGTTTTTTTAACATGCGTGAGCAACCTCTCGATGATCATCAGACGAGGTGGACTTGCATTATGCCAGATGAGGCGTCCGGGAAACCGCACGTCCGAACTGTTGCAAAACCGCGATCGGCGGAAGCCTCGAGATTTTCGCTTGGTTTACTGGTGTTACGCCAAAGCGGAGTGGAGCCGCCGTTCTCAAGTTGCG",
">Rosalind_7629",
"CTGGCCTCATATCGACATAAACACAGCGTCTCTCCGCAACGGTAGGCCAAATTTGTGGGACCCGCTTGTCATTCAACGAGGCATAAGAATTCGGACGTGGCTGAAATCGACCATGCCGCTGAGCTTGACGCCGCGAGGCTGTGATGCTGCGTTAAAGCAGCGAGGTGCTATTTGATCTCGTTCTCTGCCGCCATGCCCACCGTGAGTAAGATTTCATCATGCGATAAAATTCCAAACCAGGAATTATGCAAATGATTACGGAAATAACTCGAGGCGGGATATGGTATCAAAAGGATGCTGGTGCCATGGGACGTATCATCAGGACATCTTAGCGGGCGGTCATGGTTTTCCGGCTCAAGTGCAGTCGCAGAAAAGGTAATCACTGTCGTTGTGGTCATGTTGGTCGCAGTTAACGGTAATCCGTTGATTTCTTACAGGCGACCTACCCAGGCCAAGAGAGTCCCGAAAAGTGCTTGTGATGAAAACATCCCAGGGTAATCGCAGCTCAGATAGCACCAGAATGATACAACCCTCCCGCAGCCTGGTAGTCGACTGTTCAGTAGTCCTTTTTTGTTTGCCACACGGTAATCCACTCAGGCAGATTGTGTACGCCCCAAGTCGTTGCCCGAAAACAGTAGGTGTCGGCTCTGCACTTTACATATCTAATTCTTTGGCGGGTGAGCTTCTTAGTTTGCTTTTGTACGGATCGTCAGGAGTTGTTGGCCTACGATCCGAAGTACAGGCGAAAGACTAAACAATGTAGTGCCAAAACCGTCGTATAGGTCGGCTAGCGCCGCGATCAATTGCGATGGGCAGTTTGATATCGAGCCGTTACATAAAGAGGACAGATGAGGCTCCGGCCTGGGAATATCAAATCTTAACTACCAACAGCCGTTACTCCCAAACAAAGAGCCGGTTTAA",
">Rosalind_5940",
"GTGAGACCGACTCACCCAATGACAGGGAATCACGGAAAGACGTGAGCCTTGGCCCGAATCGCAATTTTAATGATAGAAGACATGACAGGATCAAAAGAAGGTCCTCGCTGCATTTTGGAAGGGCGAGCATATGTGGCATGAATAGATCTTTCTAGCATGGGTTTAAATTGTGACTTTATGAACTATCTTATCCTAATGGTTTGTAGCGCCCGTCTGCAACATAATGCGAGGCACGGGAAGAAGGCAACTGTGGACTTAAGTCTACACGGATACTGGATAAGGGCCTGCGGCATGGTGGGCACTTAGCAACGATGCATCTGTATTTTCCCTGCCATGAATTGTCAAGTACGAGGCCCTTATCTATCGCCGCCAAGCGGAGGGCAGGCCGTTAGGCATAGGGCAGAATTTACTTGGTCTGATTACCCCCCATTCCCTCGTACCTTAGATTTTTATCCCGAATCAGGGTTTAGTTGCGGTGTCCAGCTGCCATCGCATCACGTAGTAGGCCCGTCTCACCTACCAGCAGCACGCGCAAGGGAAGCCCGTCTCATGACCAGGGCCCCCATCCGATGAACCCGCTGGCCTCACTCTGGAGTAACAGTCCCACCATAGAATGCTCCTGGTTTGTTTCCCCATCACCGCCCATAAGTCTGCCAGAACACGCAACGCTTATTTATGAAATGTGCGAGCCGCTGCGCAGACGCCAACGTTCACTGCCTAGGGAGAGTGGCTTAACACGAAACTAGAAGCGCTTACAGTTTACGCTAAGTGTGCCTTGCTTGCTTTCTTGTTCTGGCCCTTTAAAAATGGTTTCTTCATACGTGTGTACCCCGACGCAGC"
]


result_id, result_percentage = highest_gc(data)

print(result_id)
print(f"{result_percentage:.6f}%")