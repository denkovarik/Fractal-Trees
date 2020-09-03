# Fractal-Trees

## Description
This program creates models of plant architecture and fractal geometery using Turtle Graphics and bracketed L-systems. A bracketed L-system is used to represent the graph-theoretic trees. It includes an algorithm for creating a large string of characters (called the "word") starting from a much smaller string (called the "axiom") and a set of production rules. The final "word" is then interpreted as seiries of commands (by a "little turtle") for drawing the structure. In this way, a computer can create fractal images of plant-like structures starting from a simiple set of rules.

The bracketed L-system involves the use of strings whose characters represent instuctions of how to draw the structure. These strings consist of a starting an alphabet, a starting axiom, a delta, a length 'd', a set of production rules, and a time step 't'. The set of production rules are applied to the axiom to produce a new "word" according to the set of production rules. The "word" is rewritten 't' - 1 more times according to the production rules. The alphabet defines the characters that are used in the strings and the production rules. This produces a string which represents a set of instructions for how to draw the structure. Each instruction is represeted by a single character in the final "word". 

In this project the alphabet used is as follows:
* V = {F,G,\[,\],+,-}

The commands represented by the above symbols are as follows:
| Character | Instruction |
| --------------- | --------------- | 
| F, G | Move forward a step of length 'd' while drawing a line. |
| \+ | Turn right by andle delta |
| \- | Turn left by angle delta |
| \[ | Save the current state of the turtle for later use onto a stack of saved states. No line is drawn. |
| \] | Remove the last saved state from the stack and use it to restore to turtle's last saved state. No line is draw. |

For example, an L-system with an alphabet of V = {F,G,[,],+,-}, a 


## Installation


### Required Software
* Python 3
   

### Optional Software for Windows Users running Windows Subsystem for Linux (Ubuntu)
* Xming
   * X-server package for displaying platform on windows
   * Note that if you get a error like "(Ant Clustering Simulation:34): 
   Gtk-WARNING **: 21:14:58.430: cannot open display: " when trying to run the program, 
   then make sure Xming is running and then try typing the following command into the 
   shell: "export DISPLAY=:0.0".
   
   
### Clone the repository
* Clone with SSH
  * git clone 
* Clone with HTTPS
  * git clone 
  
## Usage
* This command will start a set of example runs for demonstration

## Credits
* Dennis Kovarik

