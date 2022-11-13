#file

xfile = open("reverse.py")
for cheese in xfile:
    print (cheese)

# Reading the whole file
# using the read() method
fhand = open ("reverse.py")
inp =  fhand.read()
print(len(inp))
print("")
print(inp[:20])

#Searching through the file
# the rstrip() strips the whitespace from the white side if the string.
fhand = open("largest.py")
for line in fhand:
    #line = line.rstrip()
    if line.startswith("num"):
        print(line)       
