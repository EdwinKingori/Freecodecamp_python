#reversing string methods
# NOTE: the .reverse() method returns an attribute error when anythin other than list is used.
#  first method
def first_method():
    s = "Monty python"
    string = ""
    for i in s:
        string = i + string
    print(string)
first_method()


#Second method
def second_method():
    s = "Monty python"
    new = s[::-1]
    print(new)
     
second_method()

#Third method
def third_method(string):
    
    string = "".join(reversed(string))
    
    return string

s = "Monty Python"

print(third_method(s))

# fourth method:
# Transform to list
# Reverse the string
# Then join the string
def fourth_Method():
    string = "Monty python"
    s = list(string)
    s.reverse()
    return "".join(s)
print(fourth_Method())

#Fifth method:
def main():
    string = "Today is a good day"
    string_length = len(string)

    for i in range(string_length-1, -1, -1):
        print(string[i], end="")

    print()
    print(string)

main()
#Sixth Method
def reverse_words(text):
    reversed_text = ""
    word = ""

    for char in text:
        if char != " ":
            word = char + word
        else:
            reversed_text += word + " "
            word = ""

    reversed_text += word  # Add the last word (without space)
    
    return reversed_text

# Test case
test = reverse_words("elbuod decaps sdrow")
print(test)  # Output: "elbuod  decaps  sdrow"
