def divisors(num):

    divisors = [i for i in range(1,num +1 ) if num % i == 0]
    return divisors
    

def run():
    try:
        num = input("Please enter a number: ")
        assert num.isnumeric(), "Please enter a valid value"
        assert int(num) >0, "Please enter a positive number or different to zero"
        print(divisors(int(num)))
        print("Give me a challenge son!")
    
    except ValueError:
        print("Please enter a valid value.")
    
if __name__ == "__main__":
    run()