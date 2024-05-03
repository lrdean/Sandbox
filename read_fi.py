#a python program that reads 3 files called test1.txt, text2.txt, and text3.txt, counts
#the number of lines in each file, and prints out the number of lines to a file counts.txt.
file_names = ['text1.txt', 'text2.txt', 'text3.txt']

with open("C://Users/lrdea/Downloads/"+file_names[0]) as var1:
    dataFile = var1.readlines()
converted =""
i = 0
while i < len(dataFile):
    converted = converted + "-" + dataFile[i]
    i = i + 1
     #   (key, val) = line.split()
      #  dataFile[int(key)] = val

print(converted, len(dataFile))
i = 1
