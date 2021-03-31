import ex_module

def hello(asd):
    print(asd, type(asd))

def main():
    print("main test")
    hello(8.5)
    dog = Dog() #Animal()
    dog.move()
    print(dog.leg_count)

    ex_module.write_module_name()
    print(__name__)


class Animal:
    name = "Foo"

    def move(self):
        self.leg_count = 4
        print(self.name)

class Dog(Animal):
    def move(self):
        print("Your stuff.")
        return super().move()
        

if __name__ == '__main__':
    main()