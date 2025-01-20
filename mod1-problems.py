# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."

print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.

#when doing math always put "import math" at the top
import math
#it is easiest to as for each number separatly and assign them with a variable
x = int(input("Give me a number for x"))
y = int(input("Give me a number for y"))
#lets show the operations as follows (respectively):
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)

# Heron's formula for area A = sqrt(s*(s-a)*(s-b)*(s-c)), but s = 0.5*(a+b+c)
#doing math so...
import math
#ask for 3 lengths of the sides of a triangle
a = int(input("Please give 3 side lengths of a triangle, starting with the first"))
b = int(input("the second"))
c = int(input("and the third"))
#now we put it all together to get the side
s = 0.5*(a+b+c)
#and finally the area
A = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area using Heron's formula is",A)

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).

#MATH
import math
# Like before, ask for each of the five numbers
a = int(input("Please provide five numbers for this statistical analysis, starting with the first"))
b = int(input("the second"))
c = int(input("the third"))
d = int(input("the fourth"))
e = int(input(" and the fifth"))
# total
total = a+b+c+d+e
print("The total of these numbers is",total)
# average
av = (a+b+c+d+e)/5
print("The average of these numbers is",av)
#minimum
min = min(a,b,c,d,e)
print("The minimum of these numbers is",min)
#maximum
max = max(a,b,c,d,e)
print("The maximum of these numbers is",max)
#standard deviation
# mu = av
# std = sqrt((sum((var-mu)**2))/4)
std = math.sqrt((((a-av)**2)+((b-av)**2)+((c-av)**2)+((d-av)**2)+((e-av)**2))/4)
print("The standard deviation of these numbers is",std)
