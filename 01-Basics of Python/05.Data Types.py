#There are 14 data types in python.

#<1>int datatypes
a=1 #Decimal form
print(a)
b=0b11 #binary numbers (3 in base 10)
print(b)
c=0x12 #hexadecimal (16)
print(c)
print(type(c))# type of object


#<2>float datatypes
d=25.033
print(d)
e=14.1e1#e letter is allowed
print(e)
print(type(e))# type of object


#<3>complex datatypes
f = 30+40j #assigned int value in real part & imaginary part
print(type(f))# type of object


g = 20.5+2.3j #assigned float value in real part & imaginary part
h = 30.8+20j  #assigned float value in real part & real value in imaginary part
print(g+h)
print(g/h)
a1 = 20+30j
b1 = 20+30j
print(a1+b1)
print(a1-b1)
print(a1*b1)
print(a1/b1)

#<4> Bool Data type
i = 10
j = 20
k = i<j
l=i>j
print(k)
print(l)



#<5> Str Data Type
m = 'all'
n = "the"
q='''hai'''
print(type(m))
print(type(n))
print(type(q))
o = ''' all 
         the 
    best'''
p = '''all "the" best'''
print(o)
print(p)

r=int(1.23)
print(r)
mango = 'Welcome' # Define string using single quotes
print(mango)
print(type(mango))
orange = "To" # Define string using Double quotes
print(orange)
print(type(orange))
goal = "Hyd" # Define string using Triple quotes
print(goal)
print(type(goal))

##Type casting or TypeCoersion
# int(): - you can convert from other type to int type except complex
n=int(9.532)  # float to int
print(n)
c=int("0")  # string to int
print(c)

#float
p=float(25)
print(p)
#float(1+2j)  # cannot convert complex to float
s=float(True)    # boolean to float
print(s)
o=float('10')    # string to float
print(o)
#bool
z=bool(17.32)# float to bool
print(z)
q=bool(15) #int to bool
print(q)
g=bool(4+4j) #complex to bool
print(g)

print(type(g)) # type of object

