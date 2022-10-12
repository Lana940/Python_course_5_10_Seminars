book={}

book['Миша'] = 98465566
book['Саша']=[64654464,46546464]

print(book)

if 'Саша' in book:
    print("Yes")
else: print("No")

for x,y in book.items():
    print(x, y)

for x in book.values():
    print(x)

for x in book.keys():
    print(x)