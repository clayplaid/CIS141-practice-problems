'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
'''
#Test: can(1), immutable (4), supercalifragilisticexpialidocious (16)
#input: string (input)
#Output: number
#Function body: counter (make sure local or else won't increase), use for loop to cycle through word, 
                #use if statements for each vowel, return counter (number) because that is the result we want, print inputs

def count_vowels(input):
    counter = 0
    for char in input:
        if char == "a":
            counter += 1
        if char == "e":
            counter += 1
        if char == "i":
            counter += 1
        if char == "o":
            counter += 1
        if char == "u":
            counter += 1
    return counter

print("There are", count_vowels("supercalifragilisticexpialidocious"), "vowels.")
'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
'''
#Test: racecar (True), pikachu (False), Racecar (True)
#input: string (s)
#Output: True or False, Boolean
#Function body: lowercase s, flips and save to new variable (flipped_s), and then compare s & flipped_s

def is_palindrome(s):
    lower_s = s.lower()
    flipped_s = lower_s[::-1]
    return (lower_s == flipped_s)
    
print(is_palindrome("pikachu"))
print(is_palindrome("Racecar"))
print(is_palindrome("racecar"))
'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
'''
# Test: "Water", "Fire"/"Fire", "Water"/"Electric", "Grass"
# Input: two strings (attacker, defender)
# Output: "Super Effective", "Not Very Effective", or "Neutral"
# Function body: each input has two parts, first evaluate attacker, then defender, one condition each so use if to find 
#                desired result return effectiveness for each set. print each set requested by problem

def type_advantage(attacker, defender):
    if attacker == "Water" and defender == "Fire":
        return "Super Effective"
    elif attacker == "Fire" and defender == "Water":
        return "Not Very Effective"
    else:
        return "Neutral"

print(type_advantage("Water", "Fire"))
print(type_advantage("Fire", "Water"))
print(type_advantage("Electric", "Grass"))

'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''
# Test: 100 w/ vehicle (100, yes), 100 w/o vehicle (100, no), 50 w/ vehicle (50, yes) , 50 w/o vehicle (50, no), 7 (7, no) and (7, yes)
# Input: age and vehicle
# Output: integer (fare)
# Function body: if function for age (adds amount), if function for vehicle (adds amount)

def ferry_fare(age, vehicle):
    price = 0
    if age >= 65 and vehicle == True:
        price += 15
        return price
    elif age >= 65:
        price += 5
        return price
    if age >= 19 and vehicle == True:
        price += 20
        return price
    elif age >= 19:
        price += 10
        return price
    else:
        return price

print(ferry_fare(100, True))
print(ferry_fare(100, False))
print(ferry_fare(50, True))
print(ferry_fare(50, False))
print(ferry_fare(7, True))
print(ferry_fare(7, False))
'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''
#Test: 86 XP, 157 XP, 350 XP
#input: integer (experience)
#Output: Level 1, Level 2, Level 3
#Function body: if statements for each increment of XP, return the associated level

def level_up(experience):
    if experience >= 200:
        return "Level 3"
    elif experience >= 100:
        return "Level 2"
    else:
        return "Level 1"

print(level_up(350))
print(level_up(157))
print(level_up(86))
