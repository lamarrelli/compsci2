def fib(n, k):
    pairs_rab = [0]*(n + 1)
    pairs_rab[1] = 1
    
    for month in range(2, n + 1):     #we calculate the number of rab for each month up to n 
        pairs_rab[month] = pairs_rab[month-1] + k*pairs_rab[month-2] #ty fibonacci :)
    
    return pairs_rab[n]

n, k = 36, 4

Fib = fib(n, k) #creativity is my passion 

print(Fib)