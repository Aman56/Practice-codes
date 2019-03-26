# Program to calculate the surface area and volume of a sphere.
# By Aman

import math
pii=math.pi
def main():
    r=float (input("Enter the radius of the sphere: "))
    
    volume= (4*pii*(r**3))/3
    area= 4*pii*(r**2)
    print ("The volume is ",volume," and the area is ",area)

def pizza():
    d=float(input("Enter the diameter of the pizza: "))
    price=float(input("Enter the price of the pizza: "))
    area= (pii*(d**2))/4
    price_per_sq_inch=price/area
    print("Price per sq inch is ",price_per_sq_inch)

def organic():
    carbon=float(input("Enter the number of carbon atoms: "))
    oxygen=float(input("Enter the number of oxygen atoms: "))
    hydrogen=float(input("Enter the number of hydrogen atoms: "))
    molecular_weight=hydrogen*1.00794+carbon*12.0107+oxygen*15.9994
    print("The molecular weight is ",molecular_weight)

def slope():
    x1,y1=eval(input("Enter the first coordinates(x,y): "))
    x2,y2=eval(input("Enter the second coordinates(x,y): "))
    slope=(y2-y1)/(x2-x1)
    print("The slope of the line joining the two points is ",slope)

def distance():
    x1,y1=eval(input("Enter the first coordinates(x,y): "))
    x2,y2=eval(input("Enter the second coordinates(x,y): "))
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("The distance between the points is ",distance)

def epact():
    year=int(input("Enter the year:  "))
    c=year//100
    epact=(8+(c//4)-c+((8*c+13)//25)+11*(year%19))%30
    print("The epact is ",epact)

def triangle():
    a,b,c= eval(input("Enter the sides of the triangle: "))
    s=(a+b+c)/2
    q=s*(s-a)*(s-b)*(s-c)
    if q>=0:
        area= math.sqrt(q)
        print("The area of the triangle is ",area)
    else:
        print("The area cannot be found.")

def ladder():
    height=float(input("Enter the height: "))
    degree=float(input("Enter the angle in degrees: "))
    radians=(pii*degree)/180
    length=height/math.sin(radians)
    print("The length of the ladder is ",length)

def n_sum():
    n=int(input("Enter a natural number: "))
    summ=(n*(n+1))/2
    print("The sum of ",n," natural numbers is ",summ)

def series_sum():
    n=int(input("The total numbers in the series: "))
    series_sum=0
    for i in range(n):
        j=float(input("Enter the number: "))
        series_sum+=j
    print("The sum of the series is ",series_sum)

def average():
    n=int(input("Enter the total numbers in the series: "))
    series_sum=0
    for i in range(n):
        j=int(input("Enter the number: "))
        series_sum+=j
    average=series_sum/n
    print("The average of the series is ",average)

def approx_pi():
    n=int(input("Enter the number of terms: "))
    count=1
    approx=0
    for i in range(1,n+1,2):
        count+=1
        approx=(((-1)**count)/i)*4

    diff=math.pi-approx
    print ("The approximate value of pi is:  ",approx," and precision is ",diff)
