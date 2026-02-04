from unicodedata import name


def format_name(name, title="Customer"):
    name = name.strip()

    if name == "":
        return "Hello, Valued Customer"
    
    name= name.strip()
    return f"Hello, {title} {name}"
first_name = name.split()[0]

#Main Program
full_name= input("What is your full name? " )
greeting= format_name(full_name)   
print(greeting)


