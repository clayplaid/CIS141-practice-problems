#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
#provide a list of numbers
numbers = [7,4,18,5,30,5]

#make an empty list to add even numbers to
even_numbers = []
#iterate through list (use for loop)
for number in numbers:
#add even numbers to list
    if number in range(1,100,2): #can also use number % 2 == 0
        continue
    else:
        even_numbers.append(number)
#calculate sum of all even numbers
sum = sum(even_numbers)
#print sum
print(sum)

#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.
strings = ["Olympic", "College", "Olympic", "is", "Olympic", "a", "Olympic", "good", "Olympic", "college", "!"]

#counter because we are counting
counter = 0
#count through all the "Olympic"s
for string in strings:
    if string == "Olympic":
        counter += 1
print('# of "Olympic" in strings:', counter) # should be 5

#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.
strings = ["friends", "are", "fun", "to", "hang", "out", "with"]

#empty list to add to
new_list = []
#loop through strings
for string in strings:
#syntax for string longer than 3 characters
#len(string) > 3
#add string with longer than three characters
    if len(string) > 3:
        new_list.append(string)
#print new list
print(new_list)
#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.
integers = [-4, 7, 8, -3, -6, 4]

#need two sets of everything (one for positive, one for negative)
#counters
counter_positive = 0
counter_negative = 0
#empty sets
positive = []
negative = []
#loop through numbers
for integer in integers:
#syntax for positive
#integer > 0
#syntax for negative
#integer < 0
#if, else phrases/if, if phrase, both work because numbers can only be either positive or negative
    if integer > 0:
        positive.append(integer)
    else:
        negative.append(integer)
print(positive)
print(negative)

#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.
integers = [77, 12, 5, 43, 78, 90]

#new list
squares = []
#loop through intergers
for integer in integers:
#syntax for squaring
#integer ** 2
#square and add
    squares.append(integer ** 2)
#print new list
print(squares)
