# About the project
The game of Wordle seems to be a pretty famous one. I tried to take inspiration from it, and build a more simplistic website that helped me learn a lot more about web development, and also play around with different tools that could be used.

## Getting started
You could simply fork the project or download it. It does require some external modules to function. To use them, simply run:
```
pip3 install -r requirements.txt
```
It would be better to use `python3.8.x` to run this code.

## About the site
The site is still under development with this being only an initial release. It uses a JSON file to store words, and doesn't have any database connectivity as of now (which will be changed later). It also does not use cookies, so can be used for only one person at a time. There is only a choice of 4 possible words, but can be changed in the code.

It was build primarily using [Django template language](https://docs.djangoproject.com/en/4.0/ref/templates/language/) and [Bootstrap templating](https://getbootstrap.com/docs/5.1/getting-started/introduction/)