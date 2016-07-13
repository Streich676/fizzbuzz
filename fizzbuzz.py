top = input("Enter the Limit") 
int(top)

num = 0

while num < top:
    num = num + 1
    if (num % 3 == 0) and (num % 5 == 0):
        print "fizzbuzz"
    elif num % 5 == 0:
        print "buzz"
    elif num % 3 == 0:
        print "fizz"
    else:
        print num