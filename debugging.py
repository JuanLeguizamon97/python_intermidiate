def divisors(num):
    divisors = []

    for i in range(1, num +1 ):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = int(input("Please enter a number: "))
    print(divisors(num))
    print("Give me a challenge son!")

if __name__ == "__main__":
    run()