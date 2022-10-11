<template>
  <!-- eslint-disable -->
  <div>
    <NavBar />
    <div class="info">
      <section id="about_megan">
        <h1>About Megan</h1>
        <p>
          I'm currently a student at the Middlesex School, and I've always been
          interested in word games and crosswords. At some point I started
          making my own crosswords, and then I learned the basics of coding to
          help with the crossword-making-process (things like finding words that
          started with 'a' and ended with 'b' to fit into the crossword, etc.).
          <br /><br />
          Eventually, I had almost the entire crossword-generating process
          automated, and I decided I wanted to start sharing them with the
          world! Unfortunately, there's no website where anyone can share their
          own crosswords, so I learned how to build my own website to display my
          own crosswords and made the displaying code available for anyone to
          download and use!<br /><br />
          Below is my developer log -- it details my entire learning journey
          from learning the basics of Python to learning how to build crosswords
          and websites.
        </p>
      </section>
    </div>
    <section id="about_crosswords">
      <h1>The Megan's Mrosswords Process</h1>
      <p>
        Chronological details of how I learned to generate crosswords and create a website to display them. You can also view all the source code of the crossword generator
        and website <a href='github.com' target='_blank'>here.</a>
      </p>

      <h2 class="devlog_title">
        Learning programming words to find crossword words
      </h2>
      <p id="date">June 26, 2020</p>
      <div class="devlog_text">
        <p>
          After months of doing dozens of crosswords a week, I decided to start making my own. The most frustrating
          part of the process was always racking my brain and Googling "words that start with 'a' and end with 'z'" 
          for hours at a time, and so I set out to learn the basics of coding to write a program that would
          figure it out for me. I chose Python because I heard it was the
          most beginner-friendly language, and learned about 'strings'
          (sequences of characters that can form words and phrases), 'loops'
          (code that runs again and again without you have to write each
          iteration), and 'dictionaries' (key/value pairings where each 'key'
          has an associated 'value').<br /><br />
          The first issue I ran into was figuring out how to access a literal
          dictionary of words in Python. Luckily, learning about Python
          dictionaries before was very helpful, and I was able to load a JSON
          file as a Python dictionary where each 'key' was a word in the English
          language and each 'value' was the definition of that word. By using
          'dictionary.keys()', I was able to get a list of all the words as
          strings, and then I was able to loop through this list of words in
          order to find words that fit my requirements. <br /><br />For example,
          if my crossword looked like this:<br />
          <img src="~/assets/example_crossword1.png" />
          <br />

          Then I'd loop through the list of words to find words that started
          with 't' and had three letters. This is how my code looked:

          <pre>
    def find_word_test(number_of_letters, requirements):
    # requirements is key: string index, value: required letter for that string index
      possible_words = []
      for word in words: # words is all words in the dictionary
          if len(word) != number_of_letters:
              possible_words.append(word)
      for word in possible_words:
          for requirement in list(requirements.keys()):
              if word[requirement] != requirements[requirement]:
                  possible_words.remove(word)
      return possible_words
            </pre>
          In this example, since we're looking for a word that has three letters and starts with 'T', we'd call find_word_test(3, {0: 'T'}). 
          The code would first loop through every word and save every word with 3 letters to 'possible_words', and then it would loop through
          every word in 'possible_words' and check if the word fulfills every requirement passed in by checking if the letter at the words' requirement index
          is equal to the required letter. Since we only have one requirement, it would just check if the potential word's 0th index (first letter) was a 'T'.

        <br><br>
        With this code, I was able to cut down a lot on the time I spent looking for words and could focus on thinking of clever words and hints - the interesting 
        part of making crosswords. 
        </p>
      </div>

      <h2 class="devlog_title">
        Starting to Generate Crosswords
      </h2>
      <p id="date">September 7, 2020</p>
      <div class="devlog_text">
        <p>
          I had really enjoyed writing a little bit of code to help with finding words, so I felt confident in writing some more code to build an entire crossword for me. 
          At this point, I really understood the basic process of making a crossword since I had made so many, and set out to replicate the process by coding. However, when
          I first started, I tried to create a full-fledged, complex crossword with lots of adjacent words that looked like this:<br>
