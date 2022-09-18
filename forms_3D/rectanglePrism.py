from forms_2D import rectangle

vol = lambda s, h: round(s * h, 2)     # объём через площадь основания
sideFoundThrVol = lambda a, v, h: rectangle.sideTroughSquare(round(v / h, 2), a)    # сторона основания через объём
height = lambda s, v: round(v / s, 2)       # высота призмы

def OperSelection():
    print("\nвыбери операцию"
          "\n1 - объём через площадь основания"
          "\n2 - сторону основания через объём"
          "\n3 - высоту призмы")
    choice = input("что считаем: ")

    if choice == "1":
        v = vol(float(input("площадь основания: ")),
                float(input("высота призмы: ")))
        return "объём равен: ", v
    elif choice == "2":
        a = sideFoundThrVol(float(input("вторая сторона основания: ")),
                            float(input("объём призмы: ")),
                            float(input("высота призмы: ")))
        return "сторона основания равна: ", a
    elif choice == "3":
        h = height(float(input("объём: ")),
                   float(input("площадь основания: ")))
        return "высота равна", h
    else:
        return "фигура указана неверно", None