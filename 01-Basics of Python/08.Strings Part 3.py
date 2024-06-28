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
#Example<3>
print('How {2} {1} {0} {3}'.format('day','your','is','?'))
print('Sreekar Salary: {a}, Rahul has {b} cars, Bank Intrest rate is: {c}'.format(a=1000,b='Two',c=12.3))


#Type3: Using f-strings (Formatted String Literals):
#Introduced in Python 3.6, f-strings provide a concise and readable way to embed expressions inside string literals.
# They are the most modern and preferred method of string formatting.
name = "sreekar"
age = 56
formatted_string = f"Hello, {name}. You are {age} years old."
print(formatted_string)

#When using f-strings in Python, you can pass !r to get the string representation of an object.
# which calls the repr() function on the object.
value = 12.14159

# Without !r
print(f"The value is {value}.")
# Output: The value is 12.14159.

# With !r
print(f"The value is {value!r}.")
# Output: The value is 12.14159.



# Final Summary:
# Readability: f-strings (f"..." syntax) are generally considered the most readable and concise method.
# Performance: f-strings are also faster compared to .format() and % formatting.
# Legacy Compatibility: % formatting is still used in older codebases, while .format() is versatile and widely used in modern Python.

# Padding and Precision of Floating Point Numbers
# Here, 35 would be the minimum number of characters the string should contain;
# .7f stands for how many numbers to show past the decimal point.
print('Floating point numbers: %35.7f' %(10.5))
# output:Floating point numbers:                          10.5000000
print('Floating point numbers: %15.7f' %(10.5))
# Floating point numbers:      10.5000000
print('Floating point numbers: %5.7f' %(10.5))
# Floating point numbers: 10.5000000

# Alignment, padding and precision with .format()
print('{0:0} | {0:0}'.format('Salary', 'Interest'))
print('{0:3} | {0:2}'.format('Salary', 'Interest'))
print('{0:10} | {0:2}'.format('Salary', 'Interest'))
print('{0:10} | {0:10}'.format('Salary', 'Interest'))
print('{0:13} | {1:13}'.format('Salary', 'Interest'))
print('{0:10} | {1:10}'.format('Salary', 'Interest'))
print('{0:6} | {1:10}'.format('Salary', 'Interest'))

print('{0:<6} | {1:^6} | {2:>6}'.format('Kalki','Adipurush','Sahoo'))
print('{0:<6} | {1:^9} | {2:>5}'.format(40,15,70 ))





