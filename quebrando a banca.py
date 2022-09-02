import random 
teste = int(input("Insert the number of tests"))

trocar = 0 

naoTrocar = 0

for i in range(1, teste +1):
    porta = random.randrange(1,4) 
    premio = random.randrange(1,4)

    if porta == premio:
        naoTrocar += 1 
    else:
        trocar += 1 


print("Change and Win %.3g %%"%(trocar/teste*100))
print("Change and lose %.3g %%"%(naoTrocar/teste*100)) 

