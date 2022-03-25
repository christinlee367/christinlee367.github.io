import time


# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "Christina",  
               "LastName": "Lee",  
               "DOB": "April 9",  
               "POB": "Edina",  
               "Email": "christinlee367@gmail.com",  
               "Owns_Cars":["Lexus "]  
              })  

InfoDb.append({  
               "FirstName": "Kaavya",  
               "LastName": "Raamkumar",  
               "DOB": "April 23",  
               "POB": "La Jolla",  
               "Email": "kaavya.r16@gmail.com",  
               "Owns_Cars":["2010 Acura"]  
              })  

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Cars: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
      

# for loop iterates on length of InfoDb- Christina Lee
#change the while loop to move argument n inside the definition - Christina Lee
def while_loop():
    n = 0
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(): # Pass an argument and sometimes do not pass an argument, so I just remove all the arguments - Christina Lee
  #Those that already have a function, then I made a new one without it and call if recursively - Christina Lee
    n = 0
    recursive_loop1(n)
    return

def recursive_loop1(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop1(n + 1)
    return # exit condition


def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion