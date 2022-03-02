# COS430TeamProject
### Team Project for COS430 Software Engineering
#### **Project Team Memebers:**
Richard Beaudet, Aleksandra Milinovic, and Abdallah Mohamed
#### Project Description:
Our team was given the task of designing, developing and implementating a software product that was suggested by a customer (in this case one of 
our fellow classmates). Following the Agile Software Development Method we will approach the problem through 3 seperate iterations over
the course of the semester. For each iteration we will address 1 user story and provide a deliverable product upon completion of each
iteration. For version control and documentation we will be using this github repository, and for continuous integration we will be using 
circleci. This continuous integration will ensure that each individual part of the software is made properly, pass quality assurance tests as 
well as be assembled properly. The continuous delivery that the assembled product is efficient.
#### Software Specified By the Customer:
A game of snake where there is an added element of transporters
#### Current layout for the 3 iterations
**Iteration 1:**
Design, develop, test and deploy a functioning prototype of the traditional game of snake with the added element of including the concept of teleporters.
Based on its functionality we have decided to use python's pygame library to devlop the game.<br>
**Iteration 2:**
Implement the functionality of keeping a table of high scores. Durring this iteration we will first focus on storing that data
on the local machine, with the key for the table being a 3 character string for the users initials, just like in traditional arcade games.
If that proves to be too easy we will then move on to storing the data within an online database.
(Possible second user story) Depending on the time it takes to create the functionality of the high score, we may then move on to creating
a basic website which will be finalized within the final iteration.<br>
**Iteration 3**
We will either be creating the website or finishing it depending on the progress made within the second iteration. The functionality of the website
is to host a place where members of the class can download the game to play it. The initial idea is to use the django framework to develop the website. 
The second functionality of the website would be then to store a high score database, which upon generation of a score within any instance of the game, 
rather than storing the high score on the users local machine the high score could then be stored within the high score database on the website.
