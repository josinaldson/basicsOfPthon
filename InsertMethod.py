a = [1,2,3,4,5]

print("Lista = ",a)

x = int(input("Type value of x (from 0 to %i): " %(len(a) - 1 )))
pos = int(input("Type the positions of x (from 0 to %i): " %(len(a) - 1 )))

b = [] 

'''for i in range (len(a)):
    if i == pos:
        b.append(x)

    b.append(a[i])

a = b
print("Lista = ",a)
'''
a.insert(pos,x)
print("Lista = ",a)
