def run():

    #my_dict ={}

    #for i in range (1, 101):
    #    if i%3 != 0:
    #       my_dict[i] = i**3

    #print(my_dict)  


    natural_numbers = {i: i**3 for i in range(1,101) if i%3!=0}
    print(natural_numbers)

if __name__ == "__main__":
    run()