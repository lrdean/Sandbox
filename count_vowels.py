#a function, count_e, that takes a list of strings as a parameter and
#returns the total number of upper and lower case e’s (“E” and “e”) in all the
#strings in the list.

def count_e(words):
    total_e = 0 #sum
    for str in words:
        total_e += str.upper().count("E")
    return total_e

#a function, count_vowels, that takes a list of strings as a parameter
#and returns the total number of upper and lower case vowels (A, E, I, O, U) in all
#the strings in the list.
def count_vowels(words):
    vowels = ["A", "E", "I","O","U"]
    total_vowels = 0
    for str1 in words:
        for letter in vowels:
            if letter.upper() in vowels:
                total_vowels += str1.upper().count(letter)
        #print(total_vowels)
    return total_vowels
def main():
    print("E count = ", count_e(["hi", "hello", "EEK!"]))
    print(" Vowel count = ", count_vowels(["hi", "hello", "OOF!"]))
main()
