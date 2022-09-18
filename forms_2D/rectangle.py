square = lambda a, b: a * b
perimetr = lambda a, b: 2 * (a + b)
sideTroughSquare = lambda s, a: round(s / a, 2)
sideTroughPerimetr = lambda p, a: round(p / 2) - a

def OperSelection():
    print("\nвыбери операцию"
          "\n1 - вычислить площадь"
          "\n2 - вычислить периметр"
          "\n3 - вычислить сторону через площадь"
          "\n4 - вычислить сторону через периметр")

    choice = input("что считаем: ")

    if choice == "1":
        s = square(float(input("сторона а: ")),
                   float(input("сторона b: ")))
        return "площадь равна: ", s
    elif choice == "2":
        p = perimetr(float(input("сторона а: ")),
                     float(input("сторона b: ")))
        return "периметр равен: ", p
    elif choice == "3":
        a = sideTroughSquare(float(input("площадь: ")),
                             float(input("вторая сторона: ")))
        return "сторона равна: ", a
    elif choice == "4":
        r = sideTroughPerimetr(float(input("периметр: ")),
                               float(input("вторая сторона: ")))
        return "сторона равна", r
    else:
        return "фигура указана неверно", None