#using the try and except methods when user tries to input a bad file name

fname = input("Enter file name")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('print'):
        count = count + 1
print(f"There were {count} subject lines in {fname}")
    
