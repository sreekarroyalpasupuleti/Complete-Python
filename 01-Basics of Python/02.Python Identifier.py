# Identifiers in Python are names given to variables, functions, classes, etc.
# They must follow certain rules:
# 1.Can contain alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
# 2.Cannot start with a digit.
# 3.Case-sensitive (A and a are different identifiers).
# <1>Python Identifier
# Example: Valid identifier examples
A=5
print(A)
user=3
print(user)

# <2>Symbols are not identified in python
# Example: Using special symbols in identifiers (invalid)
# u$er = 5  # Identifier can't use special symbols except _ UNDERSCORE


# <3># Identifier can't start with a digit
# Example : Identifiers cannot start with a digit (invalid)
# 21total = 30  # Digit cannot start an identifier
total21=30
print(total21)


# <4>Case sensitivity in identifiers
hai=7
HAI=6
print(hai)
print(HAI)

# <5>Using keywords as identifiers (invalid).Keywords cannot be assigned as identifier
# true=1
# else=5
# false=6
# if=8Identifiers in Python