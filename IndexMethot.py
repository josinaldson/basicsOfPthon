a = [1,2,3,4,5]

print(a)

x = int(input("Type value of x (from 0 to %i): " %(len(a) - 1 )))

"""
n = 0
for i in range(len(a)):
    if a[i] == x :  
        print("Indice de %i: %i" %(x,i))
        n = 1

if n != 1:
    print("%i was not founded in the list"%x )

"""    
print(a.index(x))