from functools import reduce #import of the reduce function


def run():

    #Filter function
    my_list = [1,4,5,6,13,19,21]  #List with initial values

    odd = list(filter(lambda x: x%2 !=0, my_list)) #Odd variable store a list that contains the filter function, it´s necessary the use of lambda functions to evaluate the condition an return an iterator and we need to convert this typo into a list involving the filter function with a list function

    print(odd)

    #Map function
    map_list =[1,2,3,4,5] #Initial values

    squares = list(map(lambda x: x**2, map_list)) #Using map function to transform the values in map_list in this case is the squares for each value in the list. Map function recieves the intrucntions from a lambda function and the list to convert
    
    print(squares)

    #Reduce function
    reduce_list = [2,2,2,2,2] #initial values

    all_multiplied = reduce(lambda a,b: a*b, reduce_list) #Implementing reduce function and using a lambda function who recieves two parameters an iterate the initial list values

    print(all_multiplied)

if __name__ == "__main__":
    run()