from forms_2D import circle
from forms_2D import rectangle
from forms_2D import triangle

def figureSelection():
    print("\nвыбери номер фигуры:"
          "\n1 - круг"
          "\n2 - прямоугольник"
          "\n3 - треугольник")

    choice = input("что выбираем: ")
    val = None
    txt = None
    if choice == "1":
        txt, val = circle.OperSelection()
        return txt, val
    if choice == "2":
        txt, val = rectangle.OperSelection()
        return txt, val
    else:
        return "номер указан неверно", None