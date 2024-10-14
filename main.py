class Person:
  """Represents a person with a name, age, and gender."""

  def __init__(self, name, age, gender):
    """Initializes a new Person object.

    Args:
      name: The person's name.
      age: The person's age.
      gender: The person's gender.
    """

    self.name = name
    self.age = age
    self.gender = gender

  def introduce(self):
    """Prints a message introducing the person."""

    print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Create an instance of the Person class
person1 = Person("Alice", 30, "female")

# Call the introduce method
person1.introduce()