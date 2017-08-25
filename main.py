#   main.py
#   WriteSomething_Python
#
#   This program will help you get the size of a phrase given by the user, and let you
#   know if that size is an even or odd number.
#
#   Python interpreter: 3.6
#
#   Author: León Felipe Guevara Chávez
#   email:  leon.guevara@itesm.mx
#   date:   May 29, 2017
#

#   We ask the user for a phrase and read it
phrase = input("Write something:")

#   We get the size of our phrase (the number of characters in our phrase)
phraseSize = len(phrase)

#   We identify if the phrase size is an odd or an even number.  We do this dividing the size by
#   two.  If the remainder of such division is 0, then it is an even number; otherwise, it is an
#   odd number
if (phraseSize % 2) == 0:
    phraseSizeIs = "even"
else:
    phraseSizeIs = "odd"

#   We display our findings
print("Your phrase's size is " + str(phraseSize) + " characters and that is an " + phraseSizeIs + " number.")
