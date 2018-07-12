number=int(input())
if(number<=1000):
  for i in range(2,number):
    if(number%i==0):
      flag=1
    else:
      flag=0
  if(flag==1):
    print("no")
  else:
    print("yes")
else:
  print("no")
