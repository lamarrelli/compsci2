import math                                                                    
k = 7                                                                      
N = 38  

n= 2**k     

P = 0                                                                
for i in range(N, n+1):                                                      
    prob = (math.factorial(n)/(math.factorial(i)*math.factorial(n-i)))*(0.25**i)*(0.75**(n-i))                                                        
    P += prob     

print(P)        

