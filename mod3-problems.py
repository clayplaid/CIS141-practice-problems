# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.
#ask for a word
word = input("Please provide a word")
repeat = int(input("how many times would you like this word to be repeated?")) #make sure this is a number otherwise it is a string

# use * for repetition 
print(word * repeat)

#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
#Need name and age
user_name = input("Please provide your name.")
age_int = int(input("And your age")) #needs to be int so math can be preformed
age_str = str(age_int) #when put into phrase (at the end), age cant be int
#next years age
next_year = str(age_int + 1) #user_age is int but when we put into phrase it has to be str
#print(type(next_year))

#TELL EM
print("Hello, " + user_name + "! You are " + age_str + " years old. Next year, you will be " + next_year + " years old.")

#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)
#ask for sentence
sentence = input("please provide a sentence.")
#ask for word
word = input("provide a word to find.")
#determine if word exists in sentence
print(word in sentence)

#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.
#ask for word
word = input("Please provide a word.")
f_index = int(input("And a first index"))
l_index = int(input("As well as a last index. cannot be longer than word."))
#slice word
print(word[f_index:l_index])

#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.
#provide three word
phrase = "pipe dividing sentence"
#split with spaces because str are immutable
new_phrase1 = phrase.split(" ") #this makes it into a list
#use join to put | in between words
new_phrase2 = "|".join(new_phrase1)
print(new_phrase2)
