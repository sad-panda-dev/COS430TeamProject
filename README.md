# COS 430 (Software Engineering): Term Project

<p align="justify">
  <br> <strong>Group ID:</strong> G 03</br>
  <br> <strong>Group Members:</strong> Richard, Aleksandra, Abdallah</br>
  <br> <strong>Project Title:</strong> A game of Snake where there is an added element of teleporters.</br>
  <br> <strong>Project Description:</strong> Our team was given the task of designing, developing and implementing a software product that was suggested by a customer (in this case one of our fellow classmates). Following the Agile Software Development Method we will approach the problem through 3 separate iterations over the course of the semester. For each iteration we will address 1 user story and provide a deliverable product upon completion of each iteration. For version control and documentation we will be using this GitHub repository.</br>
 </p>

## Executive Summary

<p align="justify">
Below, you will find a brief executive summary of our term project, including how the project will be relevant to end-users.
</p>
<p align="justify">
  Our team has set out to create the classic arcade game Snake, with the added functionality of having a teleporter. The game will be a desktop application that is cross-platform to allow fun for as many end users as possible. We will also be creating a high score board stored that will be kept up to date via the internet. This will create a fun competitive environment for all end users to see how their skills match up against each other.
</p>

## Problem Statement

<p align="justify">
Given this task we set out to design a cross-platform desktop application that would create an easy enjoyable experience for the end user. The game of snake is one of the oldest arcade style games around and has been emulated and modified every which way. It was even depicted in the 1982 classic movie Tron, but instead of a snake the game was given the modification of being on a light cycle. But our classmate gave us the challenge of creating a variation of this classic game that we had yet to see, adding teleportation. With this new twist we hoped to create a small revitalization of the classic.
</p>


## Milestones and Timelines

#### Iteration #1
<p> Design, develop, test and deploy a functioning prototype of the traditional game of snake. Based on its cross-platform functionality we have decided to use python's pygame library to devlop the game.</p>

| Items        | Description              | Action Items and Deliverables                                                             |
|--------------|--------------------------|-------------------------------------------------------------------------------------------|
|  User Story  | Create a functioning Prototype| 
|    Created prototype      | Basic game functionality, movement with directional buttons, snake eats food and grows in size, score increments by 1. Snake hits its body and game is over                                                                            | Satisfied
|    Pause Screen       | User can press space bar to enter a pause state in the game                                                                             | Satisfied
|    Game Over Screen       | When the game ends the user enters a game over screen, where they will be given the option to play again                                                                             |  Satisfied
|    Start Screen       | When game starts the start screen is inititated giving a prompt for the user to start the game                                                                             | Satisfied


#### Iteration #2
<p>Design and implement the functionality telporters within the snake game as well as keeping a table of high scores. Durring this iteration we will first focus on storing that data on the local machine, with the key for the table being a 3 character string for the users initials, just like in traditional arcade games. If that proves to be too easy we will then move on to storing the data within an online database. (Possible second user story) Depending on the time it takes to create the functionality of the high score, we may then move on to creating a basic website which will be finalized within the final iteration.</p>

| Items        | Description              | Action Items and Deliverables                                                             |
|--------------|--------------------------|-------------------------------------------------------------------------------------------|
|  User Story  | Add teleportation to the game as well as add more stylistic changes to give the overall game experience a more congruent retro feel                                                                             | satisfied
|    Sprites Added       | Added sprites for the snake head, snake body and the food                                                                               |
|    Sounds Added       | We added background music durring game play, a sound to signify the snake ate food, a sound when entering the pause screen and a sound signifying game over                                                                              | satisfied
|    Username functionality       | We made it so a user can enter a username and the database stored on the local host will keep track of a usernames highscore                                                                            | satisfied
|    Teleporter added       | Teleporter now randomly generates on screen and when the snake hits it, the snake will randomly teleport to another part of the screen on part at a time                                                                           | satisfied
|    Style/Theme       | Gave the overall game a more retro feel with image on start screen as well as the font and color scheme for other screens of the game                                                                             | satisfied



#### Iteration #3
<p>We will either be creating the website or finishing it depending on the progress made within the second iteration. The functionality of the website is to host a place where members of the class can download the game to play it. The initial idea is to use the django framework to develop the website. The second functionality of the website would be then to store a high score database, which upon generation of a score within any instance of the game, rather than storing the high score on the users local machine the high score could then be stored within the high score database on the website.</p>

| Items        | Description              | Action Items and Deliverables                                                             |
|--------------|--------------------------|-------------------------------------------------------------------------------------------|
|  User Story  | Overall theme was finalized and made sure to be continuous throughout different screens, added website to store high score database                                                                              | satisfied
|    Website | Basic website where user can check their high score was created but is only on the local host                                                                             | satisfied
|    Minor Bugs Fixed       | Took care of any remaining minor bugs                                                                            | satisfied
|    Teleport Sprite Added       | We added the sprite for the teleporter so it matched the style for the rest of the game components                                                                            | satisfied
|    Final Tweaks to Theme       | Made sure that all colors and fonts matched between different screens due to slight reverts when merging subsequent branches                                                                              | satisfied

**Final Team Presentation:**
Upon completion of the three iterations we will then as a group present the final software product that we have developed.


## UML Diagrams 
#### [1] Use Case Diagrams
<p align="justify">
<img width="375" alt="Screen Shot 2022-03-07 at 9 26 13 PM" src="https://user-images.githubusercontent.com/80590323/157154058-76f9fc6a-fdac-4f55-b3f4-69dc37ee4303.png">
</p>

#### [2] Class Diagrams
<p align="justify">
<img width="843" alt="Screen Shot 2022-04-27 at 9 42 41 PM" src="https://user-images.githubusercontent.com/80590323/165659605-fd189e0e-a107-482a-999c-44751c30c5bb.png">
</p>

#### [3] Sequence Diagrams 
<p align="justify">
<img width="1217" alt="Screen Shot 2022-03-07 at 10 38 36 PM" src="https://user-images.githubusercontent.com/80590323/157161674-da4cb146-c78e-4b64-b29c-6a569c5e2e26.png">
</p>

#### [4] Deployment Diagrams 
<p align="justify">
<img width="779" alt="Screen Shot 2022-03-08 at 9 46 36 AM" src="https://user-images.githubusercontent.com/80590323/157261584-7abbee7d-f536-4662-97f4-6391ff673e2f.png">

</p>


## References and Further Information 

<br>[1: Pygame](https://www.pygame.org/news)</br>
<br>[2: Python](https://www.python.org/)</br>
<br>[3: Adobe Stock Images](https://stock.adobe.com/)</br>
<br>[3: MySQL](https://www.mysql.com/)</br>
<br>[3: Laravel](https://laravel.com/)</br>





