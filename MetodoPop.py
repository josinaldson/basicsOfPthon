a = [1,2,3,4,5]

print(a)

index = int(input("Type the index (from 0 to %i) to be removed: " %(len(a) - 1 )))

"""
print("Element",a[index])

b = []
for i in range(len(a)):
    if index != i:
        b.append(a[i])

a = b

print(a)

"""

print("Elemento ", a.pop(index))

print(a)

