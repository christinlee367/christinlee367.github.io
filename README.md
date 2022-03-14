## Christina's Jekyll
# [REVIEW TICKET TTO T3](https://github.com/christinlee367/christinlee367.github.io/issues/1)
You can use the [editor on GitHub](https://github.com/christinlee367/christinlee367.github.io/edit/main/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/christinlee367/christinlee367.github.io/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.
### 5.1, 5.2 Notes: Digital Divide and Harmful and Beneficial Effects
5.1: Beneficial and Harmful Effects
Accelerometers: automobile industry drove price down
Used for airbag deployment and lateral movement detection
Benefits of multirotor- deliveries, harmful- flying in unregulated zones is illegal and dangerous, privacy
Benefits of Wii- active playing video games, harmful- broken TVs/ injuries
3D printers: open source software for computer and printer
Organs, prosthetics, houses, shoes, jewelry
Internet originally for scientists but now used by many people all the time
Dopamine feedback loops
Sleep deprivation, depression, anxiety, impulsivity
Microtransactions: “free” games/apps
Cosmetics paywall to functionality, pay to win
Gold, v-bucks, chips
Loot boxes- banned in some countries; gambling

5.2: Digital Divide
Digital divide: differing access to computing devices/ internet based on socioeconomic, geographic, demographic (age, religion)
Some countries computers not common in rural areas, small # of websites, internet used to protect and advocate the government


### 5.1, 5.2 notes and actions
#### Tri 3 TPT 0.1 related to Beneficial and Harmful Effects of Computing Big Idea 5.1
GitHub pages action
***
1. Come up with three of your own Beneficial and corresponding Harmful Effects of Computing
    3 Beneficial on Computing: Increase your productivity, Connects you to the Internet, Can store vast amounts of information and reduce waste
    3 Harmful Effects of Computing: Relationships and Social Skills Issues, Health Problems, Browsing Online Can Be Dangerous. 
![2](https://github.com/christinlee367/christinlee367.github.io/blob/main/wikiDopanmine.png)
2. Talk about dopamine issues above. Real? Parent conspiracy? Anything that is impacting your personal study and success in High School?
    It is still astounding that we must still require a human response to answer our most important calls. it would be better to combine this trust with machine learning. Based on the flow chart, it is also a complicated process that is not fault-tolerant at all, but it is extremely realistic. Sometimes when making important calls such as job offers, can impact my personal study and success in High School negatively.

#### 5.2 GitHub pages action -- Digital Empowerment
***
1. How does someone empower themself in a digital world?
    Empowerment in the digital world is important because it assists organizations in opening up the knowledge, experience and values that people already have. Through resources such as slack and github, students like me can express their unique talent through these tools. Then being is linked is what is important and makes our work known.

2. How does someone that is empowered help someone that is not empowered? Describe something you could do at Del Norte HS.
   Build trust. At times, it is necessary that we trust others to complete specific tasks or own certain goals without much oversight, Ask for feedback, Offer instructions. For places such as the nighthawk center, it allows students to have a safe space where they can relax. Equip with many helpful mentors and other students, they are able to gain help to be empowered in a digital world over there.

3. Is paper or red tape blocking digital empowerment? Are there such barriers at Del Norte? Elsewhere?
Red tape is particularly burdensome to smaller businesses and may act as a disincentive to new business start-ups. Paper is definitely now blocking digital empowerment because it allows people to print and put their work on paper making it easier for others to see visually and be more accessible to those who do not have a computer device.

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

### Create Task

#### [Replit Runtime](https://youtu.be/wFyg_sEB8i8)
#### [Github Code](https://github.com/christinlee367/n225_FireEradicatorsTheSequel/blob/main/templates/pbl/CTCLPBL/playlist.html)

```
if (x.innerHTML === engTitle[0]) { x.innerHTML = chinTitle[0]; } else { x.innerHTML = engTitle[0]; }

```
```
if (x.innerHTML === engTitle[0]) {
            x.innerHTML = chinTitle[0];
        } else {
            x.innerHTML = engTitle[0];
        }
```
```
const chinTitle = ["名称", "歌曲", "您好，欢迎来到识别声音。 知道危险何时到来可能意味着生与死的区别。对于我们的英语观众，请点击上方/For English Please click above", "风暴 - 立即在封闭的建筑物或硬顶车辆中寻求庇护", "龙卷风 - 当你听到这个，去一个低而坚固的地方", "火山 - 避免火山灰，通风是关键", "地震 - 躲避书架等容易掉落的物体"]
```
