import turtle
import grille

papier = turtle.Screen()
crayon = turtle.Turtle()
papier.setup(width=550,height=350)


papier.bgcolor("lightgray")
crayon.color("darkred")
crayon.pensize(5)


def ligneoe(x1,y1,x2,y2):
    crayon.penup()
    crayon.goto(x1,y1)
    crayon.pendown()
    crayon.goto(x2,y2)

def ligneoal(x1,y1,a,l):
    crayon.penup()
    crayon.goto(x1,y1)
    crayon.pendown()
    crayon.setheading(a)
    crayon.forward(l)


'''
crayon.penup()
crayon.goto(-250,0)
crayon.pendown()
for i in range(5):
    if i==2:
        crayon.color("navy")
    else:
        crayon.color("darkred")
    crayon.forward(50)
    crayon.left(90)
    crayon.forward(50)
    crayon.right(90)
    crayon.forward(50)
    crayon.right(90)
    crayon.forward(50)
    crayon.left(90)
'''


def carre_cercle(x,y,r):
    crayon.penup()
    crayon.goto(x,y)
    crayon.pendown()
    for _ in range(4):
        crayon.forward(r)
        crayon.left(90)
    crayon.forward(r/2)
    crayon.circle(r/2)

carre_cercle(0,0,100)
crayon.color("navy")
carre_cercle(-100,-100,100)


#a.trace()
papier.update()
grille.set_crayon(grille.Axe.tortue_axe,couleur="darkgray")
grille.set_crayon(grille.Graduation.tortue_graduation,couleur="darkgray")
grille.set_crayon(grille.Pattern.tortue_pattern,couleur="darkgray")
p = grille.Pattern(20,(' ','-'),(90,10))
g = grille.Grille(50,p,50,p)
g.trace()

a = grille.Axe()
a.trace()


grad = grille.Graduation(50,20,label=("Arial",14,"normal"))
grad.affiche()
grad2 =grille.Graduation(10,5,sub=5,show_label=False)
grad2.affiche()


papier.title("Motif")


crayon.hideturtle()

papier.update()
papier.exitonclick()