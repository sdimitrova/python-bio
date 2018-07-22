# open the file
my_file = open("test-sequence.txt")
# read the contents
my_dna = my_file.read()
# calculate the length
dna_length = len(my_dna)
# print the output
print("sequence is " + my_dna + " and length is " + str(dna_length))

length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')
at_content = (a_count + t_count) / length
print("AT content is " + str(at_content))


my_dna = "ATGCGTA"
print(my_dna)
# change the value of my_dna
my_dna = "TGGTCCA"

# store a short DNA sequence in the variable banana
banana = "ATGCGTA"
# now print the DNA sequence
print(banana)