#RevolveDraw
import turtle as t
t.setup(600,600)
t.bgcolor("black")
t.pensize(2)
d = {1:"red",2:"yellow",3:"blue",4:"green",5:"orange",6:"purple"}
for i in range(50):
    for c in range(1,7):
        t.color(d[c])
        t.fd(i*5+c+1)
        t.right(59)
t.done()
