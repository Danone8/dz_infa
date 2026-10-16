class Cat:
    def __init__(self,breed,color,age):
        self.__breed = breed
        self.color = color
        self.age = age
    def meow(self):
        print('Meow')
    def get_breed(self):
        return self.__breed
c = Cat('Русская', 'черная', 10)
print(c.breed)
c.meow()
Cat.meow(c)
c.weight = 10
print(c.weight)
