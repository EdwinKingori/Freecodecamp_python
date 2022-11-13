#Nesting python for loops
def fruits():
    new_list = input("Enter a list of fruits")
    fruits_list = new_list.split()
    
    for word in fruits_list:
        print(f"The following lines will print each word of {word}")
        for letter in word:
            print(letter)
        print("")

fruits()
        
        
