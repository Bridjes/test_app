from forms_2D import circle

vol = lambda s, h: round(s * h)     # объём через площадь основания
volThrRadFound = lambda r, h: round(circle.square(r) * h, 2)   # объём через радиус основания и высоту
sqrFoundThrVol = lambda v, h: round(v / h, 2)      # площадь основания
radFound = lambda v, h: circle.radiusThroughSquare(sqrFoundThrVol(v, h))   # радиус основания
perFound = lambda v, h: circle.perimetr(radFound(v, h))     # периметр основания
height = lambda v, s: round(v / s, 2)   # высота призмы

def OperSelection():
    print("\nвыбери операцию"
          "\n1 - объём через площадь основания"
          "\n2 - объём через радиус основания"
          "\n3 - вычислить площадь основания"
          "\n4 - вычислить радиус основания"
          "\n5 - вычислить периметр основания"
          "\n6 - высоту призмы")
    choice = input("что считаем: ")

    if choice == "1":
        v = vol(float(input("площадь основания: ")),
                float(input("высота призмы: ")))
        return "объём равен: ", v
    elif choice == "2":
        v = volThrRadFound(float(input("радиус основания: ")),
                           float(input("высота: ")))
        return "объём равен: ", v
    elif choice == "3":
        s = sqrFoundThrVol(float(input("объём: ")),
                           float(input("выоста: ")))
        return "площадь равна: ", s
    elif choice == "4":
        r = radFound(float(input("объём: ")),
                     float(input("выоста: ")))
        return "радиус равен", r
    elif choice == "5":
        p = perFound(float(input("объём: ")),
                     float(input("выоста: ")))
        return "периметр равен", p
    elif choice == "6":
        h = height(float(input("объём: ")),
                   float(input("площадь основания: ")))
        return "высота равна", h
    else:
        return "фигура указана неверно", None