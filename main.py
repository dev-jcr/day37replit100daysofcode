#String slicing

# Color change subroutine
def c(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")

# Title
print(f"{c('red')}Generate your Star Wars name")

# Input and slice
name = input(f"{c('white')}What's your first name?\n").capitalize()
name = name[0:3]
surname = input(f"{c('white')}What's your second name?\n").lower()
surname = surname[0:3]
fsw = f'{name}{surname}'
maiden = input("What's your maiden name? Invent a name if you are not married\n").capitalize()
maiden = maiden[0:2]
city = input("In which city you were born?\n").lower()
city = city[-3:]
ssw = f"{maiden}{city}"

# Output
print(f"{c('blue')}Your Star Wars name is {fsw} {ssw}")


# Course solution

# print("STAR WARS NAME GENERATOR")

# all = input("Enter your first name, last name, Mum's maiden name and the city you were born in").split()

# first = all[0].strip()
# last = all[1].strip()
# maiden = all[2].strip()
# city = all[3].strip()

# name = f"{first[:3].title()}{last[:3]} {maiden[:2].title()}{city[-3:].lower()}"

# print(f"Your Star Wars name is {name}")