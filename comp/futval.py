# futval . py
# A program to compute the value of an investment
# carried 10 years into the future
def main () :
    print ("This program calculates the future value")
    years= eval(input("Enter the number of years: "))
    initial_sum=0
    apr =eval (input ("Enter the annual interest rate: ") )
    for i in range (years) :
        principal=eval (input ("Enter the initial principal: ") )
        initial_sum+=principal
        initial_sum = initial_sum * (1 + apr)
        print ("The value in",i,"  years is: ", initial_sum)
