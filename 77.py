import turtle

def main():
    arch = turtle.Turtle()
    turtle.setup(600, 500)

    def draw_arch(direction, angle, length):
        if direction == 'right':
            arch.right(angle)
        else:
            arch.left(angle)
        arch.forward(length)

    # Задает цвет
    arch.fillcolor('#34a128')

    # Начало закраски
    arch.begin_fill()

    # Размер пера
    arch.pensize(2)

    # Цикл для рисования верхней части арки
    i = 0
    while i < 4:
        if i % 2 == 0:
            draw_arch('right', 50, 60)
        else:
            draw_arch('right', 40,10)
        i += 1
    arch.end_fill()


    # Конец закраски
    arch.end_fill()

    arch.fillcolor('#ed7409')
    arch.begin_fill()
    arch.circle(80, 360)
    arch.end_fill()
    arch.up()
    arch.left(90)
    arch.forward(30)
    arch.left(90)
    arch.forward(30)

    arch.fillcolor('#ffff00')
    arch.begin_fill()
    arch.down()
    arch.right(60)
    arch.forward(30)
    arch.right(120)
    arch.forward(30)
    arch.right(120)
    arch.forward(30)
    arch.end_fill()
    arch.up()

    arch.left(120)
    arch.forward(60)
    arch.left(180)

    arch.fillcolor('#ffff00')
    arch.down()
    arch.begin_fill()
    arch.right(60)
    arch.forward(30)
    arch.right(120)
    arch.forward(30)
    arch.right(120)
    arch.forward(30)
    arch.end_fill()
    arch.up()

    arch.right(60)
    arch.forward(30)
    arch.right(90)
    arch.forward(100)
    arch.left(90)



    arch.circle(150, 345)
    arch.begin_fill()
    arch.down()
    arch.circle(150,30)
    arch.end_fill()


    turtle.done()


if __name__ == '__main__':
    main()