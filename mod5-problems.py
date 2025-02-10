#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.
n = int(input("Please provide a positive integer. "))
#while loop, sum integers 1 to n
counter = 1
sum = 0
while counter <= n: # if n = 5
    sum += counter  
    counter += 1

#print sum
print(sum) # 1+2+3+4+5 = 15

#2. Define a string variable (e.g., my_string = "Olympic College"). Use a for loop to print each character on its own line. 
# Convert each character to uppercase before printing.
#provide string
string = "badminton"
# make for loop, one character per line
for char in string:
# convert to uppercase
    #use .upper()
# print
    print(char.upper())

#3. Use a for loop and the range() function to print all even numbers from 2 to 20.
# even numbers 2 to 20
    # 2,4,6,8,10,12,14,16,18,20
#create range
    # range(start, stop, step)
    # range(2,21,2)
#create for loop
for i in range(2,21,2):
#print
    print(i)

#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. 
# Format your output so that each row corresponds to multiplying by a specific number. Example output:
# 1 2 3 4 5         # row 1
# 2 4 6 8 10        # row 2, multiples of 2, start with 2
# 3 6 9 13 15       # row 3, multiples of 3, start with 3
# 4 8 14 16 20      # row 4, multiples of 4, start with 4
# 5 10 15 20 25     # row 5, multiples of 5, start with 5

#range(start, stop, step)

# loop for rows
for a in range(1):
# loop for row 1
    for b in range(1,6):
        print(b, " ", end='')
    print("")
# loop for row 2
    for c in range(2,11,2):
        print(c, " ", end='')
    print("")
#loop for row 3
    for d in range(3,16,3):
        print(d, " ", end='')
    print("")
#loop for row 4
    for e in range(4,21,4):
        print(e, " ", end='')
    print("")
# loop for row 5
    for f in range(5,26,5):
        print(f, " ", end='')
    print("")

# Write a program that continuously asks the user to input a number. If the user enters 0, 
# immediately stop asking for more numbers. Otherwise, print the number they entered. Sample interaction:
# Enter a number (0 to stop): 4
# You entered 4
# Enter a number (0 to stop): 7
# You entered 7
# Enter a number (0 to stop): 0
# Exiting...

# ask for number
number = int(input("Please provide a number. "))
#continuous loop
while number >= 0:
    if number == 0:
        break
    print(number)
    number2 = int(input("Please provide a number. "))
    if number2 == 0:
        break

#stop if 0 is input
#   if number == 0
#        break
