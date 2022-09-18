from forms_3D import circlePrism
from forms_3D import rectanglePrism
from forms_3D import rectanglePrism

def figureSelection():
    print("\nвыбери номер фигуры:"
          "\n1 - круглая призма"
          "\n2 - прямоугольная призма")

    choice = input("что выбираем: ")
    val = None
    txt = None
    if choice == "1":
        txt, val = circlePrism.OperSelection()
        return txt, val
    elif choice == "2":
        txt, val = rectanglePrism.OperSelection()
        return txt, val
    else:
        return "номер указан неверно", None