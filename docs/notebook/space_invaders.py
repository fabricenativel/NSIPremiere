from turtle import *
PIXEL = 10
animation("off")

def afficher_dessin() :
    penup()
    L = 310
    H = 180
    goto(-L,-H)
    pendown()
    width(1)
    color("black")

    goto(L,-H)
    begin_fill()
    goto(L-10,-H)
    goto(L-10,-H+5)
    goto(L,-H)
    goto(L-10,-H-5)
    goto(L-10,-H)
    end_fill()
    goto(-L,-H)
    goto(-L,H-10)
    begin_fill()
    goto(-L-5,H-10)
    goto(-L,H)
    goto(-L+5,H-10)
    end_fill()
    done()

def taille_pixel(n=10):
    global PIXEL
    PIXEL = n

def dessine_pixel(x,y, nom_couleur):
    width(1)
    hideturtle()
    if type(nom_couleur) is str:
        couleur(nom_couleur)
    else:
        couleur_dec(nom_couleur[0], nom_couleur[1], nom_couleur[2])
    penup()
    goto(-310+x*PIXEL,-170+y*PIXEL)
    begin_fill()
    pendown()
    for i in range(4) :
        forward(PIXEL)
        right(90)
    penup()
    end_fill()

def couleur(nom_couleur) :

    couleurs = {"rouge":(1,0,0.2),
            "vert":(0.2,0.7,0.35),
            "violet":(0.85,0.25,0.65),
            "turquoise":(0,0.8,0.8),
            "vertjaune":(0.6,0.8,0.3),
            "jaune":(1,0.8,0),
            "orange":(1,0.3,0),
            "bleu":(0.25,0.37,0.8),
            "rose":(0.9,0.05,0.5)}
    assert nom_couleur in couleurs, "Couleur non reconnue"
    code_couleur = couleurs[nom_couleur]

    couleur = [int(code*255) for code in code_couleur]
    couleur_dec(couleur[0],couleur[1],couleur[2])

def couleur_dec(r,g,b) :
    hexa = ['{:02X}'.format(a) for a in (r,g,b)]
    color( '#'+''.join(hexa) )

