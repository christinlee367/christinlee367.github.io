{% include navigation.html %}

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

### Create Task

#### [Replit Runtime](https://youtu.be/wFyg_sEB8i8)
#### [Github Code](https://github.com/christinlee367/n225_FireEradicatorsTheSequel/blob/main/templates/pbl/CTCLPBL/playlist.html)
3ai. To inform the audience of what kind of natural dangers there are. Through the use of informing our audience through another aspect besides their eyes, we can also inform them through hearing. Sometimes through our ears, it can become the greatest warning. This way, the next time our users encounter a dangerous situation, they are able to hear it coming.

3aii. Through the use of the toggle, you can change the text language of the words so that it may be readable for our mandarin audience. Also, the user can interact with the play buttons on the right column and listen to real occurances of natural disasters that have happened before.
3aiii. The input is the language switch English to mandarin and vice versa. The output is the table displaying the different language change at the moment when the user hits the button for a language change.

3bi. `const engTitle = ["Title", "Tune", "Hello, Welcome to Identifying Sounds. Knowing when danger is coming could mean the difference between life and death. For our mandarin audience, please click above/中文在上", "Storm - Seek shelter immediately either in an enclosed building or a hard-topped vehicle", "Tornado - When you hear this, go somewhere low and sturdy", "Volcano - Avoid volcanic ash, ventilation is key", "Earthquake - Take cover and avoid objects that are easily fallen like bookshelves"]
    const chinTitle = ["名称", "歌曲", "您好，欢迎来到识别声音。 知道危险何时到来可能意味着生与死的区别。对于我们的英语观众，请点击上方/For English Please click above", "风暴 - 立即在封闭的建筑物或硬顶车辆中寻求庇护", "龙卷风 - 当你听到这个，去一个低而坚固的地方", "火山 - 避免火山灰，通风是关键", "地震 - 躲避书架等容易掉落的物体"]`

3bii. ```
        if (x.innerHTML === engTitle[0]) {
            x.innerHTML = chinTitle[0];
        } else {
            x.innerHTML = engTitle[0];
        }
        ```

3biii. list one: engTitle
       list two: chinTitle

3biv. It represents the titles or descriptions used on the page that are to be converted to another language.

3bv. If I did not use the list, I would resort to using just String in place of an array instead of putting all the strings together. Which would make the code less organized and harder to read for the lay population. 

3ci. ```
        if(f.innerHTML === engTitle[6]) {
            f.innerHTML = chinTitle[6];
        } else {
            f.innerHTML = engTitle[6];
        }
     ```
     ```
     function myFunction()
     ```

3cii. ```
      <p><button onclick="myFunction()">Translate</button></p>
      ```

3ciii. The identified procedure called myFunction contributes greatly to the overall structure of the javaScript code because it defines the outline for adding other features like arrays and if-else conditions.

3civ. Use a toggle switch to switch between different languages being displayed on and around the table. Then, to make the table, the use of `<td>` to generate a table. There are exactly four rows and two columns that should be displayed. Whenever there is customized text, there is a id="_" definer in the left 
```
<td>
```
argument. This way, it is able to be defined and used below in the javaScript code. Then when the table is finished, use the arguments 
```<script>
``` 
to show the beginning of javaScript code. Then to make the method, use 
```function myFunction()
``
with curly brackets surrounding it. Then define the two arrays: engTitle and chinTitle and fill them up with Strings that are involved in teh conversion process. Afterwards, you must define the variables that you want to convert using the id's that were defined earlier (Ex: 
```var x = document.getElementById("title");
```
). Then use if-conditional statements to let the computer know when to switch what and when. Here is when you would put the mandarin version that you want to switch to. The innerHTML should =/=== to the array in the format (ex: 
```chinTitle[0]
```
).

3di. First Call: The first call is for the toggle switch. There are two results that result from that call. The english language and the chinese language. Call it once it is chinese and call it twice, it is english.
    Second Call: The second call is to the function itself, it has a method where it calls the function so that the entire code is able to run properly and so that it is able to function efficiently.

3dii. The conditions that are tested by the first call are the if-else conditionals that determine whether or not the language displayed is English or Mandarin. 
      The conditons that are tested by the second call are the arrays and variables that are defined near the forefront of the JavaScript code.

3diii.The result of the first call is the conversion toggle between english and mandarin language.
      The result of the second call is the existance of the table and structure overall.
