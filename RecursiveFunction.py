def fat(n):
    if n == 1:
        return n
    return fat(n-1) * n

print(fat(5))
print(fat(1))
print(fat(3))