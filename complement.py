"""
File: complement.py
Name: Angel Chen
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This function asks user to input a DNA strand,
    and then shows the complement of it.
    """
    dna = input("Please give me a DNA strand and I\"ll find the complement: ").upper()
    new_dna = build_complement(dna)
    print(new_dna)


def build_complement(dna):
    """
    This function shows the complement of DNA.
    :param dna: str, DNA strand including A, T, C, G.
    :return: str, the complement of DNA, for example: A <--> T, G <--> C.
    """
    ans = ""
    for base in dna:
        if base == "A":
            ans += "T"
        elif base == "T":
            ans += "A"
        elif base == "G":
            ans += "C"
        elif base == "C":
            ans += "G"
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
