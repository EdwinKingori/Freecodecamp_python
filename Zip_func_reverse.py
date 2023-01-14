#using the zip function to concatenate two list index-wise
# The zip() function takes two or more iterables (like, list, dict, string), aggregates them in a tuple and returns it.

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

for i, j in zip(list1, list2):
    list3 = i+j
    print(list3,"\t", end="")
