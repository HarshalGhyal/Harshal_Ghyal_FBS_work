#### Arithmetic operators:

x=10
y=20
a='abc' 
b='xyz'

#1. '+'
#addition

res =x+y

#concatenation 
res= a+b

# res=x+a ---diff data types operation is not possible

#2.'-'
res=y-x

#3. '*'
res=x*y

#4.'/' --- division gives  exact quotient float value of division untill remainder becomes zero
res=5/2

#5.'//'--- floor division gives integer value of division roumded down to nearest whole number

res=5//2

#6. '%'---- modulas divion it gives remainder

res=5%2

#7. '**'
res=4**2

#### Assignment operators:
#1."="

x=5

#2."+="

x+=3   # x=x+3

#3. "-="
x-=2   #x=x-2

#4.  "*="
x*=3  # x=x*3

#5."/="
x/=2   # x=x/2

#6. "//="

x//=2  #x=x//2

#7."%="

x%=2   #x=x%2

#8. **=
x**=2   #x=x**2

#### relational/comparison operators
x=10
y=20
a='abc'
#1. == #exactequals to

print(x==y)  #returns false
print(x=='10') # returns false

#2.!= # not equal to
print(x!=y) # returns true

#3.> # greater than
print(x>y) # returns false

#4.>= #greater than equal to
print(x>=10)  #true

#5. < # smaller than
print(y<x) #false

#6.<= smaller than and equal to
print(x<=10) # true

#### logical operators
x=True
y=False

#1. and
print(x and y) # false

#2. or
print(x or y) # true

#3. not
print(not x) # false

#### Identity operators
x=10
y=10
z=20
#1. is
print(x is y) # true
print(x is z) # false

#2. is not
print(x is not y) # false
print(x is not z) # true

#### Membership operators
#1. in
print('f' in 'Firstbit') # false
print('F' in 'Firstbit') # true

#2. not in
print('f' not in 'Firstbit') # true
print('F' not in 'Firstbit') # false


#### Bitwise operators

#1. & (bitwise AND)
x=10  # 1010
y=5   # 0101
print(x & y)  # 0000 => 0

print(12&10) # 1100 & 1010 => 1000 => 8

#2. | (bitwise OR)
x=12 # 1100
y=10  # 1010
print(x | y)  # 1110 => 14

#3. ^ (bitwise XOR)
x=12 # 01100
y=20 # 10100
print(x ^ y)  # 11100 => 24

#4. << (bitwise left shift)
x=10 # 1010
print(x<<2) # 101000 => 40

#5. >> (bitwise right shift)
x=12 # 1100
print(x>>3) # 0001 => 1
print(12>>2) # 0011 => 3

