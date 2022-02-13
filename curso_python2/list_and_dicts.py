def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Ricardo", "lastname": "Sanchez"}

    Super_list = [
        {"firstname": "Ricardo", "lastname": "Sanchez"},
        {"firstname": "Ignacio", "lastname": "Mejia"},
        {"firstname": "Luis", "lastname": "Vasquez"},
        {"firstname": "Allison", "lastname": "Canseco"},
        {"firstname": "Ernesto", "lastname": "Cisneros"},
    ]

    super_dict = {

        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }
    
    for key, value in super_dict.items():
        print(key, "-", value)



if __name__ == "__main__":
    run()