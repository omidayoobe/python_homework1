# Python Homework Exercise 4
#
print("..........Exercise 4..................... ")
print(' ')


username = input("Hi there,Whats your name?")

print("Welcome " + username + " lets make a your together")
input('press enter to start your story')
print(' ')

story = {} #empty hash

story ['Hero'] = input("please type in your favourite hero ") # created a new value and assigned the user input to it
story ['Beginning'] = input("Now write the beggining of your story ") # created a new value and assigned the user input to it
story ['Middle'] = input("Now write the middle of your story ") # created a new value and assigned the user input to it
story ['End'] = input("that sounds interesting, now write an amazing ending ") # created a new value and assigned the user input to it

print(' ')
input('now press enter to view your amazing story')
print(' ')
print("Once there was the Almighty" + ' ' + story['Hero']) # Concatenating th hero with text
print(story['Beginning']) #print beginning
print(story['Middle']) #print beginning
print(story['End']) #print beginning

#print (story) #printing the whole has (story)