<img src="~/assets/example_crossword2.png" style="width:400px;" />
<br>
          But I realized the process for creating a crossword like this programmatically was too difficult for my current understanding, so I took a step back and instead wrote some code that resulted in a crossword like this:
          <br>

          <img src="~/assets/example_crossword3.png" style="width: 400px;" />
          <br>

          This was a lot more simple because I didn't have to worry about figuring out how to deal with gaps in the crossword, or with the overall shape of the crossword. 
          However, I still struggled a lot to go from finding a word to fill in a single gap to finding enough words to fill an entire crossword. The first issue I ran into
          was how to store a crossword in Python. I ended up going with a 2D list - a list of lists - where each sub-list was the list of letters for a row. 
          For example, the above crossword would be stored as <br>

          <pre>
          [["E", "G", "G", "S"], 
          ["P", "A", "I", "N"],
          ["I", "N", "R", "O"], 
          ["C", "A", "N", "T"]]
          </pre>
          <br>

          To fill the crossword, I started with an empty 2D list where instead of having letters, each element in the list was a " " (blank space). I then randomly chose an index in the array
          to start building the crossword from, and randomly generated a word to fill in the indexes of the array. For example, if I chose to start at the index (0, 0) (the top left) and generated the word 'EGGS', (0, 0) of the list would become 'E', (0, 1) would become 'G', and so on until (0, 3) becomes 'S'. 
          At the last letter of the word, I then generated a new word that started with the last letter of the previous word using the find_word_test function from earlier, and then added it vertically at the index of the previous word. For example, if I chose to add the word 'SNOT', (0, 4) of the list would remain an 'S' (from the 'EGGS'). Whenever the code ran into an issue, it would try every letter in the alphabet at the position where an issue was occuring to see if any words were viable (along with the previous 'find_word_test' function), and if not, it would stall or break the code loop.
          
          This method often resulted in the code getting stuck; it would typically generate 2 or 3 words, and then realize that no words fit the necessary constraints for the remaining words on the crossword. I didn't know to fix this, so I tried moving to a smaller, 2x2 crossword in order to test and debug the logic behind my code.<br><br>
          It turned out that my general logic was correct - I just had to apply the 'finding words' function from my previous post to find words that fit into the constraints. If I ran the code often enough, the random words picked for the 2x2 generator would often fulfill the crossword constraints and become a real crossword, such that my first ever generative crosswords looked like this:
          <br>

          <img src="~/assets/example_crossword6.png" style="width: 600px;" />

          <br>

          There were obviously some issues here. For one, it used the same words twice; for another, it was generating the crossword by my own constraints--my code didn't know how to assign the word numbers on the crossword by itself, or figure out where the words on the crossword needed to be. I'd have to manually define the parameters for every single crossword template I wanted to use, and that sounded even more tedious than my original problem of finding letters to fit constraints. Additionally, a 2x2 crossword wasn't very fulfilling. However, I was really excited to see that I was capable 
          of generating a crossword at all, although at the time this crossword wasn't "beautified" or user-friendly either; it was just printed to the Python console like this: 
          <br>

          <img src="~/assets/example_crossword7.png" style="width:400px;" />
          <br>

          I knew there were still a lot of things that I had to work on to accomplish my goal, but I was really proud of what I had accomplished in this dev log!

          P.S. After I figured out the bugs and flaws in my code logic, I was able to generate crosswords off any hole-less square/rectangular template/size. Take a look at these for example:

          
          <img src="~/assets/example_crossword8.png" style="width:400px;" />
          <img src="~/assets/example_crossword9.png" style="width:400px;" />

          <br>

          The only limit was how long it took to generate them--the bigger the crossword template (e.g. if it was a 4x4 vs a 14x14), the longer it took to randomly find a viable combination of letters as the number of combinations that existed became a lot smaller. As a result, I knew this wouldn't be viable for any type of final product.

          </p></div>
    </section>

    <h2 class="devlog_title">
        Using Crosses to Generate Crosswords
      </h2>
      <p id="date">December 21, 2020</p>
      <div class="devlog_text">
        <p>

          I thought that my next step with the crossword generator should be to start building crosswords with more interesting shapes and designs. To start off with, I wanted to get my crossword generator to be able to adapt to any template, and also to be able to handle 'holes', or gaps, in the template.
          <br>
          I figured a grid would be a good place to start, because the shape was conceptually similar to the crosswords I was previously generated and there weren't words stacked on top of or next to each other, and so I only had to worry about one or two constraints per word.
         
          If a 3x3 square from the previous post was represented as a template like this: [[1, 1, 1], [1, 1, 1], [1, 1, 1]], then a 3x3 square with a hole in the middle would look like this: [[1, 1, 1], [1, 0, 1], [1, 1, 1]]. I didn't want to have to generate the numbers and word locations of each 
          template I used, so after a <b>lot</b> of testing and trial and error, I came up with this function:

          <br>
          <pre>
