#a program that creates a list of 20 numbers input by the user and prints
#the average (mean) of the list
#Lisa Dean

numbers =[]
for i in range(20):
    numbers.append(eval(input("Please enter a number: ")))
get_sum = sum(numbers)
mean = get_sum / len(numbers)
print("The average mean of the list you entered : ",mean)