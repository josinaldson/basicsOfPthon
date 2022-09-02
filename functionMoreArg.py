def sum(*list):
    sumNum = 0
    print(list)

    for i in list:
        sumNum += i
    
    return sumNum

a = [1,2,3,4]

print(sum(1,2,3,4,5))