#Write a program that reads in the csv file linked above and outputs the mean, median, and standard deviation for the
# fall & spring semesters
#Author Lisa Dean
import statistics
#out print
def outputStats(listArray):
    print("       Fall 2016  Spring 2016")
    print("Mean:   ", round(statistics.mean(fall),2), "    ", round(statistics.mean(spring),2))
    print("Median: ", statistics.median(fall), "     ", statistics.median(spring))
    print("STD:    ", round(statistics.stdev(fall),2), "     ", round(statistics.stdev(spring),2))

# variable defined
fall = []
spring = []

# reading the file
fileName = "sample_grades.csv"
var1 = open(fileName)
def readFile(var1):
    for line in var1:  # read each line in file
        #print(line.rstrip())
        listArray = line.rstrip().split(",")
        #print(listArray[1])

        if  listArray[1] == "Fall 2016":
            fall.append(eval(listArray[2]))
        else:
            spring.append(eval(listArray[2]))

readFile(var1)
var1.close()
outputStats(fall)
