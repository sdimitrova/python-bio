my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
complement = []

for nucleotide in my_dna:
    if nucleotide == 'A':
        complement.append("T")
    elif nucleotide == 'C':
        complement.append("G")
    elif nucleotide == 'T':
        complement.append("A")
    else:
        complement.append("C")

print(complement)

answer = []
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

for nucleotide in my_dna:
    answer.append(complement[nucleotide])

print(''.join(answer[::-1]))