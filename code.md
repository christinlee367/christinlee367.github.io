{% include navigation.html %}

### Data Structures project

#### [Replit Runtime](https://replit.com/@ChristinaLee6/NovelShimmeringCompilers#main.py)
#### [Github Code](https://github.com/christinlee367/christinlee367.github.io/blob/main/main.py)[Github Code](https://github.com/christinlee367/christinlee367.github.io/blob/main/test.py) 

```
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
```

```
main_menu = [
    ["Swap", test.swap],
    ["Listy", test.ship],
    ["Loopy", None],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Factors", None],
    ["GCD", None],
    ["LCM", None],
    ["Primes", None],
]

patterns_sub_menu = [
    ["Patterns", None],
    ["PreFuncy", None],
    ["Funcy", None],
]
```

<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/@ChristinaLee6/NovelShimmeringCompilers#main.py"></iframe>
