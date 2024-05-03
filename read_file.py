#Write a program that reads in the csv file linked above and outputs the mean, median, and standard deviation for the
# fall & spring semesters
#Author Lisa Dean
#
with open("C://Users/lrdea/Downloads/sample_grades.csv") as var1:
    dataFile ={}

    dataFile = var1.readlines()

print(dataFile)
i = 1
