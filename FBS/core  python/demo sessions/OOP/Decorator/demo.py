# -------------------------------------------------------------
# 1. Treating functions as objects (Aliasing)
# -------------------------------------------------------------
# def demo():
#     print("I am from demo")

# a = 12
# b = demo
# print("type of demo =", type(demo))
# print("type of b =", type(b))
# demo()
# b()


# -------------------------------------------------------------
# 2. Passing a function as an argument to another function
# -------------------------------------------------------------
# def fun1():
#     print("I am from function 1")

# fun1()

# def demofun(a):
#     print("I am from demofun")
#     a()

# demofun(fun1)


# -------------------------------------------------------------
# 3. Returning an inner function from an outer function
# -------------------------------------------------------------
# def outer():
#     print("Outer is called")
#     def innerFunction():
#         print("Inner function is called..")
#     return innerFunction

# a = outer()
# a()


# -------------------------------------------------------------
# 4. Closures
# -------------------------------------------------------------
# def outer():
#     print("Outer is Called")
#     var = "Virat"
#     def innerFunction():
#         print("Inner function is called..", var)
#     return innerFunction

# a = outer()
# a()


# -------------------------------------------------------------
# 5. Decorators
# -------------------------------------------------------------
# def decorator(fun):

def demo(fun):
    print("Decorator is called...")
    def wrapper():
        print("Before Calling your function all task will be Performed here..")
        fun()
        print("After Calling your function all task will be Performed here..")
    return wrapper

@demo
def login():
    print("\n login is Done\n")

@demo
def logout():
    print("\nLogout is Done\n")

# Manual decoration equivalent to @demo:
# a = demo(login)
# a()
# b = demo(logout)
# b()

login()
logout()