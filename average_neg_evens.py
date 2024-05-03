#a function average_neg_evens that takes a list of numbers as a
#parameter, and adds all the negative even numbers (less than 0 and
#divisible by 2) together and returns their average.
#Author:  Lisa Dean

def average_neg_evens(list):
    i = 0  #count
    numb = 0 #sum numbers

    for num in list:
        if num < 0  and num % 2 == 0:
           #print(numb, num)
           numb += num
           i += 1

    return numb / i #avg
def main():
    print("Average: ", average_neg_evens([0, 1, 2, -2, -3, -4, 4, 4]))

main()