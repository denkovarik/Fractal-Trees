# Fractal-Trees

![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)

## Description
This program creates models of plant architecture using Turtle Graphics and bracketed L-systems. A bracketed L-system is used to represent the graph-theoretic trees. It includes an algorithm for creating a large string of characters (called a "word") starting from a much smaller string (called the "axiom") and a set of production rules. The final "word" is then interpreted as seiries of commands (by a "little turtle") for drawing the structure. In this way, a computer can create fractal images of plant-like structures starting from a simiple set of rules.

The bracketed L-system involves the use of strings whose characters represent instuctions on how to draw the a certain structure. These strings consist of an alphabet, a starting axiom, a delta, a length 'd', a set of production rules, and a time step 't'. The set of production rules are applied to the axiom to produce a new "word" according to the set of production rules. This "word" is then rewritten 't' more times according to the production rules. The alphabet defines the characters used in the strings and the production rules. This produces a final string, which represents a set of instructions for how to draw the a structure. Each instruction is represeted as a single character in this final string or "word". 

The following alphabet was used for this project:
* V = {F,G,\[,\],+,-}

The commands represented by the above symbols are as follows:
| Character | Instruction |
| --------------- | --------------- | 
| F, G | Move forward a step of length 'd' while drawing a line. |
| \+ | Turn right by andle delta |
| \- | Turn left by angle delta |
| \[ | Save the current state of the turtle for later use onto a stack of saved states. No line is drawn. |
| \] | Remove the last saved state from the stack and use it to restore to turtle's last saved state. No line is draw. |

The default values used in the project are given below:

The default set of production rules fo the bracketed L-system are as follows:
| Variable | Value |
| --------------- | --------------- |
| time step | 8 |
| delta | 22.5 |
| axiom | G |
| distance | 1 |

| Default Production Rules |
| --------------- |
| G -> F\+\[\[G\]\-G\]\-F\[\-FG\]\+G |
| F -> FF |
| \[ -> \[ |
| \] -> \] |

This project was created as a result of taking the course CSC 449 "Fundamentals of Natrual Computing" at the South Dakota School of Mines and Technology. The concepts used in this project were taken from the book _Fundamentals of Natural Computing_ written by Leandro Nunes de Castro. For more information, please refer to this book.


## Installation
This project was developed and tested in Ubuntu on the terminal.

### Required Software
* Python 3
* Turtle Graphics
* Python Imaging Library
   

### Optional Software for Windows Users running Windows Subsystem for Linux (Ubuntu)
* Xming
   * X-server package for displaying platform on windows
   * Note that if you get a error like "no display name and no $DISPLAY environment variable" when trying to run the program, then make sure Xming is running and then try typing the following command into the shell: 
      * "export DISPLAY=:0.0".
   
   
### Clone the repository
* Clone with SSH
  * git clone git@github.com:denkovarik/Fractal-Trees.git
* Clone with HTTPS
  * git clone git@github.com:denkovarik/Fractal-Trees.git
  
## Usage
* Run program with default values
   * python3 fractalTree.py
   
### Run with Command Line Arguments
Running the program with command line arguments will allow you to create different plant-like structures. The syntax for the command line arguments if very specific, and if your arguments do not meet this, then either the default values will be used, or the program may not work. For the program to work properly, the following arguments must be passed into the program in the following order.
| Order | Argument Name | Description | Example |
| --------------- | --------------- | --------------- | --------------- |
| 1 | Filename | The name of the file to save the newly created image as | newTree |
| 2 | Animation | Specifies whether or not to animate the drawing of the structure. To turn animation off, put "no_animation" in place for this argument | no_animation |
| 3 | Time Step | Specifies the time step variable 't' for the bracketed L-system. This variable specifies how many times the "word" is rewritten. | 8 |
| 4 | Distance | The distance of each step in drawing the structure | 1 |
| 5 | axiom | The starting word for the bracketed L-system algorithm to rewrite | G |
| 6 | Delta | The angle for the turtle to turn when drawing the structure | 22.5 |
| 7 | Axiom | The starting word for the bracketed L-system to start with | G |
| 8 | Number of Production Rules | The number of production rules used in drawing the struction. There can be a variable number of rules, and the rules can be given in any order. Note that each production rule is expected to consist of 2 space seperated words | 2 |
| 9-10 | Production Rule 1 | The first production rule to use. This consists of a Character to be rewritten followed by a space followed by a string specifying what the character in the new word will be rewritten to. | G F\+\[\[G\]\-G\] |
| 11-12 | Production Rule 2 | The second production rule to use. This consists of a Character to be rewritten followed by a space followed by a string specifying what the character in the new word will be rewritten to. | G GG |
| . | . | . | . |
| . | . | . | . |
| . | . | . | . |

#### Example
* python3 fractalTree.py test no_animation 8 1 22.5 G 2 G F+[[G]-G]-F[-FG]+G F FF


## References
* DE CASTRO, L., 2020. FUNDAMENTALS OF NATURAL COMPUTING. [S.l.]: CRC PRESS, pp.327-355.

## Credits
* Dennis Kovarik

