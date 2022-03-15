{% include navigation.html %}

## Christina's Jekyll [github repo](https://github.com/christinlee367/christinlee367.github.io)
# [REVIEW TICKET TTO T3](https://github.com/christinlee367/christinlee367.github.io/issues/1)
You can use the [editor on GitHub](https://github.com/christinlee367/christinlee367.github.io/edit/main/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/christinlee367/christinlee367.github.io/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

#### Menu Challenge
1. Build your own menu and sub-menu
[main.py](https://github.com/christinlee367/christinlee367.github.io/blob/main/main.py)
2. Add swap and keypad from Tri 2 Week 10, to your project and menu.
3. For additional challenge and review, build a Christmas tree with *s or a pattern of your choice
image
4. Add two items below to get ready for animations and interacting with terminal codes
[animation and swap.py](https://github.com/christinlee367/christinlee367.github.io/blob/main/test.py)
5. Here's an example of a ship pattern. Implement it in your project and make your own pattern following the example.
I used a bunny example on a canoe

### Data Structures project
#### [Replit Runtime](https://replit.com/@ChristinaLee6/NovelShimmeringCompilers#main.py)
#### [Github Code](https://github.com/christinlee367/christinlee367.github.io/blob/main/main.py)[Github Code](https://github.com/christinlee367/christinlee367.github.io/blob/main/test.py) 

```markdown
# menuy.py - function style menu

import test

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

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"



def patterns_submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, patterns_sub_menu)
    m.menu()


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenu])
    menu_list.append(["Patterns", patterns_submenu])
    buildMenu(title, menu_list)

def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)

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
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
