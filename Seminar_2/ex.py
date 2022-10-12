sp = []
for i in range(3):
    sp1=[]
    for j in range(3):
        sp1.append(99)
    sp.append(sp1)

for i in range(len(sp)):
    print(sp[i])

sp.insert(0,[8,9])
print("------")

sp.remove([8,9])
a=sp.pop(-1)

print(a)
print("одномерный список")
print(a[::-1])
a=a + [15,11,99]
print(a)
print(a[2:5])
