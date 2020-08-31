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

def go_turtle_go_turtle_go_turtle_go(word, d, gamma, turtleState):
	for i in range(len(word)):
		if (word[i] == "G" or word[i] == "F"):
			turtle.forward(d)
		elif (word[i] == "+"):
			turtle.right(gamma)
		elif (word[i] == "-"):
			turtle.left(gamma)
		elif (word[i] == "["):
			state = list(())		#(x,y,gamma)
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
gamma = 22.5
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
filename = "den tree 3"
d = 1

if (len(sys.argv) > 5):
	del rule
	del P
	P = list(())
	filename = sys.argv[1]
	t = int(sys.argv[2])
	d = float(sys.argv[3])
	gamma = float(sys.argv[4])
	word = sys.argv[5]
	numP = int(sys.argv[6])
	index = 7
	for i in range(numP):
		rule = list(())
		rule.append(sys.argv[index])
		index = index + 1
		rule.append(sys.argv[index])
		index = index + 1
		P.append(rule)


turtle.tracer(True)
loadWindow = turtle.getscreen() 
setUpTurtle()

for i in range(t):
	word = rewrite(word, P)


turtleState = go_turtle_go_turtle_go_turtle_go(word, d, gamma, turtleState)

filepath = "fractalTrees/" + filename

loadWindow.getcanvas().postscript(file=(filepath+".ps"))

#im = Image.open(filepath+".ps")
#im.save(filepath+".png")

turtle.exitonclick() 
