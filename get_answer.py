def get_answer(prompt):
	"""(str) -> str

	Use prompt to ask the user for a "yes" or "no"
	answer and continue asking until the user gives
	a valid response. Return the answer.
	"""

	answer = input(prompt)

	while  not (answer == 'yes' or answer == 'no'):
		answer = input(prompt)

	return answer

