def zoo(arr):
  print("In your zoo there are:")
  for x in arr:
      print(x)

  # Ask the user to input new animals
  num_new_animals = int(input("How many new animals do you want to add? "))

  new_animals = []
  for _ in range(num_new_animals):
      animal = input("Enter the name of the new animal: ")
      new_animals.append(animal)

  # Add new animals to the zoo
  arr.extend(new_animals)

  print("\nUpdated zoo:")
  for x in arr:
      print(x)

# Initial array
array = ["dog", "cat", "bear"]

# Call the zoo function with the initial array
zoo(array)
