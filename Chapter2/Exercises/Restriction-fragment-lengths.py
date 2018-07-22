seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
# seq = seq.upper()
pattern = "G","AATTC"
pattern1 = ''.join(pattern) # 'GAATTC'
pattern2 = ' '.join(pattern) # 'G AATTC'
splited_seq = seq.replace(pattern1, pattern2) # 'ATCGA ATTCATAATCGA ATTCATAATCGA ATTCATA'
print(splited_seq)
far = splited_seq.split()
print(far)

print("The size of " + far[0] + " is " + str(len(far[0])))
print(len(far[1]))
