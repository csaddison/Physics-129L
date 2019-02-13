#------------------------------------------------------------
# Conner Addison 8984874
# Physics 129L
#------------------------------------------------------------

# Homework 1, Exercise 2

def parser(string):
    punctuation = [',', '.', '!', '?']
    parse = string
    for symbol in punctuation:
        parse = parse.replace(symbol, ' ')
    return parse

while True:
    print("Type a phrase to see how many words and characters it has. Type STOP to break: ")
    phrase = input()
    if phrase.casefold() == 'stop':
        break
    else:
        parsed_phrase = parser(phrase)
        print("Your phrase has " + str(len(parsed_phrase.split())) + " words and " + str(len(phrase)) + " characters.")