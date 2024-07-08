import random 

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    
    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)

    words = []
    print(words)

    append_random_words(words, 3)
    print(words)

def append_random_numbers(numbers_list, quantity = 1):
    for x in range(quantity):
        random_number= random.uniform(1,99)
        rounded = round(random_number,1)
        numbers_list.append(rounded)

def append_random_words(words_list, quantity = 1):    
    words_new = ["hello", "ok", "byebye", "bum"]
    for word in range(quantity):
        words = random.choice(words_new)
        words_list.append(words)


if __name__ == "__main__":
    main()