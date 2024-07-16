def main():
    text_list = read_list("provinces.txt")

    # print(text_list)

    #Remove the first item in the list
    text_list.pop(0)
    #Remove last item in the list
    text_list.pop()
    #Replace all occurrences of "AB" in the list with "Alberta".
    print(replace_in_list("AB", "Alberta", text_list))
    #Count the number of elements that are "Alberta" and print that number.
    print(f"Alberta occurs {text_list.count('Alberta')} times in the modified list.")

def replace_in_list(old_word, new_word, list):
    for i,word in enumerate(list):
        if word == old_word:
            list[i] = new_word
    return list
    
def read_list(filename):
    text_list = []
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)

    return text_list

if __name__ == "__main__":
    main()