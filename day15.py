import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colour_list =[(249, 249, 249), (239, 239, 239), (242, 242, 242), (247, 247, 247), (193, 193, 193), (130, 130, 130), (157, 157, 157), (52, 52, 52), (231, 231, 231), (115, 115, 115), (141, 141, 141), (209, 209, 209), (67, 67, 67), (93, 93, 93), (85, 85, 85), (145, 145, 145), (190, 190, 190), (58, 58, 58), (196, 196, 196), (74, 74, 74), (223, 223, 223), (140, 140, 140), (177, 177, 177), (165, 165, 165), (108, 108, 108), (89, 89, 89), (174, 174, 174), (32, 32, 32), (35, 35, 35), (28, 28, 28)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range (1, number_of_dots):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)








screen = turtle_module.Screen()
screen.exitonclick()