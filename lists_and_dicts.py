def run():
    my_list = [1, "Hello", True, 4.5]
    My_dict = {"firstname":"Juan", "lastname":"Leguizamon"}

    super_list = [
        {"firstname":"Juan", "lastname":"Leguizamon"},
        {"firstname":"Adriana", "lastname":"Esguerra"},
        {"firstname":"Uriel", "lastname":"Montaño"},
        {"firstname":"Natalia", "lastname":"Cuadrado"},
    ]

    super_dict = {
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-1,2,0,-2,1],
        "floating_nums" : [3.14, 4.5,6.7,1.47]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for values in super_list:
        for key,value in values.items():
            print(key, "-", value)

if __name__ == "__main__":
    run()