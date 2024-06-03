
def greet(name):
    print(f"Hello {name}")


def year_of_birth(name,age):
    print(f"Hello {name}, you were born in {2024-age}")


def year_of_birth(name,age):
   print(f"Hello {name}, you were born in {2024-age}")

#Default arguments
def my_country(country="Uganda"):
    print(f"Hello Akirachix from {country}")


# def greeting(*names):
    # for name in names:
    # print(f"hello {names}")

def sum(*numbers):
    total=0
    for number in numbers:
        total+= number
    return total 
# positional arguments
def multiply_many(*numbers):
    total=1
    for number1 in numbers:
        total*=number1
        return total
    
# keyword arguments
def create_sentence(**words):
    print(words)
    sentence=" "
    for word in words.values():
        sentence += word
        sentence += " "
        return sentence
    
# Both positional and keyword arguments
def sum_and_greet(*args,**kwargs):
    total=0
    for x in args:
        total +=x
    f=kwargs["first_name"]
    l=args["last_name"]
    greeting=f"Hello  {f} {l} the sum of your numbers is {total}"
    return greeting


def remove_white_space(*text):
    newtext = text.split(" ").join("")
    return newtext


