#sorting by values
tuple_list = {'a':10, 'b':1, 'c':22}
tmp = list()
for k,v in tuple_list.items():
    tmp.append((v,k))

print (tmp)
tmp = sorted(tmp, reverse = True) # sorts the items in the tuple in the decending ording
print (tmp)

#or replacing the above for loop with this shorter version.
print(sorted([(v,k) for k,v in tuple_list.items()], reverse=True))
