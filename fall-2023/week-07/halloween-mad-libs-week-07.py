def halloween_madlibs():
  print("Welcome to the Halloween Madlibs Game!")

  # Get user inputs
  adjective = input("Give me an adjective: ")
  plural_noun = input("Enter a plural noun: ")
  verb = input("Give me a verb: ")
  place = input("Name a spooky place: ")
  creature = input("Name a Halloween creature: ")

  # Display the story
  print("\nHere's your spooky Halloween story:")
  print(f"On a {adjective} Halloween night, a group of {plural_noun} decided to {verb}.")
  print(f"They ventured into the haunted {place} where they encountered a terrifying {creature}!")

# Run the madlibs game
halloween_madlibs()
