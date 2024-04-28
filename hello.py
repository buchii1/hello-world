def sayHello(name):
    greet = "Hello World!"
    return f"{greet}\n{name.capitalize()}! Welcome to CSE 310."


def main():
    name = input("what is your name? ")
    print(sayHello(name))

main()