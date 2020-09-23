import turtle 
import sys
import subprocess
from PIL import Image

def setUpTurtle():
	turtle.up()
	turtle.setposition(0, -300)
	turtle.down()
	turtle.left(90)
	turtle.speed(10) 

def rewrite(word, P):
	newWord = ""
	for i in range(len(word)):
		rule = ""
		for t in range(len(P)):
			if (P[t][0] == word[i]):
				rule = P[t][1]
				break
		if (rule == ""):
			rule =  word[i]

		newWord = newWord + rule

	return newWord

def go_turtle_go_turtle_go_turtle_go(word, d, delta, turtleState):
	for i in range(len(word)):
		if (word[i] == "G" or word[i] == "F"):
			turtle.forward(d)
		elif (word[i] == "+"):
			turtle.right(delta)
		elif (word[i] == "-"):
			turtle.left(delta)
		elif (word[i] == "["):
			state = list(())		#(x,y,delta)
			state.append(turtle.position())
			state.append(turtle.heading())
			turtleState.append(state)
		elif (word[i] == "]"):
			back = len(turtleState)-1
			state = turtleState[back]
			turtleState.pop()
			turtle.penup()
			turtle.setpos(state[0][0], state[0][1])
			turtle.setheading(state[1])
			turtle.down()
			
	return	turtleState

t = 8
delta = 22.5
word = "G"
gRule = "F+[[G]-G]-F[-FG]+G"
fRule = "FF"
P = list(())
rule = list(())
rule.append("G")
rule.append(gRule)
P.append(rule)
rule = list(())
rule.append("F")
rule.append(fRule)
P.append(rule)
turtleState = list(())
filename = "defaultTree"
d = 1
animate = 'no_animation'

# Read in the command line arguments
if (len(sys.argv) > 6):
	del rule
	del P
	P = list(())
	filename = sys.argv[1] 		# Read in filename from first argument 	
	animate = sys.argv[2] 		# Read in animation
	t = int(sys.argv[3])		# Read in value for t from the second argument
	d = float(sys.argv[4])		# Read in the value for d from the second arg
	delta = float(sys.argv[5])	# Read in value for delta	
	word = sys.argv[6]		# Read in string for starting axiom
	numP = int(sys.argv[7])		# Read in the number of production rules
	index = 8
	for i in range(numP):
		rule = list(())
		rule.append(sys.argv[index])
		index = index + 1
		rule.append(sys.argv[index])
		index = index + 1
		P.append(rule)	


if (animate == 'no_animation'):
	turtle.tracer(False)
else:
	turtle.tracer(True)
turtle.tracer(True)
	
loadWindow = turtle.getscreen() 
setUpTurtle()

for i in range(t):
	word = rewrite(word, P)


turtleState = go_turtle_go_turtle_go_turtle_go(word, d, delta, turtleState)

filepath = "fractalTrees/" + filename

loadWindow.getcanvas().postscript(file=(filepath+".ps"))

im = Image.open(filepath+".ps")
#im.save(filepath+".png")

turtle.exitonclick() 
