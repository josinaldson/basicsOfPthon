def potencia(base, exp):
    pot = base**exp

    return pot

print(potencia(2,3))

def soma(arg1, arg2 , arg3):
    return arg1 + arg2 + arg3 

print(soma(1,2,3))

def opMat(num1, num2):
    soma1 = num1 + num2
    return soma1, num1*num2

a,b = opMat(3,2)
print(a, b)

import random
def lancadado():
    a = random.randint(1,7)
    print(a)

lancadado()
