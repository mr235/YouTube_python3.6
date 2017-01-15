print("--------------Classes and Object-------------------")
class Enemy:
    life = 3

    def attack(self):
        print("ouch!")
        self.life -= 1

    def checklife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")

enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checklife()
enemy2.checklife()

print("--------------init-------------------")
class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

student1 = Student("zhang san")
student2 = Student("li si")

student1.get_name()
student2.get_name()


print("--------------Class vs Instance Variables(成员变量和实例变量)-------------------")

class Girl:

    gender = "female"

    def __init__(self, name):
        self.name = name

r = Girl("Lucy")
s = Girl("Lili")
print("r's gender is " + r.gender + " and r's name is " + r.name)
print("s's gender is " + s.gender + " and s's name is " + s.name)

print("--------------Inheritance-------------------")

class Animal:

    def run(self):
        print("running")

    def eat(self):
        print("eat food")

class Cat(Animal):

    def catch_mouse(self):
        print("I can catch mouse!")

    def eat(self):
        print("eat mouse")

cat = Cat()
cat.run()
cat.catch_mouse()
cat.eat()

print("--------------Multiple Inheritance-------------------")

class Mario():

    def move(self):
        print("I am moving")

class Shroom():

    def eat_shroom(self):
        print("Now I am big!")

class BigMario(Mario, Shroom):
    pass

bm = BigMario()
bm.move()
bm.eat_shroom()
