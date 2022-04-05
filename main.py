from week2 import palindrome
from week2 import math
from week2 import factorial1
from week0 import test, carrot
from week1 import liste
from week1 import fib

main_menu = [
    # ["Stringy", test.swap],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
heart_sub_menu = [
    ["Swap", test.swap],
    ["Ship Animation", test.ship],
    ["Matrix", test.driver],
    ["Carrot Animation", carrot.carrot]
]

patterns_sub_menu = [
    ["For Loop", liste.for_loop],
    ["While Loop", liste.while_loop],
    ["Recursive Loop", liste.recursive_loop],
    ["Fibonacci", fib.fibonacci],
]

triangle_sub_menu = [
    ["Factorial", factorial1.testF],
    ["Math Factor", math.factors],
    ["Palindrome", palindrome.test],
]


border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 0", heart_submenu])
    menu_list.append(["Week 1", patterns_submenu])
    menu_list.append(["Week 2", triangle_submenu])
    buildMenu(title, menu_list)



def heart_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, heart_sub_menu)

def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def triangle_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, triangle_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
