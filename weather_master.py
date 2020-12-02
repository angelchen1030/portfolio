"""
File: weather_master.py
Name: Angel Chen
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop
EXIT = -1


def main():
	"""
	This program asks weather data from user
	and compute the highest, lowest temperature
	as well as the average temperature and cold days among the inputs.
	"""
	print('stanCode \"Weather Master 4.0\"!')
	temperature()


def temperature():
	y = 0  # variable y calculates the cold day among the inputs, so y starts from zero.
	data = int(input("Next Temperature: " + "(or " + str(EXIT) + ' to quit)? '))
	if data == EXIT:
		print("No temperatures were entered.")
	else:
		highest = data  # highest temperature
		lowest = data   # lowest temperature
		x = 1  # variable x calculates number of inputs
		total = data    # total temperature
		if data < 16:   # if the temperature is lower than 16 degree, it belongs to cold day.
			y += 1
		while True:
			data = int(input("Next Temperature: " + "(or " + str(EXIT) + ' to quit)? '))
			if data == EXIT:
				break
			else:
				# highest, lowest, average temperatures and cold day do not include EXIT number.
				if data > highest:
					highest = data  # reassign the highest temperature
				if data < lowest:
					lowest = data   # reassign the lowest temperature
				if data < 16:  # if the temperature is lower than 16 degree, it belongs to cold day.
					y += 1
				x += 1
				total = total + data
		avg = total / x

		print("Highest temperature = " + str(highest))
		print("Lowest temperature = " + str(lowest))
		print("Average = " + str(avg))
		print(str(y) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
