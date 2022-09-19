import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.energy = 0
        self.alive = True

    def to_Eat(self):
        print("Time to Eat")
        self.energy += 0.12
        self.gladness += 3


    def to_Sleep(self):
        print("Time to Sleep")
        self.gladness -= 2
        self.energy += 3

    def to_play(self):
        print("Time to play")
        self.energy -= 2
        self.gladness += 3

    def to_playOutside(self):
        print("Time to play outside")
        self.energy -= 6
        self.gladness += 5

    def to_drink(self):
        print("Time to drink water")
        self.energy += 3
        self.gladness -= 3

    def and_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Energy = {round(self.energy, 2)}")

    def is_alive(self):
        if self.energy < -0.5:
            print("Cat is very tired")
            self.alive = False
        elif self.gladness <= 0:
            print("Cat depression")
        elif self.energy > 5:
            print("Done!")
            self.alive = False


    def Life(self, day):
        day = "Day" +str(day)+"of"+self.name+"life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_Eat()
        elif live_cube == 2:
            self.to_Sleep()
        elif live_cube == 3:
            self.to_play()
        elif live_cube == 4:
            self.to_playOutside()
        elif live_cube == 5:
            self.to_drink()
        self.and_of_day()
        self.is_alive()


cat = Cat(name="cat")
for day in range(365):
    if cat.alive == False:
        break
    cat.Life(day)