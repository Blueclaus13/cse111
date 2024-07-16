import csv
from datetime import date
PRODUCT_LIST_INDEX = 0
DESCRIPTION_INDEX = 1
PRICE_INDEX = 2
QUANTITY_INDEX = 1
TAX_RATE = 0.06
PRODUCT_INDEX = 0
current_date_and_time = date.today()

def main():

  try:
    product_dict = read_dictionary("products.csv", PRODUCT_INDEX)
    print("Inkom Emporium")
    read_list("request.csv", product_dict)
    print("Thank you for shopping at the Inkom Emporium")
    print(f"{current_date_and_time.ctime()}")
  except FileNotFoundError as file_not_found:
    print(f"{file_not_found} not exist, verify name")
  except PermissionError as permission_error:
    print(permission_error)
  except KeyError as key_error:
    print(f"Error: product {key_error} is not in products list")


  
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

    for row_list in reader:
      if len(row_list) != 0:
        key = row_list[key_column_index]
        dictionary[key] = row_list

    return dictionary
  
def read_list(filename, product_dict):
  
  list = []
  with open(filename, "rt") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    total_quantity = 0
    subtotal = 0
    for row_list in reader:
      product = row_list[PRODUCT_LIST_INDEX]
      quantity = row_list[QUANTITY_INDEX]
      product_value = product_dict[product]
      description = product_value[DESCRIPTION_INDEX]
      price = product_value[PRICE_INDEX]
      total_quantity += int(quantity)
      subtotal += (float(price) * int(quantity))
      print(f"{description}: {quantity} @ {price}")
    taxes = subtotal * TAX_RATE
    total = taxes + subtotal
    print(f"Number of Items: {total_quantity}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {taxes:.2}")
    print(f"Total: {total:.2}")
    
if __name__ == "__main__":
    main()
