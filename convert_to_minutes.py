def convert_to_minutes(num_hours):
	"""(int) -> int
	Return the number of minutes there are in num_hours hours.
	>>> convert_to_minutes(2)
	120
	"""
	result = num_hours * 60
	return result

def convert_to_seconds(num_hours):
	"""(int) -> int
	Return the number of seconds there are in num_hours hours.
	>>> convert_to_minutes(2)
	7200
	"""
	minutes = convert_to_minutes(num_hours)
	seconds = minutes * 60
	return seconds

minutes = convert_to_minutes(2)
seconds = convert_to_seconds(2)
