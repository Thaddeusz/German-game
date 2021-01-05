## german gamee
# one big dictionary
# asks if it should be german-english or english-german
# shuffless
# if incorrect, save the word-pair

import random
import os,sys
# imports the dictionary into the variable dictionary with eval, that basically just copies it into a variable 1:1

os.chdir(sys.path[0]) # sets the current directory to the script's directory, so we do not need to use absolute path link for the files below

correct_words = 0
number_of_words = 0
incorrect_words = []

while True:
    try:
        language = input(f"Welcome to the German dictionary game, you can exit by writing exit or quit. \nYou can skip a question with \"PASS\"\nWould you like German-English(g) or English-German(e)? ")
        if language[0].lower() == "g" or language[0].lower() == "e":
            break
    except:
        pass

while True:
    try:
        topic = input("Which topic would you like?\nFood & Animals(f)\nAdjectives & Verbs(v)\nClothes & Nature(n)\nPronouns and conjuctions?(c)\nPlaces, tools, accusative pronouns, house?(h)\nPeople, Family and questions(q)?\nNumbers, Food2, Money(m)\nFamily2, Prepositions2, Body, Some(s)\nShopping, Transportation(t)\nJobs, Colors, Imperative(i) \neverything(e)? ")
        if topic[0].lower() in "fvnchqmstie":
        #if topic[0].lower() == "f" or topic[0].lower() == "e" or topic[0].lower() == "v"  or topic[0].lower() == "n" or topic[0].lower() == "c" or topic[0].lower() == "h" or topic[0].lower() == "q" or topic[0].lower() == "m" or topic[0].lower() == "s" or topic[0].lower() == "j":
            break
    except:
        pass
        
if topic[0].lower() == "f":
    topic_file = "food_animals.txt"
elif topic[0].lower() == "v":
    topic_file = "adjectives_verbs.txt"
elif topic[0].lower() == "n":
    topic_file = "clothes_nature.txt"
elif topic[0].lower() == "c":
    topic_file = "pos_pron_conjuctions.txt"
elif topic[0].lower() == "h":
    topic_file = "places_tools_acc_house.txt"
elif topic[0].lower() == "q":
    topic_file = "people_family_questions.txt"
elif topic[0].lower() == "m":
    topic_file = "numbers_etc_food2_money.txt"
elif topic[0].lower() == "s":
    topic_file = "family2_prep2_body_some.txt"
elif topic[0].lower() == "t":
    topic_file = "store_transport.txt"
elif topic[0].lower() == "i":
    topic_file = "jobs_colors_imperative.txt"
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
        print(f"{len(list(dictionary.keys()))}: {key_word}")

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
        elif  "PASS" in inp:
            correct_words += 1
            print(f"The correct word is: \033[1;32;40m {(list(dictionary.values())[item_number])} \x1b[0m \n")
            dictionary.pop(key_word)

            
        else:
            print(f"You are incorrect, the correct word is: \033[1;32;40m {(list(dictionary.values())[item_number])} \x1b[0m \n")
            incorrect_words.append(list(dictionary.items())[item_number])
            # collects incorrect words
    except ValueError:
        result = correct_words / number_of_words * 100
        print(f"You knew {correct_words} correct words out of {number_of_words}! That's {result}%! ")
        print(f"You did not know these words\n {incorrect_words}")
        break

    
            
