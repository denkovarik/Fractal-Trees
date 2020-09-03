# Fractal-Trees

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
| t | 8 |
| delta | 22.5 |
| axiom | G |

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
* Run p

## References
* DE CASTRO, L., 2020. FUNDAMENTALS OF NATURAL COMPUTING. [S.l.]: CRC PRESS, pp.327-355.

## Credits
* Dennis Kovarik

