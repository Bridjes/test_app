import math

square = lambda r: round(math.pi * r * r, 2)
perimetr = lambda r: round(2 * math.pi * r, 2)
radiusThroughSquare = lambda s: math.sqrt(s / math.pi)
radiusThroughPerimeter = lambda p: round(p / (2 * math.pi), 2)

def OperSelection():
    print("\nвыбери операцию"
          "\n1 - вычислить площадь через радиус"
          "\n2 - вычислить периметр через радиус"
          "\n3 - вычислить радиус черещ площадь"
          "\n4 - вычислить радиус через периметр")
    choice = input("что считаем: ")

    if choice == "1":
        s = square(float(input("радиус: ")))
        return "площадь равна: ", s
    elif choice == "2":
        p = perimetr(float(input("радиус: ")))
        return "периметр равен: ", p
    elif choice == "3":
        r = radiusThroughSquare(float(input("площадь: ")))
        return "радиус равен: ", r
    elif choice == "4":
        r = radiusThroughPerimeter(float(input("периметр: ")))
        return "радиус равен", r
    else:
        return "фигура указана неверно", None