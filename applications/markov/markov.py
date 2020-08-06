import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
   words = f.read().split()

# TODO: analyze which words can follow other words
# Your code here
dict = {}

for i, value in enumerate(words):
    if value not in dict:
        dict[value] = []
    if i < len(words) - 1:
        dict[value].append(words[i+1])


# TODO: construct 5 random sentences
# Your code here
def make_sentence():
     # choose between all capital words, regardless of ""
    startWord = random.choice([x.strip('"') for x in words if x[0].isupper()])

    # need a while loop to add to a sentence
    sentence = startWord
    # consult dict at random for next word
    nextWord = random.choice(dict[startWord])

    while not nextWord.endswith(tuple('.?!')):
        # take the prev next word and go thru the dict again
        nextWord = random.choice(dict[nextWord])
        sentence += f" {nextWord}"
    return sentence

print(make_sentence())
print(make_sentence())
print(make_sentence())
print(make_sentence())
print(make_sentence())