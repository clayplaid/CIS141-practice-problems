'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''
#I do not already have a file named gardening_tips.txt so lets make one

file = open("gardening_tips.txt", "w")
file.write("These are tips for gardening:\nUse mulch.\nControl pests and disease.\nWater properly.\n")
file.close()

with open("gardening_tips.txt", "r") as file:
    print(file.read())
'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''
file = open("hiking_log.txt", "w")
file.write("")
file.close()

file = open("hiking_log.txt", "a")
while True:
    name = input("What is the name of the hike? Press 0 to exit.")
    if name == "0":
        break
    distance = input("What is the distance, in km, of the hike? Press 0 to exit.")
    if distance == "0":
        break
    file.write(name + "\t" + distance + "\n")
file.close()

with open("hiking_log.txt", "r") as file:
    print(file.read())
'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''
with open("song_lyrics.txt","r") as file: #want everything lowercase to avoid case senitivity
song = file.read().lower()
    
words = [] #list for words inputted
for i in range(5): #
    word = input("Enter a word you want to find the frequency of: ").lower() #all numbers enter lowercase to align with words in song
    words.append(word) # now have a list

frequency_of_words = {} #dictionary for words and their count
words_in_song = song.split() #turn song into individual words
for word in words: #for each word inputted that is in the list
    counter = 0 #to be added when each word appears in song
    for song_word in words_in_song: #go through each word in the song
        if song_word == word: #each time the a word from song is the same as the word inputted, counter goes up by 1
            counter += 1
    frequency_of_words[word] = counter #format to associate the word inputted to its counter
print(frequency_of_words)
'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
'''
file = open('poll.txt', 'r')
list = file.read()
file.close()
votes = list.split(",")
yea = 0
nay = 0
for vote in votes:
    if vote == "yea":
        yea += 1
    elif vote == "nay":
        nay += 1
print("There are", + yea, "yea votes.")
print("There are", + nay, "nay votes.")
