ignore = ['"', ':', ';', ',', '.', '-', '+', '=', '\\','/', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']

def word_count(s):
    dict = {}

    wordList = s.split()

    for word in wordList:
        word = word.lower()
        for badChar in ignore:
            word = word.replace(badChar, "")


        if word in dict:
            dict[word] += 1
        elif word == "" or word == " ":
            break
        else:
            dict[word] = 1
    return dict
    
    

    


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))