"""
File: rocket.py
Name: Angel Chen
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	This function prints a rocket, which size is decided by a constant SIZE.
	:return: str
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	for i in range(SIZE):  # row = size
		for j in range(SIZE-i):  # print the space, the picture of space is an inverted triangle
			print(" ", end="")
		for k in range(2*i+2):   # the slash composes an isosceles triangle
			if k < i:
				print("", end="")
			if k <= i:       # the number of left slash is equal and lower than the size of rocket
				print("/", end="")
			if k > i:        # the number of right slash is bigger than the size of rocket
				print("\\", end="")
		print(" ")


def belt():
	for i in range(1):   # row = 1
		print("+", end="")
		for j in range(SIZE*2):  # the number of '=' is twice as the size
			print("=", end="")
	print("+")


def upper():
	for i in range(SIZE):  # row = size
		print("|", end="")   # every row starts with '|'
		for j in range(SIZE-i-1):
			print(".", end="")   # print ".", the picture of "." is an inverted triangle
		for k in range(2 * i + 2):
			if k % 2 == 0:   # when k is even
				print("/", end="")
			else:   # when k is odd
				print("\\", end="")
		for j in range(SIZE-i-1):
			print(".", end="")
		print("|")   # every row ends with '|'


def lower():
	for i in range(SIZE):   # row = size
		print("|", end="")   # every row starts with '|'
		for j in range(i):
			print(".", end="")  # print ".", the picture of "." is an triangle
		for k in range(2*SIZE-2*i):
			if k % 2 == 0:   # when k is even
				print("\\", end="")
			else:   # when k is odd
				print("/", end="")
		for j in range(i):
			print(".", end="")
		print("|")    # every row ends with '|'


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()