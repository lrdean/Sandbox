
Prompt = "Enter the next line in the file: "

outfilename = input("What is the name of the output file? ")
numLines = eval(input("How  many lines do you want to write?"))
# create a new file
dataFile = open(outfilename, "w")

for x in range(numLines):
    userinput = input(Prompt)
    print(userinput, file= dataFile)

dataFile.close()
