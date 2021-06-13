n = int(input("Enter the number: "))
sum = 1
for x in range(2,n+1,2):
    sum = sum * x*x

print(sum)