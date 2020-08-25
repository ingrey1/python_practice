import timeit


print(timeit.timeit(setup = '''class Dog:
    def __init__(self):
        pass
    def bark(self):
       print("bark") 

dog1 = Dog()''', stmt = "dog1.bark()", number = 1000 )) # result in seconds