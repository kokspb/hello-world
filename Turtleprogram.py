import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

# faz o quadrado
def square(length, angle,):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.left(angle)
	
#no fim de cada quadrado, vira para a esq 11º, e repete o mesmo por 100x
for i in range(100):
    square(100, 90)
    my_turtle.left(11)

#exercicio: melhorar este codigo, colocando cores etc. https://trinket.io/ 
    


