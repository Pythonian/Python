def shift_left(L):
	"""(list) -> NoneType

	Shift each item in L one position to the left
	and shift the first item to the last position.

	Precondition: len(L) >= 1

	>>> L = ['a', 'b', 'c', 'd']
	>>> shift_left(L)
	>>> print(L)
	['b', 'c', 'd', 'a']
	"""

	# store the first item of the list
	first_item = L[0]

	# Start the loop from the second item
	for i in range(1, len(L)):
		# Takes the item at i position and move to i-1 position
		L[i - 1] = L[i]
	# Take the item at index 0 and move to the last position
	L[-1] = first_item


def count_adjacent_repeats(s):
	"""(str) -> int

	Return the number of occurences of a character and
	an adjacent character being the same.

	>>> count_adjacent_repeats('abccdeffggh')
	3
	"""

	# stores number of adjacent repeats found
	repeats = 0

	for i in range(len(s) - 1):
		# compare the char at index i with the one after it
		if s[i] == s[i + 1]:
			repeats += 1
	return repeats

