#e a function count_letter that takes a list of strings and a string
#letter as parameters and returns the number of times this letter
#occurs, both upper- & lower-cased.
#Author:  Lisa Dean
list = ["HELLO", "goodbye", "1234 Oooh!"]

def count_letter(text, chrr):
    print(text)
    count = 0
    chrr = chrr.lower()
    i =0
    #for word in text:   converting to while loop
    while i < len(text):
        word = text[i]
        count += word.lower().count(chrr)
        i += 1
    return count

def main():
    print("the number of occurances in the text: ", count_letter(list, "o"))
main()