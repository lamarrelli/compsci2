'''        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
        "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"'''

def num(protein):
    codons={
        "F": 2, "L": 6, "S": 6, "Y": 2, "C": 2, "W": 1, "P": 4, "H": 2, "Q": 2, "R": 6, "I": 3, "M": 1, "T": 4, "N": 2, "K": 2, "V": 4, "A": 4, "D": 2, "E": 2, "G": 4,
        "Stop": 3
    }

    tot = 1
    for aa in protein:
        tot = (tot*codons[aa])%1000000

    return (tot*codons["Stop"])%1000000

protein = "MNNGVFFMIEDAFCEHYAKWMNQMEFQVKIMAQMQCMLGEHLANYKRCKHGAVGLKYNKPQSQWHWTFCRNEWLDREFGETLDFGFLFPNVDWQERFYHMCQHNPVPWCKNHEANGATTPTCTTGWMWTDTMFRTRGEVLPTPPREYNHTRPHKKGTFPYRGHMVEMYWGRVEVACHYPMKCIPVQSPNFWPGGKKRKEDYNMHSQIEKDSVDDNCCGARVIQMLFCWAPGRYVVSKKIACFWNHMQSPDPLYKRKDTDCHEAYCILHVVQKRMDTVSPLSNDTQSEAMYFRWFCMHSFYDWTDVYTHMLGHEIRLIMRPKGQTHGHRIKVLNSELREYFRHQTTQALMFFDMTRMIYYEDFHHYPAGLNDLHDGYFECGHFCGPESHMKARRCPFENYQGKPITQMRQTNLQPPEEYKMDWYWYQFVVPRLQNKEHIIHWACNTMVWCRVMDKEEDSTQKMWIMIHCLQQKTEGQFTKANHKEEIKEDQDNWWQQIRKMLAYHIDEGHQCWMFFIQLCHRMMWLKRTWFKGVYHAATGSTTYDTVEKSIQQRETTLFGWPFWSREMEFPIAFSYTWGHHWMMMRMLHLEISVLINHTQCFDINVCAMKWRFGRSGRYTRAPKMAFTWFTLIFHCMMAFRACCGQRSQWLVGFLGYHLMSYDPLSPPFRLMCRCWVRCWPNTDEEISTATNSCQSAYDYRDCPWALDSGTVCFYLYCFNFPANYSDYWFGARSRQDAVLNGCPHARQWYPIIGCWQIFQDCDFRQGKEICRKMMFLFLKTINARLWPDDELESGEMEAIHGSMLWQRCHVPEEVQRQNSHVMTERATQTDPGGQINCCDRRQCKFRYPSLIVIKFIQHRCFAHFTQYPLPASILLVTGIKGWHYAKGQNPREVLGLRHQRCKQYSPFLDALCNKHYSPMFHCYYCAADPASSDEGTVSCWDQNGYSHPIMGQTDDPQNLQPHETSYHVIRKNQRSRQQMTTSKVLFTLAEDKDDVHGE"

mrna =num(protein)

print(mrna)






