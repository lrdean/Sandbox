

def count_e(words):
    total_e = 0 #sum
    for str in words:
        total_e += str.upper().count("E")

    return total_e
def count_vowels(words):
    vowels = ["A", "E", "I","O","U"]
    total_vowels = 0
    for str1 in words:
        for letter in vowels:
            total_vowels += str1.upper().count(letter)
        #print(total_vowels)
    return total_vowels
def main():
    print("E count = ", count_e(["hi", "hello", "EEK!"]))
    print(" Vowel count = ", count_vowels(["hi", "hello", "OOF!"]))
main()
