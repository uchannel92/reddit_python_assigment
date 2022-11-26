#Uchenna will create his solution from this page for assignment.py

def calc_average():
	""" Function to determine the average score """

	test_score = []
	test_scores_count = 8

	# Add error handling to ensure if the input is NaN or more than 100
	# or less than 0. The input will be rejected.
	while len(test_score) < test_scores_count:

		user_prompt = int(input("Enter a test score: "))
		test_score.append(user_prompt)

	print(test_score)



def determine_grade():
	""" Determine the grade from the score provided """


calc_average()