import turtle as T

keep_turtle = True


def stopTurtle():
    ans = input("Wanna stop yet? ")
    if ans == 'y' or ans == 'Y':
        keep_turtle = True

while keep_turtle == True:

    for i in range(1, 100):
        T.forward(2*i)
        T.left(90)

    stopTurtle()
