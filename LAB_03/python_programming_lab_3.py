# -*- coding: utf-8 -*-
"""Python Programming - Lab - 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sVLA1muUW0xoXho__mthqS2NFORVCVOA

<a href='https://www.darshan.ac.in/'> <img src='https://www.darshan.ac.in/Content/media/DU_Logo.svg' width="250" height="300"/></a>
<pre>
<center><b><h1>Python Programming - 2101CS405</b></center>
<center><b><h1>Lab - 3</b></center>    
<pre>

# for and while loop

### 01) WAP to print 1 to 10
"""

i=1
while i<=10:
  print(i,end=',')
  i+=1

"""### 02) WAP to print 1 to n"""

n=int(input("Enter a number:"))
i=1
while i<=n:
  print(i,end=',')
  i+=1

"""### 03) WAP to print odd numbers between 1 to n"""

n=int(input("Enter number:"))
i=1
while i<=n:
  if(i%2!=0):
    print(i,end=',')
  i+=1

"""### 04) WAP to print numbers between two given numbers which is divisible by 2 but not divisible by 3"""

n1=int(input("Enter a initial number,n1:"))
n2=int(input("Enter a terminate number,n2:"))
i=n1
while i<n2:
  if(i%2==0 and i%3!=0):
    print(i,end=',')
  i+=1

"""### 05) WAP to print sum of 1 to n numbers"""

n=int(input("Enter a nth number: "))
i=1
sum=0
while i<=n:
  sum=sum+i
  i+=1
print(f'sum of 1 to {n} number:',sum)

"""### 06) WAP to print sum of series 1 + 4 + 9 + 16 + 25 + 36 + ...n"""

n=int(input("Enter a nth number:"))
i=1
sum=0
print("Square series 1 to Nth = ",end=' ')
while i<=n:
  print(pow(i,2),end=' + ')
  sum=sum+pow(i,2)
  i+=1
print('\r')
print("sum of series: ",sum)

"""### 07) WAP to print sum of series 1 – 2 + 3 – 4 + 5 – 6 + 7 ... n"""

n=int(input("Enter a nth number: "))
sum=0
i=1
while i<=n:
  if(i%2==0):
    sum=sum-i
  elif(i%2!=0):
    sum=sum+i
  i+=1
print("Sum of the given series: ",sum)

"""### 08) WAP to print multiplication table of given number."""

n=int(input("Enter nth number for multiplication table: "))
i=1
while i<=10:
  
  print(n,'x',i ,'=',n*i )
  i+=1

"""### 09) WAP to find factorial of the given number"""

n=int(input("Enter a number: "))
i=n
fact=1
while i>=1:
  fact=fact*i
  i-=1
print('Factorial of number : ',fact)

"""### 10) WAP to find factors of the given number"""

n=int(input("Enter a number : "))
i=1
count=1
print(f"Factors of {n} =",end=' ')
while i<=n:
  if(n%i==0):
      print(i,end=',')
  i+=1

"""### 11) WAP to find whether the given number is prime or not."""

n=int(input("Enter a number:"))
flag=0
i=2
while i<n/2:
  if(n%i==0):
    falg=0
    break;
  else:
    flag=1
  i+=1

if(flag==0):
  print(f"{n} is not a prime number.")
else:
  print(f"{n} is a prime number.")

"""### 12) WAP to print sum of digits of given number"""

n=int(input("Enter a number:"))
temp1=n
sum=0
while n>=1:
  temp=n%10
  sum=sum+temp
  n=n//10
print(f"Sum of digits of number '{temp1}'= ",sum)

"""### 13) WAP to check whether the given number is palindrome or not"""

n=int(input("Enter a number: "))
temp=n
temp1=0
while n>=1:
  r=n%10
  temp1=(temp1*10)+r
  n=n//10
print(f"Revere number of {temp} = ",temp1)

if(temp==temp1):
  print(f"Number {temp} is a Palindrome number.")
else:
  print(f"Number {temp} is not a Palindrome number.")

"""### 01) WAP to check whether the given number is Armstrong or not."""

n=int(input("Enter a number:"))
temp=n
temp1=n
count=0
sum=0
count=len(str(n))
while temp>=1:
  r=temp%10
  sum=sum+pow(r,count)
  temp=temp//10
if(temp1==sum):
  print(f"Entered number {temp1} is an Armstrong number.")
else:
    print(f"Entered number {temp1} is not an Armstrong number.")

"""### 02) WAP to find out prime numbers between given two numbers."""

n1=int(input("Enter a number,n1= "))
n2=int(input("Enter a number,n2= "))
while n1<=n2:
  n=n1
  flag=0
  i=2
  while i<n/2:
    if(n%i==0):
      falg=0
      break;
    else:
      flag=1
    i+=1

  if(flag==1):
    print(f"{n} is a prime number.")
  n1+=1

"""### 03) WAP to calculate x^y without using any function."""

x=int(input("Enter amount of x : "))
y=int(input("Enter amount of y: "))
ans=1
for i in range(1,y+1):
  ans=ans*x
 
print(f"{x}^{y} = ",ans)

"""### 04) WAP to check whether the given number is perfect or not.
[Sum of factors including 1 excluding number itself]
"""

n=int(input("Enter a Number : "))
sum=0
for i in range(1,n):
  if(n%i==0):
    sum=sum+i
if(sum==n):
  print(f"number {n} is a perfect number.")
else:
  print(f"number {n} is not a perfect number.")

"""### 05) WAP to find the sum of 1 + (1+2) + (1+2+3) + (1+2+3+4)+...+(1+2+3+4+....+n)"""

n=int(input("Enter a Nth number of series : "))
sum=0
for i in range(1,n):
  for j in range(1,i+1):sum+=j
print("Sum of given series = ",sum)

"""### 06) WAP to print Multiplication Table up to n"""

n=int(input("Enter number of multiplication table,n : "))
for i in range(1,n+1):
  j=1
  while(j<=10):
    print(i,'x',j ,'=',i*j)
    j+=1