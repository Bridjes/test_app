import forms_2D
import forms_3D


def Main():
    print("Выбери измерение фигуры: "
          "\n1 - 2D"
          "\n2 - 3D")

    choice = input("что выбираем: ")
    text = None
    value = None
    if choice == "1":
        text, value = forms_2D.figureSelection()
    elif choice == "2":
        text, value = forms_3D.figureSelection()
    else:
        print("неправильный выбор")

    print("=" * 10)
    print(text, value)

Main()