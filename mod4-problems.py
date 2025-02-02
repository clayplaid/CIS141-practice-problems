#1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False. Your truth table should be commented out (as it's not valid Python code!)
# 1. List variable
# A and B

# 2. Determine the Number of Rows
# 2 possibilities for A
# 2 possibilities for B
# 2 x 2 combinations for A&B = 4

# 3. Create Table Columns
# A B   (A AND B)   (NOT B)     (A AND B) OR (NOT B)

# 4. Enumerate All Possible (A, B) Combinations
# A B   (A AND B)   (NOT B)     (A AND B) OR (NOT B)
# T T   
# T F   
# F T     
# F F     

# 5. Fill Each Row with Sub-Expression Results
# A B   (A AND B)   (NOT B)     (A AND B) OR (NOT B)
# T T      T           F                 T
# T F      F           T                 T
# F T      F           F                 F
# F F      F           T                 T


#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".
sensor = int(input("What is the daylight sensor reading? "))
if sensor < 8:
    print("Headlights On")
else:
    print("Headlights Off")


#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. Print True if the user’s balance is below $100; print False, otherwise.
# Ask for balance
balance = int(input("Please state the balance of your bank account. "))

# If statement for balance < $100, print true
if balance < 100:
    print(True)

#Else statement for if it is more than $100, print false
else:
    print(False)
    
    
#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.
# ask for age
age = int(input("Please state your age for movie restrictions. "))

#determine which age gets to watch what
# G -> age < 13 
# PG-13 -> 13 to 17 (in between ages means we have to use elif)
# R -> age > 18
# write if statement (have to start with highest number because we are using elif)
if age >= 18:
    print("You can see R rated movies.")
# write elif statments
elif age > 12:
    print("You can watch PG-13 movies.")
# write else statement
else:
    print("You can watch G rated movies.")
    
    
#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping.
# ask for order total
total = float(input("Please state the total of the order you are shipping. "))
final_total = str(5 + total)

# if statement for total < $50
if total < 50:
    print("Your total after shipping will be $" + final_total + ".")
    
# else statement for total >= $50
else:
    print("You earned free shipping! Your total will be $" + str(total) + ".")
