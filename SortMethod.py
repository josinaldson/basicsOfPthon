from operator import le


a = [4,2,5,3,1]

print("Lista = ",a)

"""
c = 0

for i in range(len(a)):
    for j in range (len(a)):
        if a[i]<a[j]:
            c = a[i]
            a[i] = a[j]
            a[j] = c



"""
a.sort()
print("Lista = ",a)
