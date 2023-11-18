# write a program that tells user how many letters are in their name 

# get user input 
# used length function to find length of string 
# used strip function to remove blank space 
name=input("What is your name? ").strip()
length_of_name=len(name)
print(length_of_name)


print(f"Hi {name}! You have {length_of_name} letters in your name.")