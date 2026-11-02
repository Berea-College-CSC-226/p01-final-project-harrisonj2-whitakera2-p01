# CSC226 Final Project

**Author(s)**: `Jairus Harrison, Aaron Whitaker`'Jairus V. Harrison, Aaron Whitaker'

**Google Doc Link**: `https://docs.google.com/document/d/1M8_sSF6B-XI_b6pINM26Fy4johnEERpBXgVQSXv1kRc/edit?usp=sharing
`

---

## Milestone 1: Setup, Planning, Design

**Title**:`Echoes of the cave`   

**Purpose**: `This project is going to be a game that is made off of our first assignment that uses the arrow pad to move around 
`
**Source Assignment(s)**: `T01, T11, T12`

**CRC Card(s)**:
  - Create a CRC card for each class that your project will implement.
  - See this link for a sample CRC card and a template to use for your own cards (you will have to make a copy to edit):
    [CRC Card Example](https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing)
  - Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the 
    README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - 
    and REPLACE it with your own:
  - 
  
![Don't leave me in your README!](image/crc.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one. ")

**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments, then re-branching out from the merged code.  

```
    Branch 1 starting name: Jairus  
    Branch 2 starting name: whitakera2  
```

### References 

Throughout this project, you will likely use outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update this 
section as you go. DO NOT forget about it!

---

## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
    So far we are feeling behind with the weather with it behind a bit hard to meet up and discuss everything to do with 
    our code
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: `0 - 100%`

**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
   75%
   
   We are ver yconfident that we can get this done we just have to find the time to meet up and bash it all out. Meeting when
   we are free other then just meet up days will help us get this project where we want it to be.
```
 
---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions

In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button 
in PyCharm. 

    Once you hit "Run" in PyCharm, Gui will ask you a question once you answer the qoestion the GUI wll give you a litte story, then a player-controlled characater will spawn,
    appearing on the screen. As you move through rooms, you will encounter NPCs and doors that lead to other areas. Your goal 
    is to avoid obstacles (bad NPCs) while interacting with friendly NPCs to progress. The game is divided into multiple rooms, 
    When you complete the final room, you will receive a "You Passed the Game" message, 
    and the game will close automatically after 15 seconds. If you collide with an enemy NPC, the game will end, and a 
    "You Lose" message will appear, closing the game after 5 seconds. You can explore different areas by entering doors, 
    which take you to other rooms.

### Errors and Constraints

Every program has bugs or features that had to be scrapped for time. These bugs should be tracked in the issue queue. 
You should already have a few items in here from the prior weeks. Create a new issue for any undocumented errors and 
deficiencies that remain in your code. Bugs found that aren't acknowledged in the queue will be penalized.

    Start game file doesnt work because it doesnt close the game properly

    Hit boxes are not centered 
    
    No orginal code was put in the readme due to lack of how to do it and being confused 
    
    Lack of organization and CRC cards

    GUI does not close game properly and does not disappear once you start the game

    Lack of multiple standalone functions

    Game wouldnt run becuase game.run was not called in main

    Doors code The game's door functionality is responsible for transitioning between rooms

    Collision Detection on Objects may not collide as expected, even though they should. 
    This can happen due to incorrect bounding box sizes, improper collision handling, or missing checks.

    Incorrect Sprite Positioning Sprites (like characters and objects) don’t appear in the right place on the screen or move erratically. 
    This might be due to issues with rect positioning or coordinate mismatches.
     
    Unresponsive Controls Player controls don’t work properly, often due to incorrect event handling or missed key press events.

    Unclear or Unintuitive User Interface (UI) The game lacks clear instructions, feedback, or buttons, which can confuse players. 
    This might include unclear win/lose screens or lack of proper UI elements like score counters, health bars, or menus.

    Memory Leaks or Slow Performance As the game runs, performance degrades, or the game crashes unexpectedly due to improper resource management

    Unintended NPC Movement or AI Behavior NPCs or enemies don’t behave as expected—such as moving in the wrong direction, not following the player, or not reacting to events.
    Meaning Enemies  walk off-screen or don’t chase the player when they should.

    Sound Issues Sounds not playing correctly, either due to incorrect file formats or not managing the sound channels properly. This can lead to no audio or a mix of sounds playing out of sequence.
    So it was removed

    Level Design Issues Levels may be improperly designed, causing the player to get stuck or make the game unplayable.

    State Management Issues game does not properly manage different states like gameplay, or game over states, leading to transitions being broken.

    Asset Loading and Performance had issues with loading assets such as images, or fonts, p

    Player Input Bugs Player inputs were sometimes ignored, or multiple inputs are read simultaneously causing erratic player behavior.

    Inconsistent Art Style or Missing Assets The art style of the game doesn’t match throughout, or certain assets (e.g., backgrounds, characters) are missing or inconsistent. 
    Some NPCs look entirely different from the main character, or missing animations lead to poor visual feedback.

    Poor Documentation Lack of clear comments or documentation within the code makes it difficult for the developer or others to understand the structure of the game.

    Bad NPC does not despawn in room 2: The Bad NPC should disappear when the player enters room 2, but there is a bug where it continues to persist. This needs to be addressed.
    
    Good Npc did not spawn
    
    There isnt a fully correct border on the map that goes with the cave background meaning the player can walk anywhere
    
    The door hitboxes are still visable

    The game does not keep track of every NPC you caught so you can pass the game without caughting even one

    NPC speed isn't dynamically updating: The speed of the Bad NPC is set to a default but doesn’t adjust during gameplay as expected. This issue needs a review of how the speed parameter is passed and updated.

    Game does not properly handle player respawn: When the player respawns after losing, the NPCs and their interactions might not reset properly, which results in unintended behavior.

    Limited feedback for "You Win" state: While the game closes 15 seconds after the win message, additional feedback about the player’s progress could enhance the user experience.

    Lack of pause functionality: The game lacks a way to pause or resume gameplay. This feature could be useful for players who wish to take a break without losing progress.

### Peer Evaluation

It is important that all members of your team contribute equitably. The peer evaluation is your chance to either 
a) celebrate the great work you all did together as an effective team, or b) indicate to the instructor if a member of
your team did not contribute their fair share. Grades will be adjusted for any team member who is evaluated poorly. Your
commit history will be used as evidence, so make sure you are using git effectively!

    In our team, the contributions were generally well-balanced. I took on the tasks of managing the NPC behavior, movement, and collisions, 
    while my partner focused on handling room transitions and updating the game logic. Despite challenges, we both worked well 
    together and were flexible when issues arose. 

### Reflection

Each partner should write three to four well-written paragraphs address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- How well did you work with your partner? What made it go well? What made it challenging?

```
    Partner 1:
    
    We selected this project because we wanted to create a game with multiple levels, interactive NPCs, and 
    dynamic elements. It seemed like a good balance between creative storytelling and technical programming challenges. 
    Our final project, while relatively close to the initial design, evolved as we refined the NPC mechanics and room 
    transitions. We learned a lot about structuring game states, handling sprite groups in Pygame, and implementing smooth movement mechanics.
    
    The hardest part of the project was dealing with unexpected bugs related to NPC behavior, especially the movement and 
    despawn logic. These issues required careful debugging and testing. If I were to do this again, I would ensure that NPC 
    interactions and transitions are better modularized, so each room and NPC type is more easily managed.
    
    Working with my partner was an enjoyable experience, and we managed to divide tasks effectively. We worked 
    asynchronously on different aspects of the project, but it was helpful to review each other's work regularly. 
    One challenge was the timing of certain game mechanics, such as showing win/lose screens after specific delays. Overall,
    it was a positive and collaborative experience.
```

```
    Partner 2: 
    
Our final project stuck fairly close to our initial design in terms of layout and features. 
We successfully implemented multiple rooms with transitions, player movement, collectable NPCs, and an enemy that 
could trigger a game-over state. However, there were areas where the design had to change due to time constraints or 
technical complexity. For example, we had originally planned more advanced enemy AI, but simplified these ideas to meet deadlines and focus on stability.

This project taught me a lot about game architecture—especially the importance of managing state across multiple scenes 
(or rooms), and how to properly use sprite groups and event loops in Pygame. I also learned how difficult debugging can
be in game development, since so many things rely on visual feedback. One small typo in coordinates or object initialization 
can cause something to silently fail or break in unexpected ways.

The hardest part of the project was managing transitions between rooms while preserving or resetting various game objects 
correctly. For example, getting enemies to spawn or despawn at the right times took a lot of trial and error. Next time, 
I would plan more clearly how game state should be managed globally, and write reusable helper functions to handle room 
changes. I think our collaboration went well—we communicated openly and divided tasks fairly. It was sometimes challenging
when we misunderstood each other’s code, but working through those issues helped us improve as a team.
```

---