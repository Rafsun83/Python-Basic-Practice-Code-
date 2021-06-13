n = int(input("Enter the number: "))
f = 1
if n<0:
    print("This is invalid number")
elif n==0:
    print("This factorial is 0")
else:
   for x in range(1, n+1 ):
      f = f * x
   print(f)

