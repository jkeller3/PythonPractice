def reverse_word(word):
	reversed = ''
	for letter in word:
		reversed = letter + reversed
	print(reversed)
	return reversed

def is_palindrome(word):
	return word == reverse_word(word)

def check_all_palindromes(arr):
	for word in arr:
		if is_palindrome(word) == false:
			return false
	return true

word = 'abcdefgfedcba'
print(is_palindrome(word))