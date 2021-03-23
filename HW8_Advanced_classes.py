from __future__ import annotations
from typing import Dict, Any
from abc import ABC, abstractmethod
import uuid
import random
import time


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError


class Predator(Animal):

    def eat(self, forest: Forest):
        prey = random.choice(list(forest.animals.values()))

        if self.id == prey.id:
            print(f">>>>>The Predator {animal.id} is hunting...<<<<<")
            self.current_power = round(self.current_power * 0.5)
            print(f"The Predator {self.id} was left without a dinner and its power is {self.current_power}!")
            if self.current_power == 0:
                print(f"The Predator {animal.id} is dead by starving!")
                forest.remove_animal(self)
        else:
            print(f">>>>>The Predator {animal.id} is hunting the Prey {prey.id}...<<<<<")
            if self.speed > prey.speed and self.current_power > prey.current_power:
                self.current_power = min(round(self.current_power + (self.max_power * 0.5)), self.max_power)
                print(f"The Predator {animal.id} kills the Prey {prey.id}.",
                      f"The Predator's power is {animal.current_power}")
                prey.current_power = 0
            else:
                self.current_power = max(round(self.current_power - self.max_power * 0.3), 0)
                if self.current_power <= 0:
                    print(f"The Predator {animal.id} loses the fight and dies.")
                else:
                    print(f"The Predator's {animal.id} power became {animal.current_power}.")
                prey.current_power = max(round(prey.current_power - prey.max_power * 0.3), 0)
                print(f"The Prey's {prey.__class__.__name__} {prey.id} power became {prey.current_power}.")
        if self.current_power == 0:
            forest.remove_animal(self)
        if prey.current_power == 0:
            forest.remove_animal(prey)

    def __repr__(self):
        return f"{__class__.__name__} {animal.id}"


class Herbivorous(Animal):

    def eat(self, forest: Forest):
        if self.current_power == 0:
            forest.remove_animal(self.id)
            return
        self.current_power = min(round(self.current_power + (self.max_power * 0.5)), self.max_power)
        print(f"{__class__.__name__} {animal.id} is eating. Its power became {self.current_power}.")

    def __repr__(self):
        return f"{__class__.__name__} {animal.id}"


AnyAnimal: Any[Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()
        self.i = 0

    def __iter__(self):
        self.i = 0
        self.animal_i = list(self.animals.values())
        return self

    def __next__(self):
        self.i += 1
        if self.i <= len(self.animal_i):
            return self.animal_i[self.i-1]
        else:
            raise StopIteration

    def add_animal(self, animal: AnyAnimal):
        print(f"=====Added new animal {animal.__class__.__name__} {animal.id}, power:{animal.current_power}, "
              f"speed: {animal.speed}=====")
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        if len(self.animals.values()) == 0:
            return
        print(f"=====Removing dead animal {animal}...=====")
        self.animals.popitem()

    def any_predator_left(self):
        return not all(isinstance(animal, Herbivorous) for animal in self.animals.values())


def animal_generator():
    while True:
        anim = random.choice([Predator(random.randrange(25, 100, 1), random.randrange(25, 100, 1)),
                             Herbivorous(random.randrange(25, 100, 1), random.randrange(25, 100, 1))])
        anim.id = uuid.uuid4()
        yield anim


if __name__ == "__main__":
    n = 0
    nature = animal_generator()

    forest = Forest()
    for i in range(10):
        animal = next(nature)
        forest.add_animal(animal)

    while True:
        print(f"...............{n}...............")
        n += 1
        if not forest.any_predator_left():
            break
        for animal in forest:
            animal.eat(forest=forest)
            if animal.current_power == 0:
                forest.remove_animal(animal)
        time.sleep(1)
    print(f"These animals survived in the forest: {list(forest.animals.values())}")
