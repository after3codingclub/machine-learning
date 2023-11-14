import turtle
t = turtle.Turtle()
t.speed(0) 
t.shape('turtle')
#sets the array
arr=[]
# function declaration

# sets the size of the array
# draws the circles
def draw_circle(x,y):
  t.penup()
  t.setpos(x,y)
  arr.append(t.pos())
  t.pendown()
  t.circle(10)
  t.penup()
  t.setpos(0,0)
  
# draws the line
def draw_line(arr):
  t.pendown()
  for x in arr:
    t.setpos(x)

#function execution
draw_circle(62,405)
draw_circle(-100,-215)
draw_circle(200,-35)

print(arr)
draw_line(arr)
input("press enter")
