text = input('input text: ')
pattern = input('input pattern: ')
number_of_pattern = sum([1 for i in range(0, len(text) - len(pattern) + 1) if (text[i:(len(pattern) + i)] == pattern)])
print(number_of_pattern)
