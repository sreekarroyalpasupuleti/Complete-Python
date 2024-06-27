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