def get_crossword_words(template):

    horizontal_words = []

    # getting horizontal words

    for a in range(len(test_crossword)):
        new_word = []
        for b in range(len(test_crossword[0])):
            if template[a][b] == 1:
                new_word.append((a, b))
            else:
                if len(new_word) > 0:
                    horizontal_words.append(new_word)
                    new_word = []
        if len(new_word) > 0:
            horizontal_words.append(new_word)
            new_word = []

    transposed = [[template[j][i] for j in range(len(template))] for i in range(len(template[0]))]

    words = []
    # getting vertical words
    for a in range(len(transposed)):
        new_word = []
        for b in range(len(transposed[0])):
            if transposed[a][b] == 1:
                new_word.append((a, b))
            else:
                if len(new_word) > 0:
                    words.append(new_word)
                    new_word = []
        if len(new_word) > 0:
            words.append(new_word)
            new_word = []

    flipped_words = []
    for word in words:
        flipped_word = []
        for coord in word:
            flipped_coord = (coord[1], coord[0])
            flipped_word.append(flipped_coord)
        flipped_words.append(flipped_word)

    vertical_words = flipped_words

    for word in flipped_words:
        horizontal_words.append(word)

        word_list = []
    for wc in horizontal_words:
        if len(wc) > 1:
            word_list.append(wc)

    return word_list
          </pre>

          <br>

          What this function returns is a two dimensional list where every element in the 'bigger' list is a list of coordinates corresponding to one word on the crossword. The way it's finding the words in the crossword template is that it's looping through 
          every coordinate in the crossword template, and keeping track of a new_word list of coordinates that gets: 
          <br>
          - appended to with a coordinate whenever the current coordinate is storing a 1 (a letter) 
          <br>
          - appended to the 'bigger' list of all coordinates whenever the previous coordinate was a letter, but the current coordinate is a 0 (a gap, signifying an end of the current word), and then set to an empty list ([])
          <br>
          - ignored if the current letter is a 0 (gap) and the previous letter is also a gap (e.g. there's nothing in new_word)
          <br>
          This worked really well for the horizontal words, but for the vertical words, I had to find a clever solution; I rotated the crossword using the 'transposed' syntax (tbh I didn't fully understand this, but it worked) - and then applied the same formula
          as before to find the vertical words. However, I did have to re-flip the coordinates (again for reasons I didn't fully understand, but it did work). This took a lot of debugging, but now I can automatically find the words in any crossword template no matter how big or small!

          <br><br>

          Given this list of word coordinates, I also wrote a function that assigns each one to a number until all of them had been assigned. It didn't perfectly replicate what most hand-made crosswords look like, but there was an organization to the system and I think I'll come back to this at a later date. If you want to see the code for it,
          it's on the Github as the generate_word_numbers function in crossword.py

          <br><br>

          With these new helper functions and some other modifications to my source code, I was able to produce crosswords with real structures and gaps like this:
          <br>




          <pre>
              [['O', 'U', 'T', 'S', 'T', 'E', 'P'],
              ['P', ' ', 'O', ' ', 'H', ' ', 'R'],
              ['P', 'O', 'S', 'T', 'E', 'R', 'O'], 
              ['O', ' ', 'H', ' ', 'R', ' ', 'C'], 
              ['S', 'O', 'R', 'C', 'E', 'R', 'Y'], 
              ['E', ' ', 'E', ' ', 'O', ' ', 'O'], 
              ['R', 'E', 'D', 'E', 'F', 'E', 'N']]</pre> where each " " is an empty space (black square).<br>

            <br>
            These crosswords ended up looking like this:<br>


          <img src="~/assets/example_crossword10.png" style="width:600px;"/>
          <br>
          <br>
          I'd managed to go from square crosswords with little structure to structured, almost-real looking crosswords, and I had figured out a schema to actually convert any template I wanted into a format readable by my program! However, there were still some issues that I needed to get creative to fix, and that won't get fixed in this dev log: 
          As with the previous crossword iterations, these still struggled to fit a real word into every template, and as the templates got larger, it became more time consuming to generate a single one. 


        </p>
      </div>

      <h2 class="devlog_title">
        Displaying The Crosswords (Building a website!)
      </h2>
      <p id="date">March 5, 2021</p>
      <div class="devlog_text">
        <p>
          The original intent of this crossword project was to generate infinite crosswords for myself so that I could entertain myself indefinitely. Up until this point, I was preoccupied with learning the fundamental skills
          required to generate the crosswords, but I figured since I was able to generate almost-real looking crosswords, I should take some time to format them and make them interactable. Previously, I was just printing out my crosswords to check them such that they looked like this: 
          <br>
          <img src="~/assets/example_crossword11.png" style="width:600px;"/>
          <br>
          These crosswords weren't interactable, and they were already filled--I needed them this way to check to make sure they were valid and 'looked' right--but now that I was confident in my crossword generation program, I wanted to make an interface for them to be interacted and used. 
          I wanted the crosswords to start with every grid empty, and to have the hints shown next to the crossword (like a real crossword). I also wanted each hint on the crossword to have an associated number. This screenshot from USAToday's crossword (my favorite crossword and crossword user interface!) was my inspiration:
          <br>
          <img src="~/assets/example_crossword12.png" style="width:500px;"/>
          <br>
          I looked into various user interface technologies to display my technology, and I narrowed my options down to two: Tkinter and HTML. I liked Tkinter because it was already in Python--the only language I knew how to code in at the time--and the code required to make any type of user interface looked pretty simple. However, I knew at some point I wanted to put my website onto the Internet and have other people
          view my crosswords, and I felt really out of my depth to set up a website using only Python (I only understood one or two words in every sentence describing how to do it). HTML, on the other hand, was a completely new language to me but it looked relatively simple to set up and 'host' a website using HTML, so I set out to learn enough of it to build a website prototype.
          This is how my first attempt looked:
          <br>
          <img src="~/assets/example_crossword13.png" style="width:600px;"/>
          <br>
          The biggest issue was this was that if I wanted to change the width of an input box (in order to make it a square, like in most crosswords), it wouldn't retain the square 'form' I wanted it to have. This is what I mean:
          <br>
          <img src="~/assets/example_crossword14.png" style="width:600px;"/>
          <br>
          Fortunately, HTML has a 'grid' display feature and this seemingly solved all my problems. For this example 4x4 crossword, I set the display to equal 'grid' rather than the default setting and set the grid width and box width to equal numbers that resulted in something that looked like a crossword. Here's the result:
          <br>
          <img src="~/assets/example_crossword15.png" style="width:600px;"/>
          <br>
          With some more styling, I managed to get it to look like this: not bad, all things considered! 
          <br>
          <img src="~/assets/example_crossword16.png" style="width:600px;"/>
          <br>
          There were still two issues though: I couldn't figure out a good way to get the numbers of each word to appear on the corresponding input box, and I didn't have a way to display gaps yet. The gaps was easily fixed - I just used an 'id' attribute to specify which input boxes were gaps, and set the attribute's background color to black. <br><br>For the numbers, however, I had to look into absolute positioning and the 'float' style attribute.
          At first, I thought I could just specify the absolute position/coordinates of each number and then generate them programmatically (e.g. if we know there are 4 rows and 4 columns, we can just generate the coordinates of each number by adding a certain width and/or height to each number's position). This solution did work, but I wanted to learn more about HTML so I set out to find a more HTML-oriented solution, which is how I came across the 'float' attribute. 
          I initially thought 'floating' each number to its corresponding box would do the trick if I wrapped everything in a div, but unfortunately everything got layered on top of itself such that it looked like this: 
          <br>
          <img src="~/assets/example_crossword17.png" style="width:400px;"/>
          <br>
          I couldn't figure out a perfect solution with my currently styling, so I changed things up - instead of having the input boxes be colored black or white, I gave the div <b>wrapping</b> the input box a color, and then let the input box itself be transparent and borderless. This solved an issue I was noticing where the input box would take layer-precedent over the crossword number no matter what, and also made it so that you couldn't enter/interact with
          the gaps. The end result looked like this:
          <br>
          <img src="~/assets/example_crossword18.png" style="width:600px;"/>
          <br>
          I really enjoyed the process of figuring out how to layout my website and crossword in HTML, and it was a breath of fresh air from working with printed, uninteractable crosswords as well as from working in my messy Python crossword.py file. For my next dev log, I might look into re-writing some of the Python code and seperating it into more than just one or two functions, and also into how I can try automatically formatting my crosswords into this HTML format. 
        </p>

      </div>

      <h2 class="devlog_title">
        Learning 'JavaScript' and making sure user crosswords are right!
      </h2>
      <p id="date">May 2, 2021</p>
      <div class="devlog_text">
        <p>
          Last month, I figured out how to display my crosswords using HTML. This month, I focused on how I could show the user that they had completed the crossword correctly, since finishing is the most rewarding part of doing a crossword! I also had to figure out how to display the correct answers to the user in case they were stuck. 
          To do this, I knew I needed to learn 'JavaScript' beacuse it was brought up repeatedly in the HTML tutorials I looked at. 
          The first thing I needed to figure out was how to get the values of every input box, and the solution I went for first was to assign each one an unique ID, and then get the value of that element in JavaScript. Thus, each input box ended up looking like this in HTML: <mark>&lt;input type="text" placeholder=" " id="1"&gt;&lt;/input&gt;</mark>, and the corresponding JavaScript looked like this: <mark>var pos1 = document.getElementById('1').value</mark>.
          <br><br>
          Therefore, to check that all of the users' input was correct and that the crossword was completed, I just needed a big if statement that looked like this: 
          <br>
          <mark>
            if (pos1 == 'A' && pos2 == 'B' && pos3 == 'C' && pos4 == 'D'
       && pos5 == 'E' && pos6 == '' && pos7 == '' && pos8 == 'F'
       && pos9 == 'G' && pos10 == '' && pos11 == '' && pos12 == 'H'
       && pos13 == 'I' && pos14 == 'J' && pos15 == 'K' && pos16 == 'L'){
        alert("Congratulations! You completed this Mrossword!")
    }
          </mark>
          <br>

          I also figured out pretty quickly that you could set the value of an input box with the same code - instead of just getting the input/value, you can set the value like so: <mark>document.getElementById('1').value = 'C'</mark>
          I also realized that users could enter upper or lower case values, so to make sure my crossword checker didn't get broken for that reason, I changed the 'checking' if statement to look  like this: <mark>if (pos1.toUpperCase() == 'A'</mark>
          <br><br>

          The last thing I had to do was add a button to show the answers for stuck users, and this is when I realized that JavaScript was really cool beacuse it allowed for easy two way interactivity with the website. All I had to do was add a function call to a button, like so: <mark>&lt;button onclick="showAnswers()"&gt;Show Answers&lt;/button&gt;</mark>, and add the function in my JavaScript code like so: <br>
          <mark>
            function showAnswers(){
        document.getElementById('1').value = 'A'
        document.getElementById('2').value = 'B'
        document.getElementById('3').value = 'C'
        document.getElementById('4').value = 'D'
        document.getElementById('5').value = 'E'
        document.getElementById('8').value = 'F'
        document.getElementById('9').value = 'G'
        document.getElementById('12').value = 'H'
        document.getElementById('13').value = 'I'
        document.getElementById('14').value = 'J'
        document.getElementById('15').value = 'K'
        document.getElementById('16').value = 'L'
    }
          </mark>

          <br><br>
          Here are some pictures and videos of the two working: <br>
          <img src="~/assets/example_crossword20.png" style="width:500px;"/>
          <img src="~/assets/example_crossword21.gif" style="width:200px%;"/>
          All in all, I've learned in the past three months that making websites is actually pretty easy; I'm sure designing super complex websites and animations is more difficult, but the core concepts make sense and are a lot more intuitive than I thought they would be!

        </p>
      </div>

      <h2 class="devlog_title">
        Putting my crosswords onto the internet
      </h2>
      <p id="date">June 19, 2021</p>
      <div class="devlog_text">
        <p>
          After building the website, I wanted to put it online. I thought this would be an easy, 2 hour task because I'd used website generators like Squarespace before and those websites were always 'generated' and put on the Internet for you, but the process turned out to be pretty complicated.
          <br><br>
          After looking around at various options, I tried to install 'Vue', a JavaScript 'framework' that was supposed to make things more simple, and host my website on DigitalOcean, but found both to be needlessly complicated for what I wanted to accomplish. Eventually, I settled on GitHub pages. What appealed to me was that you could apparently upload your website and set it up without using the Terminal, but I ended up still using the Terminal and 'git' to upload my files to my Github.
          Now that I've written down what I did, it doesn't seem like it was particularly hard to upload and host a website, but it took more than a dozen hours to ultimately get it figured out. Regardless, here's how it ended up looking: 
        </p>
        <br>
          <img src="~/assets/example_crossword19.png" style="width:100%;"/>
          <br>

      </div>

      <h2 class="devlog_title">
        "Refactoring" and crosswords with real shape
      </h2>
      <p id="date">October 18, 2021</p>
      <div class="devlog_text">
        <p>
          I had been dreading working with my original crossword.py file for months at this point (this dread was actually part of the reason why I shifted to building a website and user interface for the crosswords instead of continuing to make them better). I'd been working on this same file basically since I started learning how to code, which was almost a yera and a half ago, and so whenever I looked over the previous code, I was finding a lot of inconsistencies and potential bugs that were
          giving my anxiety. Furthermore, I wasn't comfortable with functions and global variables, 'returns', and input/output when I started writing this code, so there was a lot of repeat code. To make matters even worse, some of the repeat code also wasn't consistent--for example, the 'minimum number of viable words' variable that I had changed every time I needed it throughout the code. I decided that before I kept trying to make my crossword generator better, I should rewrite and organize some of the code
          and save some time debugging in the future. <br><br>
          This doesn't make for a super interesting dev log, but after multiple refactoring sessions, I went from having only 4 functions -- a generate_word_numbers function, a print_crossword function, a get_crossword_words function, and a function that checked for possible words given a constraint -- into having 18 functions. I also removed a lot of commented out old/broken code, and a lot of obsolete/redundant/repeat code, and these combined efforts resulted in the line count going from 2200 lines down to 650. It was no longer a pain to scroll through the document, which in and of itself was a huge win for me. 
          <br><br>
          This was an unexpectedly informative dev log / process - I got a much better understanding of how functions and the 'event loop' work, and honestly feel like I understand my own code better now in a way that allows me to better improve it in the future. 
          <br><br>
          To test out my refactoring, I also started generating crosswords based on templates that weren't simply grids. I didn't change much in the actual algorithm, but here are some examples of the crosswords I can now generate (with nice styling on the website/crossword too!): <br><br>
          <img src="~/assets/example_crossword22.png" style="width:500px;"/>
          <img src="~/assets/example_crossword23.png" style="width:500px;"/>
        </p>
      </div>

      <h2 class="devlog_title">
        Moving to larger templates
      </h2>
      <p id="date">December 29, 2021</p>
      <div class="devlog_text">
        <p>
          I was really proud of my code after having refactored it, and thought that it would be able to generate crosswords from any template. As a result, I took some of the larger templates from my favorite crossword organizations (USAToday, NYTimes, etc.) and converted them into a format that my generator could read, 
          but unfortunately I wasn't able to generate a single crossword with more than half the fields filled out after more than 10,000 'runs' of the algorithm. Here's an example of one of the templates I was using: 
          <br>
          <img src="~/assets/example_crossword12.png" style="width:400px;"/>

          <br>
          After a lot of debugging, I figured out that the reason my crossword generator couldn't handle crosswords of this size/complexity was because of required words that were 10+ letters long. Official crosswords often have hints like 'PUBLISHORPERISH' (Career advice that may be purely academic), or 'ANNAJULIACOOPER' (A Voice from the South' author, 1892), and there simply aren't that many English words that are this long. As a result, whenever my crossword generator gets to a requirement like this, the chances are really small that it'll be able to find a word that not only fulfills the length requirement, but also the constraints of the words around it.
          I didn't know what to do at first, but after a few days of thinking, it dawned on me that I could simply also add names and proper nouns to my crossword generator! To do this, I downloaded a dataset of 'famous biographies' from <a href='https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/28201' target='_blank'>Pantheon, a Harvard research project.</a> I then used the below Python code to convert the database into a JSON.<br><br>
          <pre>
            ans = []
with open("pantheon.tsv") as f:
    # Read data line by line
    for line in f:
        # split data by tab
        # store it in list
        l = line.split('\t')

        # append list to ans
        ans.append(l)

# print data line by line

d = {}

for i in ans:
    name = i[1]
    from_specific = i[3].capitalize()
    from_country = i[5].capitalize()
    job = i[13].lower()

    formats = ["{job} from {from_country}", "famous {job} from {from_country}"] # remember to .capitalize()

    clue_f = random.randint(0, 1)
    clue_f_two = random.randint(0, 1)
    f = ""
    if clue_f_two == 0:
        f = formats[clue_f].format(job=job, from_country=from_country)
    else:
        f = formats[clue_f].format(job=job, from_country=from_specific)
    f = f[0].upper() + f[1:]
    f = unidecode(f)

    clue_r = random.randint(0, 2)
    clue = ""
    if clue_r == 0 or clue_r == 1:
        clue = name
    elif clue_r == 2:
        clue = name.split(" ")[0]
    clue = unidecode(clue)
    clue = clue.replace(" ", "")
    clue = clue.upper()
    regex = re.compile('[^a-zA-Z]')
    # First parameter is the replacement, second parameter is your input string
    clue = regex.sub('', clue)


    d[clue] = f
    print(clue, ":", f)
    #print(i)

with open('names.json', 'w') as outfile:
    json.dump(d, outfile)
          </pre>
          
          What this code is doing is basically parsing the database into a 2D list for every famous person in the database, and then using the name (either the full name, or last name, as is seen in most crosswords) as the 'word' and then the famous persons' job description and geographical origin (e.g. 'United States' or 'Boston') to generate a hint for them. I also added in elements of random-ness to model after a real crossword's hints involving famous people. 
          <br><br>
          For example, Abraham Lincoln could be 'ABRAHAMLINCOLN': President of the United States from Kentucky, or 'LINCOLN': President from the United States. I took these names and 'hints' and then turned them into a JSON, and then added the plaintext from that JSON to my original 'dictionary' JSON and my crosswords were suddenly able to have words and names as clues!
          <br><br>
          Unfortunately, while the odds of getting a name that could fulfill both the length and constraint requirements in a crossword were higher -- I was able to generate 2 crosswords in 10,000 tries -- generating crosswords was still too slow for my liking, so I scaled down the size of the complicated crosswords slightly to be able to have a better variety of crosswords. Here are some examples of new crosswords I could generate: 
          <br><br>
          <img src="~/assets/example_crossword24.png" style="width:500px;"/>
          <img src="~/assets/example_crossword25.png" style="width:500px;"/>
          <br>
          Notice the new hints like 'Philosopher from the United Kingdom' or 'Writer from Gaomi'. I repeated the same process for cities and states using data from <a href='https://simplemaps.com/data/world-cities' target='_blank'>SimpleMaps</a>, and ended up with over 2000 new 'longer' word and hint combinations to choose from.

        </p>
      </div>
        
      <h2 class="devlog_title">
        Better Clues with Artificial Intelligence
      </h2>
      <p id="date">March 29, 2022</p>
      <div class="devlog_text" id="devlog_ai">
        <p>
          I've been really busy with school recently, but had some free time over spring break and in the past few months to come up with ways to improve my crossword generator. The biggest issue with my generator right now, in my opinion, is that the hints aren't "clever"--I love hints in 'official' crosswords that make you think and make you smile when you answer them, and although my crossword hints make you think (in the sense that you have to figure out what the word is), the hints aren't as 'clever' or 'punny' as I'd like them to be.
          <br><br>
          I read some articles about GPT-3, an AI that generates text based on the prompts you give it, and was curious if it would work for the purpose of generating crossword hints. 
          I played around with it using <a href='beta.openai.com' target='_blank'>OpenAI</a> for a bit, and I was amazed at what it could do. If I told it to generate an article with a specific prompt, or a story with a specific set of events, it generated cohesive stories with 'real' narratives and detail, and it was for the most part difficult to tell that they were AI generated at all. However, when I gave it the prompt '3 puns with the word 'crossword', I was expecting something like "1. Words that are crossed; 2. Mad words; 3. Words that are all jumbled up" but instead got this: <br><br>
          <pre>
           Prompt: 3 puns with the word 'crossword'

            1. I'm not good at crosswords, I'm more of a Sudoku person.
            2. I completed the crossword in record time!
            3. I'm stuck on this crossword clue, can anyone help?
          </pre>
          I tried a lot of different prompts and tried to 'trick' the AI into giving me some puns; here are some other examples:
          <pre>
            Prompt: Define 'crossword' without using the word 'crossword'

            A puzzle in which words are written forward, backward, or across, 
            each in a separate line, usually with clues for each word, and often 
            with blank spaces between the words to separate them.
          </pre>

          <pre>
            Prompt: What is a 'crossword' without using the word 'crossword'

            A puzzle that consists of a grid of squares and blanks into which words
            written across and down are to be fitted, each word being read left to right 
            or top to bottom and intersecting with another word.
          </pre>      
          <br>
          The best results that I was able to get were by changing the 'temperature' (defined as 'randomness') to 1 (the max), and lowering the maximum length to the size of a crossword hint. It resulted in some clues like this:
          <pre>

            Prompt: Define 'crossword' without using the word 'crossword'

            A word puzzle that normally takes the form of a rectangular grid of white
          </pre>
          <br>
          However, most of the time the results ended up being more like this:
          <pre>
            Prompt: Give me a pun about space

            I'm sorry, I couldn't hear you over the sound of the incredible vastness of space.

          </pre>
          <br>
          I don't really know anything about AI or 'machine learning' barring having read a couple introductory articles, but this result made sense to me; there's not really any way to impart semantic meaning of words to computers/programs (and if there was it would probably be too complicated for me to grasp, especially without any formal understanding of the concepts involved)
          and as a result it's probably even more impossible to not only impart the semantic meaning of words but also have the computer generate creative puns based on that meaning. Regardless, I found the GPT-3 AI almost impressively scary. That being said, college applications are coming up for me, and I jokingly gave it the prompt of generating a 'college application essay about crossword puzzles', and it gave me this:
          <pre>
            College application essay about making a crossword puzzle

            Making puzzles and crosswords is part of my daily routine i've never considered it a hobby,
             but it's a way of life i wake up in the morning and while eating breakfast, i.

            College application essay about making a crossword puzzle body paragraphs of an essay, 
            the writer should quizlet ukraine research paper quilling @georgia_xoxx.

            Research papers in education journal impact factor test basic essay format outline java 
            personal essay for college application format questions essay on application.
          </pre>
          <br>
          So we still have a ways to go. Regardless, I still wanted to start incorporating puns and word-play into my crosswords, and so I went with my fallback plan of finding a database of puns and manually finding a word in the pun to use as the word, and the pun itself to use as the hint. I then used the same process as I did in the last devlog to incorporate these hints into the crossword generator. 
          There weren't that many puns, and so the pun-to-regular-hint ratio isn't as high as I would like, but it's a start, and playing with the GPT-3 AI was a lot of fun and very insightful.          
          
        </p>
      </div>

      <h2 class="devlog_title">
        Full Website Building
      </h2>
      <p id="date">August 22, 2022</p>
      <div class="devlog_text" id="devlog_ai">
        <p>
          It's been a while, but I've been busy! After APs/exams, I had a lot of time to work on the crossword generator and I made a couple small improvements to make the process/algorithm more efficient, the hints more interesting, the word base larger, and the overall program easier to use. 
          <br><br>
          When summer started, I also got the chance to take an introduction to web development / JavaScript class, and the bulk of this devlog is going to be me applying what I learned to my summer goal, which is to display all my past (and future) generated crosswords on a website, and have an archive for past crosswords in a way that's efficient and not just me generating the HTML string for every crossword. 
          Here were the goals for the website:
          <br>
          <ol>
            <li>Uses a JavaScript framework (I chose Nuxt)</li>
            <li>Hosted online with my own domain (I ended up using AWS Amplify and Google Domains)</li>
            <li>Has a home page that hosts a 'crossword of the day'</li>
            <li>Has an about page with all my dev logs, and an 'about me'</li>
            <li>Has an archive page where you can see all my past manual and generated crosswords</li>
            <li>Users can interact with the crosswords, and it shows them the right answer when they're stuck and tells them when they're done</li>
            <li>Stores all the crosswords in an elegant way, instead of just having the HTML for every crossword manually written/generated</li>
            <li>Website looks nice and isn't buggy</li>
          </ol>
          <br>
          The ultimate result of this summer-long project is this website that you're using right now (I hope you like it!), but I'll be writing some of the tricks and tips I learned along the way.

          <h3>1. Using Nuxt (a JavaScript framework)</h3>

          <p>At first, when I was taking the JavaScript course, I didn't understand why you would need a 'framework'--to me, importing from JavaScript/CSS files or even having the JavaScript/CSS on the same page as my HTML seemed more organized and user-friendly. 
          However, as I was converting my larger crosswords to HTML, the files were getting admittedly large and disorganized even without HTML, and one key feature of frameworks stood out to me -- components. 
          I would realize later that things like 'reactivity' and the event loop would be even more important, but the idea of reusable components--essentially turning visual/UI elements into functions--appealed to me because it meant I could write some component and visualize every crossword/crossword-template using that component, instead of doing each one manually. 
          <br><br>
          One of the first things I built to practice components was a NavBar, and from then, I was hooked. Being able to modify the CSS for one 'component' and see that change propagate across every page containing that component was huge. Here's how my NavBar looked, and the corresponding couple lines of code that style it:
          <br>
          <img src="~/assets/example_crossword26.png" style="width:500px; border: 1px solid black;"/>
          <img src="~/assets/example_crossword27.png" style="width:500px;"/>
          <br>

          The other key component that I wanted to build was the Crossword component, but this ended up being much more complicated than the NavBar. 

          To get the crossword I wanted to display into the Crossword component to begin with, I learned about 'props', which are essentially inputs to the Crossword component if you think about it as a function.

          I then wanted to figure out how to display it. The resulting HTML and CSS for the new Crossword component remained relatively unchanged from my original HTML/CSS crossword, but the code looked quite different; I used 'v-for' loops, which are essentially visual for-loops, to iterate through the given crossword and generate the number of input boxes (and rows) needed to display any given crossword. 
          For example, instead of my code having 16 lines of input boxes for a 4x4 crossword (like I do in an earlier dev log), I just use this code: 

          <br>
          <img src="~/assets/example_crossword28.png" style="width:500px;"/>
          <br>

          The code iterates through the rows and columns of a crossword template and displays it for us, regardless of what the crossword looks like! This alone was a huge accomplishment, but I still had a long way to go. I used similar 'v-for loops' to display the 'across' and 'down' hints. 
      
          </p>
          <h3>2. Hosting Websites</h3>
        <p>
          This was actually one of the last things I did, but my first time trying to host websites using GitHub Pages was pretty complicated and so I was ready for another similarly painful process. However, I was pleasantly surprised when the first hosting service I tried - AWS Amplify, since it was free - basically worked instantly. The longest process was setting up the AWS account and connecting my GitHub, and then afterwards it was smooth sailing to get the Nuxt site up and running under the AWS domain.
          <br><br>
          Where things got more complicated, however, was 'routing' my own domain - megansmrosswords.com - to the AWS site so that I could access my website by going to meganmrosswords.com instead of a cryptic 'main2193081.amplify.com' link. I followed a bunch of tutorials without success, and ultimately found <a href='https://betterprogramming.pub/routing-an-aws-amplify-app-to-a-google-domain-7ca06fe88f0' target='_blank'>this one</a> that worked for me. I still don't really understand anything about how the technology behind the Internet or domains/routing works, but I'm just grateful I was able to figure out a working solution. It is interesting that you can just 'buy' or generate a domain from Google (or other services), though - it seems like something that should be free, but that's neither here nor there.
        </p>

          <h3>4. About Page</h3>
        <p>
          Throughout the course of this entire project, I've been writing short devlogs as 'progress pics' to see how far I've come (and to remember what I've already done). I also think that writing things down / explaining things helps me to better understand how things work, which was especially helpful when I just started learning to code but is still incredibly helpful now. 
          One of the more tedious parts of building the Megan's Mrosswords website was uploading these devlogs to the website (the about page looked too empty without it), because I had to format everything, load in all the images and required assets (and sometimes even generate some to show what I meant), and also go through everything I'd written and edit it to make it coherent, but it was also enjoyable and nostalgic to see how far I'd come and reminisce about the little issues and bugs that took me hours to debug but seem so simple now. 
      </p>

          <h3>5, 7. Archives and Data Structures and Design</h3>
        <p>
          Another big thing I did for the project was refactor the way my crossword generator was outputting the crosswords. Previously, it was a mess - I was storing bits and pieces (such as the hints, the templates, the words, and where the numbers were going) in various variables across the program, and then calling on them to ultimately generate an HTML file, as a string, that looked like a longer version of the example HTML file in a previous dev log. At the time, it was a much better alternative than generating the crossword in a more computer-friendly format but having to manually convert it to a string, and I didn't think to first generate it into a computer-friendly format and generate the HTML string from that. However, with some refactoring, the crossword objects now look like this:
          <br>
          <mark>
            {
date: 1658614278,
done_crossword: [['S', 'T', 'O', 'M', 'A', 'T', 'E', ' ', 'U', 'W', 'E'], ['H', ' ', ' ', ' ', 'J', 'A', 'M', ' ', 'M', 'E', ' '], ['E', ' ', ' ', ' ', 'A', 'G', 'E', ' ', 'B', 'L', ' '], ['A', ' ', ' ', ' ', 'Y', ' ', 'S', 'O', 'O', 'T', 'Y'], ['L', 'O', 'B', ' ', 'E', ' ', 'I', ' ', ' ', ' ', 'A'], [' ', ' ', 'O', ' ', 'R', 'E', 'S', 'E', 'E', 'E', 'W'], [' ', ' ', 'E', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['K', ' ', 'S', 'O', 'L', 'I', 'D', ' ', ' ', ' ', ' '], ['E', 'W', ' ', ' ', 'O', ' ', 'E', ' ', ' ', ' ', ' '], ['L', 'E', ' ', ' ', 'G', ' ', 'E', ' ', ' ', ' ', ' '], ['T', 'B', 'E', 'E', 'E', 'E', 'P', ' ', ' ', ' ', ' ']],
grid_numbers: [[1, 0, 0, 0, 5, 7, 8, 0, 10, 11, 0], [0, 0, 0, 0, 13, 0, 0, 0, 14, 0, 0], [0, 0, 0, 0, 15, 0, 0, 0, 16, 0, 0], [0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 12], [18, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 20, 0, 6, 0, 9, 0, 0, 0, 0], [21, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0], [22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
down_definitions: {1: ('STOMATE', 'A stoma'), 10: ('UWE', 'NO DEFINITION'), 13: ('JAM', 'A kind of frock for children'), 14: ('ME', 'One'), 15: ('AGE', 'To grow aged; to become old; to show marks of age; as, he grewfat as he aged'), 16: ('BL', 'NO DEFINITION'), 17: ('SOOTY', 'To black or foul with soot'), 18: ('LOB', 'To let fall heavily or lazily'), 19: ('RESEEEW', 'NO DEFINITION'), 20: ('SOLID', 'Having all the geometrical dimensions; cubic; as, a solid footcontains 1,728 solid inches'), 21: ('EW', 'A yew'), 22: ('LE', 'Famous architect from La chaux-de-fonds'), 23: ('TBEEEEP', 'NO DEFINITION')},
across_definitions: {1: ('SHEAL', 'Same as Sheeling'), 2: ('KELT', 'See Kilt, n'), 3: ('WEB', 'A weaver'), 4: ('BOES', 'Behoves or behooves'), 5: ('AJAYER', 'Philosopher from United kingdom'), 6: ('LOGE', 'A lodge; a habitation'), 7: ('TAG', 'A sale of usually used items (such as furniture, clothing,household items or bric-a-brac), conducted by one or a small group ofindividuals, at a location which is not a normal retailestablishment'), 8: ('EMESIS', 'A vomiting'), 9: ('DEEP', 'To a great depth; with depth; far down; profoundly; deeply'), 10: ('UMBO', 'One of the lateral prominence just above the hinge of a bivalveshell'), 11: ('WELT', 'A narrow border, as of an ordinary, but not extending aroundthe ends'), 12: ('YAW', 'To rise in blisters, breaking in white froth, as cane juice inthe clarifiers in sugar works')},
},
          </mark>

          The date refers to the day the crossword is meant for (which is only really relevant for the home page), the 'done_crossword' is the finished crossword where every letter is where it should be (used to compare and see if the users' crossword is finished), the grid_numbers mappings of word numbers to the corresponding coordinates, and the 'down_definitions' and 'across_definitions' fields are for mappings of the grid number to down and across definitions, respectively. 
          <br><br>
          This was a huge improvement visually and organizationally from how the crosswords used to be stored, and also meant I could build my archive by sorting all of these crossword objects by the date timestamp field. It took a lot of trial and error to ultimately design my 'data structure' like this; what helped was to keep in mind what it would be used for (passed into the Crossword component as props, and then used to render a visual and interactive representation of the crossword).
        <br>

        </p>

          <h3>6. Interactivity</h3>

        <p>
          The other big thing I was able to get out of using a JavaScript framework was 'reactivity', which is that code can automatically execute upon user (or API) input. To do this, I set up a client-side data of the users' current crossword, which gets initialized upon website load as an empty crossword (all the input boxes are empty). As the user gives inputs, the user_crossword updates accordingly. I also set a 'computed' variable that watches the user_crossword, and every time it's updated, if the user_crossword looks exactly like the generated crossword, the user has completed the crossword. This is the code I used to check for crossword completion reactively: 
          <br>
          <pre>
            user_crossword(newCrossword, oldCrossword) {
      var temp = []
      for ( var i = 0; i &lt; newCrossword.length; i++){
        var uppercase = newCrossword[i].map(element => {
        return element.toUpperCase();
});
        temp.push(uppercase)
      }

      var crossword_done = true

      for (var a = 0; a &lt; temp.length; a++){
        for (var b = 0; b &lt; temp[0].length; b++){
          console.log("temp[a][b] is", temp[a][b])
          if (temp[a][b] != this.$props.done_crossword[a][b]){
            console.log("setting crossword_done to false")
            crossword_done = false
          }
        }
      }
      if (crossword_done){
        alert("Congratulations! You finished today's Mrossword!")
      }
      
    }
          </pre>
          <br>
          As you can see, it's similar to the original JavaScript code from months ago, but is a lot more efficient and uses a lot more JavaScript and coding tricks. Additionally, since this is in the 'crossword' component, it's now possible to keep track of the completion status of multiple crosswords on the same page (e.g. the archive page!)
          <br>
          <br>
          All in all, the implementation of reactivity and various components enabled a lot of new features on the site (mostly being able to see and work on multiple crosswords on one page), and also allowed for a much cleaner code repository (as opposed to the original thousands of hard-coded HTML lines). I'm really happy about the changes that have been made, and really proud of the website as a whole!

        </p>

          <h3>8. Making things look nice</h3>
          <p>The big visual change I implemented (besides designing every such that the visual elements and overall view was cohesive) was writing a function to make sure that the crossword would always be a similar objective size, regardless of how big or small the crossword was.</p>
          <img src="~/assets/example_crossword29.png" style="width:500px;"/>
          <img src="~/assets/example_crossword30.png" style="width:500px;"/>
          <br>
          <p>To do this, I essentially set a fixed size for the crossword div (container), and then dynamically calculated the size of the input boxes in a way that would guarantee the crossword fit on the screen, and was also (relatively) consistent in size with the other crosswords regardless of it's own actual size. This way, all the crosswords on my archive page can look cohesive. If you want to see the code for this, it's in the GitHub under the Crossword.vue component.</p>

        </p>
      </div>
          

      <div class="spacer"></div>

  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'IndexPage',
  data() {
    return {
    }
  },
  computed: {
    todays_date: function () {
      const timeElapsed = Date.now();
const today = new Date(timeElapsed);
return today.toDateString()


    },
  }
}
</script>

<style>
@font-face {
  font-family: "Space Mono";
  font-weight: normal;
  src: local("Space Mono"),
    url(~/assets/SpaceMono-Regular.ttf) format("truetype");
}
@font-face {
  font-family: "Space Mono";
  font-weight: bold;
  src: local("Space Mono"), url(~/assets/SpaceMono-Bold.ttf) format("truetype");
}

@font-face {
  font-family: "Monument Grotesk";
  font-weight: bold;
  src: local("Monument Grotesk"),
    url(~/assets/MonumentGrotesk-Bold.ttf) format("truetype");
}

@font-face {
  font-family: "Monument Grotesk";
  font-weight: normal;
  src: local("Monument Grotesk"),
    url(~/assets/MonumentGrotesk-Regular.ttf) format("truetype");
}

body {
  margin: auto;
  width: 75%;
  background-color: #f9dae2;
}
</style>

<style scoped>

h3 {
  font-family: "Monument Grotesk";
}
#devlog_ai pre {
  background-color: white;
}
.spacer {
  height: 20vh;
}

a {
  color: black;
  background-color: white;
}

a:hover {
  background-color: white;
}

h1 {
  font-family: "Monument Grotesk";
  font-weight: bold;
}

.info {
  width: 40vw;
}
p {
  font-family: "Space Mono";
  font-size: 15px;
}

h2 {
  font-family: "Monument Grotesk";
  font-weight: bold;
  text-align: right;
  padding-right: 3vw;
  background-color: white;
}

.devlog_title {
  text-align: left;
}

#date {
}
</style>
