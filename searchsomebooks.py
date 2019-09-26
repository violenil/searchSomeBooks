import nltk
from nltk.book import *


text = None
textOptions = [text1, text2, text3, text4, text5, text6, text7, text8, text9]
textNum = None
print("""
The above are texts you may search and perform processes on. Please select one by entering its number.
(Enter q/Q to exit)
""")

while text is None:
    textSelect = input("Text to process: ")

    if textSelect == "q" or textSelect == "Q":
        exit()
    elif textSelect in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        textNum = int(textSelect)
        text = textOptions[textNum - 1]
    else:
        print("That is an invalid choise. Please choose a text or exit.")

print("Great! You've selected " + str(text) + ". What do you want to do with it?")

choice = None

#while choice is None:
#    print("""
 #   1) Concordance
  #  2) Find Similar Words to Mine
   # 3) Find Common Contexts
    #4) Dispersion Plot
    #5) 

