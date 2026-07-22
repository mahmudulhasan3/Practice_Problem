def hello():
    return "Hello"

some = hello
print(some())

def outer():
    def inner():
        return "I am Mahmud"
    return inner

result = outer()
print(result())