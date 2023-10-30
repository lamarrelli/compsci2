n= 97
m= 16
mn_gen = [0]*m
mn_gen[0] = 1

for i in range(n-1):
    x = 0
    for y in range(m-1, 0, -1):
        x = x + mn_gen[y]
        mn_gen[y] = mn_gen[y-1]
    mn_gen[0] = x

print(sum(mn_gen))
