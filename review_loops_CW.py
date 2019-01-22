def main():
    # exercise1()
    exercise2()
    # exercise3()



# ### Exercise 1:
# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Hint: Use 'continue' statement.
# Expected Output :
# ```0 1 2 4 5```

def exercise1():
    num = 0
    for num in range(7):
        if(num !=3 and num != 6):
                print(num)

# ### Exercise 2:
# Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers: ```numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)```
# Expected Output :
# ```
# Number of even numbers : 5
# Number of odd numbers : 4
# ```

def exercise2():
    num = 0
    even = num % 2
    odd = num % 3
    for num in range(10):
        evcounter = even+1
        odcounter = odd+1
        while(even):
            print("Number of even numbers: " + str(evcounter))
        while(odd):
            print("Number of odd numbers: " + str(odcounter))

# ### Exercise 3:
# Write a Python program that accepts a sequence of lines (blank line to terminate) as input and
# prints the lines as output after User enters a blank line to end.
# Do not use an array to hold the lines of text
# Hints:
# You can use ```"\n"``` if you want to add a line break between sentences


def exercise3():

    while True:
        x = input("Enter a sentence")
        if(x != ""):
            continue
        elif(x == ""):
            print(x)
            break



if __name__ == '__main__':
    main()

