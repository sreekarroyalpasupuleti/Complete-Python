# String concatenation
a1 = "Good" #a1 is a string
c2 = "Morning" #c2 is a string
v3 = a1 + c2 #concatenation
print(v3)

q="Have" # q is a string
w="A" # w is a string
e="Good" # e is a string
r="Day" # r is a string
t=q + " " + w + " " + e + " " + r
print(t)
# Iterating through a String
string = "NEWYORK CITY" # string q is a string
# Iteration
for i in string:
    print(i)

for i in enumerate(string):
    print(i)

a=list(enumerate(string))
print(a)

# String membership
string2 = "I MISS YOU"
print ('I' in string2) # Check whether substring "I" is present in string2
print ('MISS' in string2) # Check whether substring "LOVE" is present in string2
print ('YOU' in string2) # Check whether substring "YOU" is present in string2

# String Partitioning
string3 = "I am so sorry i forget your Birthday"
d = string3.partition("forget")
print(d)

# Upper Case a string
a=" Newyork State "
print(a)
b=a.upper() #Return whole string in uppercase
print(b)
# Lower Case a string
c=a.lower() #Return whole string in lowercase
print(c)

# String Functions
a="    CALIFORNIA STATE    "
print(a)
b=a.replace(" " , "") # Remove all whitespaces using replace function
print(b)
# remove *'s
a="*****NEWYORK*****STATE*****"
print(a)
b=a.strip('*')
print(b)

# rstrip,lstrip
t="******KALKI*****MOVIE****"
print(t)
b=t.rstrip('*') # Removes all '*' characters at the end of the string
print(b)
b=t.lstrip('*') # Removes all '*' characters at the beginning of the string
print(b)
c=t.strip('*') #Removes all '*' characters from begining & end of the string
print(c)