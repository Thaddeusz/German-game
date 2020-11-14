## german gamee
# one big dictionary
# asks if it should be german-english or english-german
# shuffles
# if incorrect, save the word-pair

import random

# imports the dictionary into the variable dictionary with eval, that basically just copies shit 1:1
with open('all.txt','r') as inf:
    dictionary = eval(inf.read())


incorrect_words = []

language = input(f"Welcome to the German dictionary game, currently there are {len(list(dictionary.keys()))} words. \nYou can exit by writing exit or quit and also write show or pass to show the current word. \nWould you like German-English(g) or English-German(e)? ")
#if language[0].lower() != "g" or language[0].lower() != "e":
#    language = input("please write either e or g: ")

# reverses the dictionary
if language[0].lower() == "g":  dictionary = {v: k for k, v in dictionary.items()}

while True:
    # generate a random number
    item_number = random.randrange(0,len(list(dictionary.keys())))
    # selects the key appropiate to the random number
    key_word = list(dictionary.keys())[item_number]
    print(key_word)

    inp = input("\nWhat's the word in the other language? ")
    # compares answer with value
    if inp == list(dictionary.values())[item_number]:
        print("\x1b[6;30;42m" + "CORRECT" + "\x1b[0m")

    elif inp == "exit" or inp == "quit":
            print(incorrect_words)    
            break
    else:
        print(f"You are incorrect, the correct word is: \033[1;32;40m {(list(dictionary.values())[item_number])} \x1b[0m \n")
        incorrect_words.append(list(dictionary.items())[item_number])
        # collects incorrect words
            