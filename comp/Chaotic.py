# File: chaos. py
# A simple program illustrating chaotic behavior.
def main() :
    print("This program illustrates a chaotic function")
    X = eval(input("Enter a number between 0 and 1: "))
    Y = eval(input("Enter a number between 0 and 1: "))
    N = eval(input("Enter a number to run: ") )
    print(X,Y)
    for i in range(N) :
        X = 3.9 * X * (1 - X)
        Y = 3.9 * Y * (1 - Y)
        print(X,Y)


