# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# This will get the file that we want to cipher
with open("applications/crack_caesar/ciphertext.txt") as f:
    words = f.read()

#This breaks the words into a list of strings
wordList = words.split()

#This is the frequency of letters in order
letters = ('E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z')

# Set the count to hold the letter frequency
count = {}

for word in wordList:
    for char in word:
        if char.isalpha():
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

letterCount = list(count.items())

letterCount.sort(key = lambda x: x[1], reverse=True)

decoded = {}
# Assign numbers to the letters
for num in range(len(letterCount)):
    decoded[letterCount[num][0]] = letters[num]


def crack_caesar(s):
    # Set up an empty string to hold the translated cipher
    translated = ''

    for char in s:
        if char.isalpha():
            # if the character in the string is a letter add the decoded character num to the translated cipher string
            translated += decoded[char]
        else:
            # if not a letter add the character
            translated += char
    
    return translated

finalTranslation = map(crack_caesar, wordList)

print(" ".join(finalTranslation))







