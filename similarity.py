"""
File: similarity.py
Name: Angel Chen
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
	"""
	This function asks user to input two sequences of DNA,
	and compares both sequences, then shows the most similar segment of DNA.
	"""
	long_sequence = input("Please give me a DNA sequence to search: ").upper()
	short_sequence = input("What DNA sequence would you like to match? ").upper()
	most_similar = sequence_compare(long_sequence, short_sequence)
	print("The best match is " + most_similar)


def sequence_compare(seq_a, seq_b):
	"""

	:param seq_a: str, long DNA sequence
	:param seq_b: str, short DNA sequence
	:return: str
	"""
	max_num = 0  # count the number of same DNA
	for i in range(len(seq_a)):  # for loop each long DNA
		segment = seq_a[i:i+len(seq_b)]  # Slice the length of short DNA seq from long DNA seq to match
		same_dna_num = 0
		for j in range(len(segment)):  # for loop each short DNA
			char = segment[j]
			if char == seq_b[j]:    # if DNA from short DNA seq matches DNA from long seq
				same_dna_num += 1   # adding 1 to the number of same DNA
			else:
				same_dna_num += 0
		result = same_dna_num       # reassign the current same DNA number to 'result'
		if result > max_num:
			max_num = result
			most_similar = segment   # reassign the most similar DNA seq for now to 'most_similar'
	return most_similar


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
