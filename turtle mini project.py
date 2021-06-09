import turtle
window = turtle.Screen()
window.bgcolor("BLACK")
obj = turtle.Turtle()
obj.shape("turtle")
colors = [ "RED","ORANGE","YELLOW","GREEN","BLUE","PINK","PURPLE","WHITE","BROWN","VIOLET"]
y = 50
for x in range (500):
    obj.color(colors[x%10])
    obj.forward(y)
    y += 1/2
    obj.right(89)
