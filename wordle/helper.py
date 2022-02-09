import json
import random

def check_word(word):
    #clear previous data
    try:
        with open("wordle/words.json", "r") as fp:
            l = json.load(fp)
            
        last_word = l["words"][-1]
        if (list(last_word.values()).count("correct")) == 5 or l["count"] >= 6:
            l["words"] = []
            l["real"] = random.choice(["frame", "strap", "cigar", "prank"])
            l["count"] = 0
            l["success"] = False

        with open("wordle/words.json", "w") as f:
            json.dump(l, f, indent = 2)
    
    except IndexError:
        with open("wordle/words.json", "r") as fp:
            l = json.load(fp)

        l["words"] = []
        l["real"] = random.choice(["frame", "strap", "cigar", "prank"])

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

    real = l["real"]
    if word.lower() == real:
        #When the word has been guessed
        d = {}
        for letter in word.lower():
            d[letter] = "correct"
        
        l["words"].append(d)
        l["count"] += 1
        l["success"] = True

        with open("wordle/words.json", "w") as f:
            json.dump(l, f, indent = 2)

        return "success"

    elif word.lower() in l["words"]:
        #If the word already has been guessed before
        return "exists"

    else:
        #If the word hasn't been guessed and is a legitimate word
        real_list = list(real)
        d = {}
        for letter in word.lower():
            if (letter in real_list) and  (word.lower().index(letter) == real_list.index(letter)):
                d[letter] = "correct"
            elif (letter in real_list):
                d[letter] = "half"
            else:
                d[letter] = "null"
        l["words"].append(d)
        l["count"] += 1

        with open("wordle/words.json", "w") as f:
            json.dump(l, f, indent = 2)

        return "done"