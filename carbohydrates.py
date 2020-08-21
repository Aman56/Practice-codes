# Multiple functions to accomplish tasks.
import math
def carbohydrate():
    h=int(input(("No. of H atoms: ")))
    c=int(input(("No. of c atoms: ")))
    o=int(input(("No. of O atoms: ")))
    weight=1.00794*h+12.0107*c+15.9994*o
    print(weight)
def distance():
    x,y=map(int,input("Enter Coordinates: ").split())
    p,q=map(int,input("Enter Coordinates: ").split())
    distance=math.sqrt((p-x)^2+(q-y)^2)
    print(distance)
def length():
    height=int(input("Enter Height: "))
    degree=float(input("Enter the angle: "))
    angle=(math.pi/180)*degree
    length=height/math.sin(angle)
    print(length)
def total():
    n=int(input("Enter length of the series: "))
    a=[int(x) for x in input().split()]
    total=0
    for i in a:
        total+=i
    print(total)
def average():
    n=int(input("Enter length of the series: "))
    a=[int(x) for x in input().split()]
    total=0
    for i in a:
        total+=i
    avg=float(total/n)
    print(avg)
def find_pi():
    n=int(input("Enter length of the series: "))
    new_sum=0
    for i in range(n):
        new_sum=new_sum+math.pow(-1,i)/(2*i+1)
    my_pi=4*new_sum
    print(my_pi)
    accuracy=math.pi-my_pi
    print(accuracy)
def fibonacci():
    n=int(input())
    a=[1,1]
    for i in range(2,n):
        a.append(a[i-1]+a[i-2])
    if(n==1 or n==2):
        print(int("1"))
    else:
        print(a[n-1])
def guess():
    x=int(input("Enter number: "))
    n=int(input("Enter no. of guesses: "))
    guess=x/2
    for i in range(n):
        guess=(guess+(x/guess))/2
    print(guess)
    accuracy=math.sqrt(x)-guess
    print(accuracy)
        
