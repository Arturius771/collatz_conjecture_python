##=======================================##
##Project Name: Collatz Conjecture
##Date Started: 16/08/2021
##Date Completed: 16/08/2021
##Artúr Foden
##www.arturfoden.ie
##=======================================##
##Calculates the path of a given integer according to the method described in the Collatz Conjecture using a recursive function. 
##=======================================##
##Language + Version: Python 3.9.4
##IDE + Version: IDLE 3.9.4
##Project Version: v1
##Lines of Code: 17
##=======================================##
##Input Integer
##Creates Variables to count steps and highest number
##Takes the number of steps and adds one to the count
##Checks if the current number is the highest so far, if yes then store it and pass it on to the next recursion
##Takes input integer
##  If even then divide by two
##  If odd then multiply by three and add one
##=======================================##

def collatz(n, c = 0, h = 0):
    c = c + 1
    if n > h:
        h = n
    if n == 1:
        print("{} is odd".format(n))
        print("We have reached the end")
        print("It took {} steps".format(c))
        print("The highest number was {}".format(h))
    else:        
        if (n % 2) == 0:
            print("{} is even".format(n))
            n = n / 2
            collatz(n, c, h)
        else:
            print("{} is odd".format(n))
            n = (n * 3) + 1
            collatz(n, c, h)
