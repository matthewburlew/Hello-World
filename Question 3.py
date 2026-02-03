from ast import Name
from turtle import title


def format_greeting(name, title="Customer"):
    return f"Hello, {title} {name}!"


def main():
    full_name = input("What's your full name? ")
    greeting = format_greeting(full_name)
    print(greeting)


if __name__ == "__main__":
    main()
