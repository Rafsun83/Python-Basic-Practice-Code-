import math
n = int(input("Enter the Number of people: "))
m = int(input("Enter the number of position: "))
k = 1
f = n-m

for i in range(f+1, n+1):
    k = k * i
print(f"This postion is {k}")