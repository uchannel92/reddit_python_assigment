#Uchenna will create his solution from this page for assignment.py

def calc_average():
	""" Function to determine the average score """

	# Add the total of numbers in list and divide by list length to get average.
	total = 0
	test_score = []
	test_scores_count = 8

	# Add error handling to ensure if the input is NaN or more than 100
	# or less than 0. The input will be rejected.
	while len(test_score) < test_scores_count:

		user_prompt = int(input("Enter a test score: "))
		test_score.append(user_prompt)

	print(test_score)

	for number in test_score:
		total += number

	average = round(total / len(test_score))
	print(average)
	return average



def determine_grade():
	""" Determine the grade from the score provided """

	score_average = calc_average()
	comment = 'Your average grade is:'

	if score_average >= 90:  
		print(f'{comment} A')

	elif score_average >= 80 and score_average <= 90: 
		print(f'{comment} B')

	elif score_average >= 70 and score_average <= 79: 
		print(f'{comment} C')

	elif score_average >= 60 and score_average <= 69: 
		print(f'{comment} D')

	elif score_average < 60: 
		print(f'{comment} F')



determine_grade()