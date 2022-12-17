import random


def Start():
    print("1. Задание 1")
    print("2. Задание 2")
    __a = input(":")
    if __a == "1":
        dz1()
    else:
        if __a == "2":
            dz2()
        else:
            print("Not found")
            Start()


def dz1():
    class BMW():
        benzin = "100L"
        motor = "v10"
        type = "lexkovaa"

        def __init__(self):
            print("BMW")
            print(self.benzin)
            print(self.motor)
            print(self.type)
            print(" ")


    class LADA(BMW):
        motor = "v3"

        def __init__(self):
            print("LADA")
            print(self.benzin)
            print(self.motor)
            print(self.type)
            print(" ")


    class MERSEDES(LADA):
        motor = "v13"
        type = "gryzovaa"


        def __init__(self):
            print("MERSEDES")
            print(self.benzin)
            print(self.motor)
            print(self.type)
            print(" ")


    BMW()
    LADA()
    MERSEDES()
    input("Press Enter to return to the menu")
    Start()


def dz2():
    class number():
        _number = random.random()
        print(_number)
        _number = _number - random.random()
        print(_number)
        input("Press Enter to return to the menu")
        Start()


Start()