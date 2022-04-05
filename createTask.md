{% include navigation.html %}

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
     `function myFunction()`

3cii. ```
      <p><button onclick="myFunction()">Translate</button></p>
      ```

3ciii. The identified procedure called myFunction contributes greatly to the overall structure of the javaScript code because it defines the outline for adding other features like arrays and if-else conditions.

3civ. Use a toggle switch to switch between different languages being displayed on and around the table. Then, to make the table, the use of `<td>` to generate a table. There are exactly four rows and two columns that should be displayed. Whenever there is customized text, there is a id="_" definer in the left `<td>`argument. This way, it is able to be defined and used below in the javaScript code. Then when the table is finished, use the arguments 
`<script>` to show the beginning of javaScript code. Then to make the method, use `function myFunction()`
with curly brackets surrounding it. Then define the two arrays: engTitle and chinTitle and fill them up with Strings that are involved in teh conversion process. Afterwards, you must define the variables that you want to convert using the id's that were defined earlier (Ex: 
`var x = document.getElementById("title");`). Then use if-conditional statements to let the computer know when to switch what and when. Here is when you would put the mandarin version that you want to switch to. The innerHTML should =/=== to the array in the format (ex:`chinTitle[0]`).

3di. First Call: The first call is for the toggle switch. There are two results that result from that call. The english language and the chinese language. Call it once it is chinese and call it twice, it is english.
    Second Call: The second call is to the function itself, it has a method where it calls the function so that the entire code is able to run properly and so that it is able to function efficiently.

3dii. The conditions that are tested by the first call are the if-else conditionals that determine whether or not the language displayed is English or Mandarin. 
      The conditons that are tested by the second call are the arrays and variables that are defined near the forefront of the JavaScript code.

3diii.The result of the first call is the conversion toggle between english and mandarin language.
      The result of the second call is the existance of the table and structure overall.
