import json
import random

def check_word(word):
    #clear previous data and reset data
    try:     
        with open("wordle/words.json", "r") as fp:
            l = json.load(fp)

        with open("wordle/permitted_words.json", "r") as fp:
            word_list = json.load(fp)
            
        last_word = l["words"][-1]
        if (list(last_word.values()).count("correct")) == 5 or l["count"] >= 6:
            l["words"] = []
            l["real"] = random.choice(word_list)
            l["count"] = 0
            l["success"] = False

            with open("wordle/letters.json", "r") as fp:
                letters = json.load(fp)

            d = {}

            for i in letters:
                d[i] = "null"

            with open("wordle/letters.json", "w") as f:
                json.dump(d, f, indent = 2)

        with open("wordle/words.json", "w") as f:
            json.dump(l, f, indent = 2)
    
    except IndexError:
        with open("wordle/words.json", "r") as fp:
            l = json.load(fp)

        l["words"] = []
        l["real"] = random.choice(word_list)

        with open("wordle/words.json", "w") as f:
            json.dump(l, f, indent = 2)

    #---------
    #check if word exists
    with open("wordle/permitted_words.json", "r") as fp:
        w = json.load(fp)

    if word.lower() in w:
        pass

    else:
        return "bad"

    #---------
    #Guessing

    with open("wordle/words.json", "r") as fp:
        l = json.load(fp)

    with open("wordle/letters.json", "r") as fp:
        letters = json.load(fp)

    guessed_words = []

    for i in l["words"]:
        s = ""
        for letter in i:
            s += letter
        guessed_words.append(s)

    real = l["real"]
    if word.lower() == real:
        #When the word has been guessed
        d = {}
        for letter in word.lower():
            d[letter] = "correct"
            letters[letter] = "correct"
        
        l["words"].append(d)
        l["count"] += 1
        l["success"] = True

        with open("wordle/words.json", "w") as f:
            json.dump(l, f, indent = 2)

        return "success"

    elif word.lower() in guessed_words:
        #If the word already has been guessed before
        return "exists"

    else:
        #If the word hasn't been guessed and is a legitimate word
        real_list = list(real)
        d = {}
        for letter in word.lower():
            if (letter in real_list) and  (word.lower().index(letter) == real_list.index(letter)):
                d[letter] = "correct"
                letters[letter] = "correct"
            elif (letter in real_list):
                d[letter] = "half"
                letters[letter] = "half"
            else:
                d[letter] = "null"
                letters[letter] = "wrong"
        l["words"].append(d)
        l["count"] += 1

        with open("wordle/words.json", "w") as f:
            json.dump(l, f, indent = 2)

        with open("wordle/letters.json", "w") as f:
            json.dump(letters, f, indent = 2)

        return "done"


def clean_letters():
    with open("wordle/letters.json", "r") as fp:
        letters = json.load(fp)

    d = {}

    for i in letters:
        d[i] = "null"

    with open("wordle/letters.json", "w") as f:
        json.dump(d, f, indent = 2)