# splitting
words = "His e-mail is q-lar@freecodecamp.org"
pieces = words.split()
parts = pieces[3].split("-")
n = parts[1]
print(n)

items = "first;second;third"
new_item = items.split()

new_item = items.split(';')
print(new_item)
