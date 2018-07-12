number=int(input())
count=0
if(number<=1000):
  for i in range(2,number):
    if(number%i==0):
      count=count+1
  if(count==2):
    print("yes")
  else:
    print("no")
else:
  print("no")
