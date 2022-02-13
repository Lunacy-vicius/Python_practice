def run():
    squares = [i**2 for i in range(1, 101) if  i % 3 !=0]
            #[Element for element in iterable if condition]
#Element: representa cada uno de los lementos a poner en la nueva lista
#for element in iterable: ciclo a partir del cual se extraeran elementos de otra lista o cuaquier iterable
#if condicion: Condicion opcional para filtrar los elementos del ciclo
if __name__ == "__main__":
    run()


# def run():
#     squares = []
#     for i in range(1, 101):
#         if i % 3 != 0:
#             squares.append(i**2)

#     print(squares)

# if __name__ == "__main__":n
#     run()