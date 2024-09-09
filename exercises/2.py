# Enter a word: Python
# Uppercase: PYTHON
# Lowercase: python
# First character: P
# Last character: n
# Replaced word: *ython

aword = input("Enter a word: ")
upper = aword.upper()
lower = aword.lower()
fchar = aword[0]
lchar = aword[5]
repword =  aword.replace("P","*")

print(f"Uppercase: {upper} \nLowercase: {lower} \nFirst Character: {fchar} \nLower Character: {lchar} \nReplaced word: {repword}")