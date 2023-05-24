def goForward():
    print("It went forward")

def inner(car):
    car["model"] = "Honda"
    print("Inner: " + car["model"])

def outter():
    obj = {
        "model": "BMW",
        "year": 1998,
        "goForward": goForward
    }
    print("Outter: " + car["model"])

    inner(car)

    print("Outter Again: " + car["model"])

    outter()

    #primary data types get passingby values

    #Local.
    #Pytorch. is an important library
    #Matplot is also a library
    #Pathlib. gives every type of computer access to your program
    #Methonds are functions built into arrays by python