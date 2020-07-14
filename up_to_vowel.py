def up_to_vowel(s):
	"""(str) -> str
	
	Return a substring of s from index 0 up to but
	not including the first vowel in s.

	>>> up_to_vowel('hello')
	'h'
	>>> up_to_vowel('there')
	'th'
	>>> up_to_vowel('cs')
	'cs'
	"""
	
	# before_vowel contains all the characters found in s[0:i]
	before_vowel = ''
	i = 0

	# Accumulate the non-vowels at the beginning of the string
	while i < len(s) and not (s[i] in 'aeiouAEIOU'):
		before_vowel += s[i]
		i += 1

	return before_vowel
