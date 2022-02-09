#from django.http import HttpRequest
# from django.template import loader
from django.http import request
from django.shortcuts import render
import bleach
from .forms import wordle
import json

from .helper import check_word

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = wordle(request.POST)
        # check whether it's valid:
        if form.is_valid():

            guess = bleach.clean(form.cleaned_data['guess'])

            l = check_word(guess)


            with open("wordle/words.json", "r") as fp:
                lp = json.load(fp)

            #If the word has been guessed before
            if l == "exists":
                return render(request, 'game.html', {'form': form, 'details' : lp["words"], 'count' : lp["count"], "exists" : True})

            #If the word count has touched 6
            elif lp["count"] == 6:
                if lp["success"]:
                    #If the correct word has been guessed
                    return render(request, 'gameover.html', {'details' : lp["words"], 'count' : lp["count"], 'success' : True})
                else:
                    #If the user has failed to guess the right word
                    return render(request, 'gameover.html', {'details' : lp["words"], 'real' : lp["real"]})

            elif lp["words"] != []:
                form = wordle()
                if l == "success":
                    #If the user has guessed the word before 6 guesses
                    return render(request, 'gameover.html', {'details' : lp["words"], 'count' : lp["count"], 'success' : True})
                else:
                    if l == "bad":
                        #If the word is not a legitimate word
                        return render(request, 'game.html', {'form': form, 'details' : lp["words"], 'count' : lp["count"], 'bad' : True})
                    else:
                        #If the word is legitimate, and word count is less than 6
                        return render(request, 'game.html', {'form': form, 'details' : lp["words"], 'count' : lp["count"]})

            else:
                form = wordle()
                if l == "bad":
                    #if first guess is a word that does not exist
                    return render(request, 'game.html', {'form': form, 'count' : lp["count"], 'bad' : True})
                else:
                    #If the word exists
                    return render(request, 'game.html', {'form': form, 'count' : lp["count"]})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = wordle()

    return render(request, 'game.html', {'form': form})

def index(request):
    return render(request, 'game.html')