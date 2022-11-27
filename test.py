def calc_average():
	""" Function to determine the average score """

	# Add the total of numbers in list and divide by list length to get average.
	total = 0
	test_score = []
	test_scores_count = 3

	# Add error handling to ensure if the input is NaN or more than 100
	# or less than 0. The input will be rejected.
	while len(test_score) < test_scores_count:
		try:
			user_prompt = int(input("Enter a test score: "))
			test_score.append(user_prompt)
		except ValueError:
			print('Enter a valid number!')

		else:
			print(test_score)
			for number in test_score:
				total += number
				
		average = round(total / len(test_score))
		print(average)
		return average

result = calc_average()