# Your code here

ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '\\','/', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', '?']

def histogram():

    dict = {}

    with open("applications/histo/robin.txt") as f:
        words = f.read()
        splitWords = words.split()

    for word in splitWords:
        histo = ""
        for char in word:
            if char not in ignore:
                histo += char

        word = histo.lower()

        if word in dict:
            dict[word] += 1
        elif word == "" or word == " ":
            break
        else:
            dict[word] = 1
    
    items = list(dict.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for (string, value) in dict.items():
        maxLen = len(max(string, key=len))
        print(f'{string} {" " * maxLen} {"#" * value}')
    
print(histogram())





