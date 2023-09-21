
def rectangle_area(width, height):

    if width <=0:
        print("Длина фигуры не может быть равна 0")
    if height <=0:
        print("Высота фигуры не может быть равна 0")
    else:
       print(height * width)
print("Введите высоту")
width = float(input())
print("Введите длину")
height = float(input())
rectangle_area(width, height)