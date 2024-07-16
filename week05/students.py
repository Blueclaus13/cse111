import csv


def main():
    
    ID_INDEX = 0

    NAME_INDEX = 1
    
    i_number = input("What is the student i-number? ")
    
    clean_number = i_number.pop("-")
    
    read = read_dictionary("team_assignments/students.csv", ID_INDEX)
    
    
    
    if clean_number in read:
        
        value = read[clean_number]
        
        print(value[NAME_INDEX])
        
    else:
        print("No such student.")
    
    

    
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
    Return: a compound dictionary that contains
      the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, "rt") as csv_file:
        
        reader = csv.reader(csv_file)
        
        next(reader)
        
        for student_list in reader:
            
            if len(student_list) != 0:
                
                key = student_list[key_column_index]
                
                dictionary[key] = student_list
                
    return dictionary
      
      
if __name__ == "__main__":
    main()
      
      
      
    