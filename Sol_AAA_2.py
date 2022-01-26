import turtle

radio = 20

for i in range(3):
    while radio >= 40:
        radio += 10
        turtle.pencolor('red')
        turtle.circle(radio)
        break
    radio += 20
    turtle.pencolor('green')
    turtle.circle(radio)
