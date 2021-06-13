import math
n = int(input("enter the number: "))
count = 0
val = int(math.sqrt(n))

for x in range(2, val+1, 1):
    if (n % x) == 0:
        count = 1
        break
if count==0:
    print(n, "prime")
else:
    print(n, "not prime")














