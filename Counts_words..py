#e a program similar to above that counts the number of words in the files as well.
#After printing out information about each file, this program should also print the total
#number of lines & words in all 3 files. You can use the string split function to split a line
#of input into a list of words by splitting the line on spaces
file_names = ['text1.txt', 'text2.txt', 'text3.txt']

for name in range(len(file_names)):
    with open("C://Users/lrdea/Downloads/"+file_names[name]) as var1:

        dataFile = var1.read()
        contents = dataFile.split()
        wordCount = len(contents)
    print(file_names[name], " : ", len(dataFile), "lines, ", wordCount, "words. ")
