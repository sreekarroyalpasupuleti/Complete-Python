# There are three types to perform string formatting.

# Type1. Using % Operator (Old method with placeholders):
# The % operator is used to format strings by inserting values into placeholders.
# It's an older method that is still found in some legacy codebases.

# 1. Using % Operator (Old method with placeholders):
# The % operator is used to format strings by inserting values into placeholders.
a = ("shyam")
v = 30
formatted_string = "My name is %s. My age is %d." % (a, v)
print(formatted_string)


# Type2. Using .format() Method:
# The .format() method provides more flexibility and readability compared to % formatting.
# The basic syntax for using the .format() method
# formatted_string = "String with {} placeholders and {}".format(value1, value2)----SYNTAX
# Example usage of the .format() method
# In this syntax:
# {}: Curly braces {} serve as placeholders in the string where values will be inserted.
# formatted_string: This is the resulting string after values are inserted into placeholders using .format().

#Example <1>
name = "SREEKAR"
age = 10
# Using .format() to insert values into placeholders
code = "Hello, my name is {} and I am {} years old.".format(name, age)
# Printing the formatted string
print(code)

#Example <2>
name = "SREEKAR"
age = 56
profession = "Data Scientist"
code2 = "Hello, my name is {}. I am {} years old, and I work as an {}.".format(name, age, profession)
print(code2)

#Type3: Using f-strings (Formatted String Literals):
#Introduced in Python 3.6, f-strings provide a concise and readable way to embed expressions inside string literals.
# They are the most modern and preferred method of string formatting.
name = "sreekar"
age = 56
formatted_string = f"Hello, {name}. You are {age} years old."
print(formatted_string)

# Final Summary:
# Readability: f-strings (f"..." syntax) are generally considered the most readable and concise method.
# Performance: f-strings are also faster compared to .format() and % formatting.
# Legacy Compatibility: % formatting is still used in older codebases, while .format() is versatile and widely used in modern Python.

