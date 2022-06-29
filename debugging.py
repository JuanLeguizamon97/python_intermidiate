def divisors(num):

    divisors = [i for i in range(1,num +1 ) if num % i == 0]
    return divisors
    

def run():
    try:
        num = int(input("Please enter a number: "))
        if num <=0:
           raise ValueError
        print(divisors(num))
        print("Give me a challenge son!")
    
    except ValueError:
        print("Please enter a valid value.")
    

if __name__ == "__main__":
    run()