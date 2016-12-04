#Loop1
#n = any positive integer
n=2
i = 0
while i <= n:
        i = i + 1

#Outcome: Loop always finishes
        
#Loop2
#n = any positive integer
n=3
i = 1
while True:
        i = i*2
        n=n+1
        if i>n:
            break

#Outcome: Loop always finishes


#Loop3
#n = any positive integer
n=2

while n!=1:
        if n%2==0: #n is even
            n-n/2
        else:
            n=3*n+1
        

#Outcome: outcome is difficult for computer to determine
