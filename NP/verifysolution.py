def get_num_guesses(length):
    total = 0
    for i in range(1,length+1):
        total += 26 **i

    return total



while True:
    text = input("Enter password length (or 'q' to quit): ")
    
    if text.lower() == "q":
        break

    length = int(text)

    print(get_num_guesses(length))
    