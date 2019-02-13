#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 1, Exercise 3

def parser(string):
    punctuation = [',', '.', '!', '?']
    parse = string
    for symbol in punctuation:
        parse = parse.replace(symbol, ' ')
    return parse

while True:
    print("Type a phrase to see how many words and characters it has. Repeated words and puncuation will be removed. Type STOP to break: ")
    phrase = input()
    if phrase.casefold() == 'stop':
        break
    else:
        parsed_phrase = parser(phrase).split()
        unique_words = []
        for words in parsed_phrase:
            if words not in unique_words:
                    unique_words.append(words)
        i = len(unique_words) - 1
        for word in unique_words:
            i = i + len(word)
        print("Your phrase has " + str(len(unique_words)) + " words and " + str(i) + " characters.")