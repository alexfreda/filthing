class define:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')

class fuckboy(define):
    def talk(self):
        print('fuckboy')

class movie(define):
    def __init__(self, name, age, genre):
        super().__init__(name,age)
        self.genre = genre
    def talk(self):
        print(f'{self.name}, {self.age}, {self.genre}')
   

d = define("Alex", 24)
d.show()
f = fuckboy("Brandon", 37)
f.talk()
m = movie("Star Wars", 18, "action")
m.talk()
