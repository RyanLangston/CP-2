name = "Ryan"
age = 37
PI = 3.14159

# print(f"my name is {name} and I am {age} years old")
# print(f"my name is {name: <10} and I am {age} years old")

# print(f"Pi rounded to 2 decimal places is: {PI:.2f}")

# print(f"Pi rounded to 4 decimal places is: {PI:.4f}")

# F String Notes
"""
f before the string allows expressions/variables inside of the {}

.2f 2 decimal places

< aligns text to the left
> aligns text to the right
^ centers the text

To center and adjust alignment to make things look good we need to provide the WIDTH of the text



"""

print(f"my name is {name:?<25} and I am {age} years old")
