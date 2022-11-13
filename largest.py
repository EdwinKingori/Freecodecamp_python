# Finding largest value in an array

num = [3,9,29,45,75,86]
largest = num[0]
    
for i in num:
    if i > largest:
        largest = i
        
print (" The largest value is:", largest)


#or

num = [3,9,29,45,75,86]
max_number = max(num)
print (" The largest value is:", max_number)
