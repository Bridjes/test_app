square = lambda a, h: round((a * h) / 2)
perimetr = lambda a, b, c: a + b + c

def OperSelection():
    print("\nвыбери операцию"
          "\n1 - вычислить площадь"
          "\n2 - вычислить периметр")

    choice = input("что считаем: ")

    if choice == "1":
        s = square(float(input("основание: ")),
                   float(input("высота: ")))
        return "площадь равна: ", s
    elif choice == "2":
        p = perimetr(float(input("сторона а: ")),
                     float(input("сторона b: ")),
                     float(input("сторона с: ")))
        return "периметр равен: ", p
    else:
        return "фигура указана неверно", None
