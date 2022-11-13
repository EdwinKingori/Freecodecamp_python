#reversing string methods
# first method
# NOTE: the .reverse() method returns an attribute error..
# when anythin other than list is used.
s = "Monty python"
string = ""
for i in s:
    string = i + string
    
print(string)

#Second method

s = "Monty python"
new = s[::-1]
print(new)
     
