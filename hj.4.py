class Animal(object):
    def run(self):
        print('Animal is running...')

spart=Animal()
print(spart.run())
print('.........1')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

    def run_twice(animal):
        animal.run()
        animal.run()

dog = Dog()
print('.........2')
dog.run()
print('.........3')
cat=Cat()
print('.........4')
cat.run()
print('.........5')
cat.run_twice()
print('.........6')

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
print('.........7')

run_twice(Cat())
print('.........8')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())





