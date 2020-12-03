"""
File: quadratic_solver.py
Name: Angel Chen
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Firstly, User inputs 3 numbers.
	Then the program will use the format to compute the roots of equation.
	Lastly, the program will show the number of root.
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a:  '))
	b = int(input('Enter b:  '))
	c = int(input('Enter c:  '))

	dis = b**2-4*a*c  # discriminant formula
	if dis < 0:
		print('No real roots.')
	else:
		y = math.sqrt(dis)
		root1 = (-b+y) // 2*a   # root formula
		root2 = (-b-y) // 2*a
		if dis > 0:
			print('Two roots: ' + str(root1) + " ," + str(root2))
		else:  # if discriminant equals to zero
			print("One root: " + str(root1))  # Both roots are same, so print one of the roots.


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
