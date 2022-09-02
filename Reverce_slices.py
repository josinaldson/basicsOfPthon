ages = []
hights = []

for i in range (1,3):
    age = int(input("Enter the age of the person %i de 5" %i))
    hight = int(input("Enter the hight of the person %i de 5" %i))
    ages.append(age)
    hights.append(hight)

#agesReverse = ages[::-1]
#hightsReverse = hights[::-1]
#print(agesReverse)
#print(hightsReverse) 

ages.reverse()
hights.reverse()

print(ages)
print(hights) 

 
