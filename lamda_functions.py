def run():
    word = ((input("Write your palindrome: ")).lower()).replace(" ","")

    palindrome = lambda word: word == word[::-1]

    if palindrome(word) == True:
        print("Congratulations " + word + " is a palindrome!")
    else:
        print("Sorry " + word + " is not a palindrome!")
    

if __name__ == "__main__":
    run()