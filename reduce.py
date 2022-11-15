from functools import reduce

expenses = [
  ('Dinner', 80),
  ('car repair', 120)
]

#sum = 0
#for i in expenses:
  #sum += i[1]
#replacing the for loop with a reduce function
sum = reduce(lambda a,b: a[1]+ b[1], expenses)

print(sum)