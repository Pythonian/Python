def calculate_average(assignment_grades):
	"""(list of list of [str, number]) -> float

	Return the average of the grades in assignment_grades.

	>>> calculate_average([['A1', 80], ['A2', 90]])
	85.0
	"""

	# sum of the grades
	total = 0

	for item in assignment_grades:
		total += item[1]

	return total / len(assignment_grades)

