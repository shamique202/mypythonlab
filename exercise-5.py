# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it


# fibonacci sequence:
def fib(n): 
    if n >2:
        return n
        else: 
            return fib(n-2) + fib(n-1)
            for num in range(1,50):
                print("term:" + str(num) + "/number:" + str(fib(num)))