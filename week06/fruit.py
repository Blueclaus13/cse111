def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")
  #Reverse
  fruit_list.reverse()
  fruit_list.append("orange")
  print(f"Modified: {fruit_list}")
  apple_index = fruit_list.index("apple")
  fruit_list.insert(apple_index, "cherry")
  print(f"Modified: {fruit_list}")
  fruit_list.remove("banana")
  print(f"Add code to remove: {fruit_list}")
  deleted_element = fruit_list.pop()
  print(f"deleted: {deleted_element}")
  print(f"Modified: {fruit_list}")
  fruit_list.sort()
  print(f"Sorted: {fruit_list}")
  fruit_list.clear()
  print(f"Cleared: {fruit_list}")

if __name__ == "__main__":
  main()

