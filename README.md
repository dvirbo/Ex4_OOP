
# Object-Oriented Programming & Design- Task 4: “Pokemons” in Python

![ezgif com-gif-maker](https://user-images.githubusercontent.com/73783656/148681714-d93afb4e-d9eb-4447-b2f8-424b6cb45b59.gif)

## Authors

- [@dvir borochov](https://github.com/dvirbo)
- [@yuval shabat](https://github.com/yuvili)

## Backround

This project presents the final (last) assignment for the OOP course.
In this assignment, we asked to “put into practice” the main tools covered along the course, in particular,expected to design a “Pokemon game” in which given a weighted graph,  a set of “Agents” that should be located on it so they could “catch” as many “Pokemons” as possible.
The pokemons are located on the graph’s (directed) edges, therefore, the agent needs to take (aka walk)  the proper edge to “grab” the pokemon (see below for more info). 
our goal is to maximize the overall sum of weights of the “grabbed” pokemons (while not exceeding the maximum amount of server calls allowed in a second - 10 max)
The game is being played on a “server” that is given to you, and the task was to design and implement the client-side.\
After the game ends (each game has a fixed time - commonly 30-120 seconds) the results are printed - by the server.\
the results are printed as a json string below the “Game over”.
In this assignment, we are mainly interested in maximizing the overall score - which is denoted as “grade” - the sum of all the pokemon weight as caught by all the “Agents”. 
# client:
The client has the following api (all json based):
* Init the server with a case [0-15] from a command line.
* Get the underlining weighted (directed) graph - assume it is strongly connected (getGraph).
* Get the list of Pokemons (getPokemons), e.g., {"Pokemons":[{"Pokemon":{"value":5.0,"type":-1,"pos":"35.197656770719604,32.10191878639921,0.0"}}]} where value is the weight (grade), type is positive if the edge_dest > edge_src (else negative), and pos is the 2D position of it (here you need to find the edge - by the position & type). 
* Get a list of all the Agents (in case an agent is on a node its “dest” is -1).
* Locate each Agent on a node (addAgent) - before the game starts.
* Start a game - each game has a fixed time - mostly 30-120 seconds.
* Get the remaining time (in mili seconds) for the game to be played
* Direct each agent to the next destination (chooseNextEdge) - this can be done only when the agent is on a node (not on an edge) - this is the main api for the algorithm.
* Move the agents: this is the main method that “plays the game” - in order for an Agent to grab a pokemon, the agent needs to be on the same (directed edge) & the server should be called (move) when the Agent is “close-enough” to the pokemon - Note: the exact distance is not given.
* Get the game info (getInfo): returns the grade, and the number of moves of the current game. This data is printed at the end of each game.
*demonstration*:
![server](https://user-images.githubusercontent.com/73783656/148685551-acbb4e04-6b9f-478e-8447-ac4499767fcd.JPG)

## Run Locally

Clone or Download this project\

before you Start the server make sure that you have any java machine (JDK 11 or above)
paste on terminal:

    java -jar Ex4_Server_v0.0.jar 0  
 the last number at the end of the line indicate the case number(0-15)
 the code
 after paste the above line and press enter, you should get the output:
    Init Ex4 server on case: 0
    server started
    
after that, perss shift + F10 (Run)






## links:
*  Github: https://github.com/benmoshe/OOP_2021/tree/main/Assignments/Ex4
*  Main document: https://docs.google.com/document/d/1LrXIX2pLvRIVHdSqVIimCCxL7UBMaogAcLKfr2dOjHk/edit?usp=sharing
* create gif: https://ezgif.com/video-to-gif
