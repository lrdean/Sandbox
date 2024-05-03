by Lisa Dean
def while_1():
    i = 1
    while i <= 5:
        print(i)
        i += 1

def while_1b():
    j=2
    while j <= 11:
        print(j)
        j +=3
def while_1c():
    k = -10
    while k <= 0:
        print(k, end =" ")
        k += 2
def while_1d():
    l = 0
    while l <= 4:
        print("*" * 4)
        l += 1
def while_2(text):
        chr =[]
        chr = list(text)
        print(chr)
def while_3():
    numb = []
    prompt = "Please enter a number ( zero to finish): "
    num_list = eval(input(prompt))
    while num_list != 0:
        numb.append(num_list)
        num_list = eval(input(prompt))
    print(sorted(numb))
    print("sum = ", sum(numb))
    print("Average = ", sum(numb) / len(numb))
def main():
    while_1()
    while_1b()
    while_1c()
    while_1d()
    while_2("CSCI 150")
    while_3()

main()