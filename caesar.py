"""
File: caesar.py
Name: Angel Chen
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""

# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    The function deciphers the encrypted words that the user inputs.
    :return: deciphered string
    """
    num = int(input("Secret number: "))
    ciphered_string = input("What\'s the ciphered string? ").upper()
    new_alphabet = replace(ALPHABET, num)
    deciphered_string = cipher(new_alphabet, ciphered_string, ALPHABET)
    print("The deciphered string is: "+deciphered_string)


def replace(alphabet, num):
    """
    The function produces shifted alphabet according to the number user inputs.
    :param alphabet: CONSTANT
    :param num: int, a number to produce shifted alphabet as the cipher table
    :return: str, shifted alphabet
    """
    new_alphabet = ''
    new_alphabet += ALPHABET[-1*num:]   # slice the alphabet from back
    new_alphabet += ALPHABET[:(26-num)]
    return new_alphabet


def cipher(new_alphabet, ciphered_string, alphabet):
    """
    This function deciphers the encrypted words.
    :param new_alphabet: str, shifted alphabet
    :param ciphered_string: str, encrypted words
    :param alphabet: CONSTANT
    :return: str, deciphered string
    """
    ans = ""
    for i in range(len(ciphered_string)):  # loop every letter from ciphered_string
        ch = ciphered_string[i]
        if ch.isalpha():     # if it is a letter,
            j = new_alphabet.find(ch)  # find the index of this letter in the new_alphabet
            ans += ALPHABET[j]    # add the letter into the 'answer'
        else:   # if it is not a letter,
            ans += ch   # add this character into the 'answer'
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
