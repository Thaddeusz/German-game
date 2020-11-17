## german gamee
# one big dictionary
# asks if it should be german-english or english-german
# shuffles
# if incorrect, save the word-pair

import random

# imports the dictionary into the variable dictionary with eval, that basically just copies it into a variable 1:1

correct_words = 0
number_of_words = 0
incorrect_words = []

while True:
    try:
        language = input(f"Welcome to the German dictionary game, you can exit by writing exit or quit. \nWould you like German-English(g) or English-German(e)? ")
        if language[0].lower() == "g" or language[0].lower() == "e":
            break
    except:
        pass

while True:
    try:
        topic = input("Which topic would you like? Food & Animals(f) or everything(e)? ")
        if topic[0].lower() == "f" or topic[0].lower() == "e":
            break
    except:
        pass
        
if topic[0].lower() == "f":
    topic_file = "food_animals.txt"
elif topic[0].lower() == "e":
    topic_file = "all.txt"
else:
    pass

with open(topic_file,'r') as inf:
    dictionary = eval(inf.read())

print(f"currently there are {len(list(dictionary.keys()))} words")

#if language[0].lower() != "g" or language[0].lower() != "e":
#    language = input("please write either e or g: ")

# reverses the dictionary
if language[0].lower() == "g":  dictionary = {v: k for k, v in dictionary.items()}

while True:
    try:
        # generate a random number
        item_number = random.randrange(0,len(list(dictionary.keys())))
        # selects the key appropiate to the random number
        key_word = list(dictionary.keys())[item_number]
        number_of_words += 1
        print(f"{number_of_words}. {key_word}")

        inp = input("\nWhat's the word in the other language? ")
        # compares answer with value
        
        if inp == list(dictionary.values())[item_number]:
            print("\x1b[6;30;42m" + "CORRECT" + "\x1b[0m")
            correct_words += 1
            dictionary.pop(key_word)
        elif inp == "exit" or inp == "quit":
                result = correct_words / number_of_words * 100
                print(f"You knew {correct_words} correct words out of {number_of_words}! That's {result}%! ")    
                print(f"You did not know these words\n {incorrect_words}")
                break
        else:
            print(f"You are incorrect, the correct word is: \033[1;32;40m {(list(dictionary.values())[item_number])} \x1b[0m \n")
            incorrect_words.append(list(dictionary.items())[item_number])
            # collects incorrect words
    except ValueError:
        result = correct_words / number_of_words * 100
        print(f"You knew {correct_words} correct words out of {number_of_words}! That's {result}%! ")
        break

    
            