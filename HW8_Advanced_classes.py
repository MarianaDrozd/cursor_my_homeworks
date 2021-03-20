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
    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, forest: Forest):
        prey = random.choice(list(forest.animals.values()))
        if prey.current_power == 0:
            prey = random.choice(list(forest.animals.values()))
        else:
            if self.id == prey.id:
                print(f">>>>>The Predator {animal.id} is hunting...<<<<<")
                self.current_power = round(self.current_power * 0.5)
                print(f"The Predator {self.id} was left without a dinner and its power is {self.current_power}!")
                if self.current_power <= 0:
                    print(f"The Predator {animal.id} is dead by starving!")
                    forest.remove_animal(animal.id)
            else:
                print(f">>>>>The Predator {animal.id} is hunting the Prey {prey.id}...<<<<<")
                if self.speed > prey.speed and self.current_power > prey.current_power:
                    self.current_power = min(round(self.current_power + (self.max_power * 0.5)), self.max_power)
                    print(f"The Predator {animal.id} kills the Prey {prey.id}.",
                          f"The Predator's power is {animal.current_power}")
                    forest.remove_animal(prey.id)
                else:
                    self.current_power = max(round(self.current_power - self.max_power * 0.3), 0)
                    if self.current_power <= 0:
                        print(f"The Predator {animal.id} loses the fight and dies.")
                        forest.remove_animal(animal.id)
                    else:
                        print(f"The Predator's {animal.id} power became {animal.current_power}.")
                    prey.current_power = max(round(prey.current_power - prey.max_power * 0.3), 0)
                    if prey.current_power == 0:
                        forest.remove_animal(prey.id)
                    else:
                        print(f"The Prey's {prey.__class__.__name__} {prey.id} power became {prey.current_power}.")

    def __repr__(self):
        return f"{__class__.__name__} {animal.id}"


class Herbivorous(Animal):
    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, forest: Forest):
        self.current_power = min(round(self.current_power + (self.max_power * 0.5)), self.max_power)
        print(f"{__class__.__name__} {animal.id} is eating. Its power became {self.current_power}.")

    def __repr__(self):
        return f"{__class__.__name__} {animal.id}"


AnyAnimal: Any[Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        print(f"=====Added new animal {animal.__class__.__name__} {animal.id}, power:{animal.current_power}, "
              f"speed: {animal.speed}=====")
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        print(f"=====Removing dead animal {animal}...=====")
        self.animals.pop(animal)

    def any_predator_left(self):
        return not all(isinstance(animal, Herbivorous) for animal in self.animals.values())


def animal_generator():
    while True:
        anim = random.choice([Predator(random.randrange(25, 100, 1), random.randrange(25, 100, 1)),
                             Herbivorous(random.randrange(25, 100, 1), random.randrange(25, 100, 1))])
        anim.id = uuid.uuid4()
        yield anim


if __name__ == "__main__":
    nature = animal_generator()

    forest = Forest()
    for i in range(10):
        animal = next(nature)
        forest.add_animal(animal)

    while True:
        if not forest.any_predator_left():
            break
        for animal in list(forest.animals.values()):
            if animal.current_power == 0:
                continue
            else:
                animal.eat(forest=forest)
        time.sleep(1)
    print(f"These animals survived in the forest: {list(forest.animals.values())}")

# Output:
# /usr/bin/python3.8 /home/mariana/Документи/CURSOR/Homeworks/cursor_my_homeworks/HW8_Advanced_classes.py
# =====Added new animal Herbivorous 96b8486c-e1bc-4de9-8196-ff7401e0db6e, power:79, speed: 40=====
# =====Added new animal Predator 50038426-1d14-4fde-a0e3-a4528f29f679, power:46, speed: 70=====
# =====Added new animal Predator 6e072811-2bbf-413e-a658-b458dac4deb9, power:29, speed: 48=====
# =====Added new animal Herbivorous 1094c043-fc6a-457b-b54d-ce96f63ab824, power:26, speed: 88=====
# =====Added new animal Predator 1f979e15-5310-4e9c-8e74-8ab98cee009a, power:87, speed: 60=====
# =====Added new animal Herbivorous c2ec45e3-0da2-48b7-a20c-9942848ccefa, power:75, speed: 58=====
# =====Added new animal Herbivorous cf52cd00-ed2c-467d-ab72-0ef43f4d3c3c, power:29, speed: 84=====
# =====Added new animal Herbivorous 073225a8-c7c5-40e7-8be4-65195826cdff, power:56, speed: 69=====
# =====Added new animal Herbivorous 75ebe620-5598-4cf4-a2c3-124546249918, power:64, speed: 43=====
# =====Added new animal Predator 4790bb9a-054a-419c-a30a-2e40aef6d59e, power:42, speed: 80=====
# Herbivorous 96b8486c-e1bc-4de9-8196-ff7401e0db6e is eating. Its power became 79.
# >>>>>The Predator 50038426-1d14-4fde-a0e3-a4528f29f679 is hunting the Prey 6e072811-2bbf-413e-a658-b458dac4deb9...<<<<<
# The Predator 50038426-1d14-4fde-a0e3-a4528f29f679 kills the Prey 6e072811-2bbf-413e-a658-b458dac4deb9. The Predator's power is 46
# =====Removing dead animal 6e072811-2bbf-413e-a658-b458dac4deb9...=====
# >>>>>The Predator 6e072811-2bbf-413e-a658-b458dac4deb9 is hunting the Prey c2ec45e3-0da2-48b7-a20c-9942848ccefa...<<<<<
# The Predator's 6e072811-2bbf-413e-a658-b458dac4deb9 power became 20.
# The Prey's Herbivorous c2ec45e3-0da2-48b7-a20c-9942848ccefa power became 52.
# Herbivorous 1094c043-fc6a-457b-b54d-ce96f63ab824 is eating. Its power became 26.
# >>>>>The Predator 1f979e15-5310-4e9c-8e74-8ab98cee009a is hunting the Prey 1094c043-fc6a-457b-b54d-ce96f63ab824...<<<<<
# The Predator's 1f979e15-5310-4e9c-8e74-8ab98cee009a power became 61.
# The Prey's Herbivorous 1094c043-fc6a-457b-b54d-ce96f63ab824 power became 18.
# Herbivorous c2ec45e3-0da2-48b7-a20c-9942848ccefa is eating. Its power became 75.
# Herbivorous cf52cd00-ed2c-467d-ab72-0ef43f4d3c3c is eating. Its power became 29.
# Herbivorous 073225a8-c7c5-40e7-8be4-65195826cdff is eating. Its power became 56.
# Herbivorous 75ebe620-5598-4cf4-a2c3-124546249918 is eating. Its power became 64.
# >>>>>The Predator 4790bb9a-054a-419c-a30a-2e40aef6d59e is hunting the Prey cf52cd00-ed2c-467d-ab72-0ef43f4d3c3c...<<<<<
# The Predator's 4790bb9a-054a-419c-a30a-2e40aef6d59e power became 29.
# The Prey's Herbivorous cf52cd00-ed2c-467d-ab72-0ef43f4d3c3c power became 20.
# Herbivorous 96b8486c-e1bc-4de9-8196-ff7401e0db6e is eating. Its power became 79.
# >>>>>The Predator 50038426-1d14-4fde-a0e3-a4528f29f679 is hunting the Prey cf52cd00-ed2c-467d-ab72-0ef43f4d3c3c...<<<<<
# The Predator's 50038426-1d14-4fde-a0e3-a4528f29f679 power became 32.
# The Prey's Herbivorous cf52cd00-ed2c-467d-ab72-0ef43f4d3c3c power became 11.
# Herbivorous 1094c043-fc6a-457b-b54d-ce96f63ab824 is eating. Its power became 26.
# >>>>>The Predator 1f979e15-5310-4e9c-8e74-8ab98cee009a is hunting the Prey 4790bb9a-054a-419c-a30a-2e40aef6d59e...<<<<<
# The Predator's 1f979e15-5310-4e9c-8e74-8ab98cee009a power became 35.
# The Prey's Predator 4790bb9a-054a-419c-a30a-2e40aef6d59e power became 16.
# Herbivorous c2ec45e3-0da2-48b7-a20c-9942848ccefa is eating. Its power became 75.
# Herbivorous cf52cd00-ed2c-467d-ab72-0ef43f4d3c3c is eating. Its power became 26.
# Herbivorous 073225a8-c7c5-40e7-8be4-65195826cdff is eating. Its power became 56.
# Herbivorous 75ebe620-5598-4cf4-a2c3-124546249918 is eating. Its power became 64.
# >>>>>The Predator 4790bb9a-054a-419c-a30a-2e40aef6d59e is hunting...<<<<<
# The Predator 4790bb9a-054a-419c-a30a-2e40aef6d59e was left without a dinner and its power is 8!
# Herbivorous 96b8486c-e1bc-4de9-8196-ff7401e0db6e is eating. Its power became 79.
# >>>>>The Predator 50038426-1d14-4fde-a0e3-a4528f29f679 is hunting the Prey 1094c043-fc6a-457b-b54d-ce96f63ab824...<<<<<
# The Predator's 50038426-1d14-4fde-a0e3-a4528f29f679 power became 18.
# The Prey's Herbivorous 1094c043-fc6a-457b-b54d-ce96f63ab824 power became 18.
# Herbivorous 1094c043-fc6a-457b-b54d-ce96f63ab824 is eating. Its power became 26.
# >>>>>The Predator 1f979e15-5310-4e9c-8e74-8ab98cee009a is hunting the Prey cf52cd00-ed2c-467d-ab72-0ef43f4d3c3c...<<<<<
# The Predator's 1f979e15-5310-4e9c-8e74-8ab98cee009a power became 9.
# The Prey's Herbivorous cf52cd00-ed2c-467d-ab72-0ef43f4d3c3c power became 17.
# Herbivorous c2ec45e3-0da2-48b7-a20c-9942848ccefa is eating. Its power became 75.
# Herbivorous cf52cd00-ed2c-467d-ab72-0ef43f4d3c3c is eating. Its power became 29.
# Herbivorous 073225a8-c7c5-40e7-8be4-65195826cdff is eating. Its power became 56.
# Herbivorous 75ebe620-5598-4cf4-a2c3-124546249918 is eating. Its power became 64.
# >>>>>The Predator 4790bb9a-054a-419c-a30a-2e40aef6d59e is hunting the Prey 50038426-1d14-4fde-a0e3-a4528f29f679...<<<<<
# The Predator 4790bb9a-054a-419c-a30a-2e40aef6d59e loses the fight and dies.
# =====Removing dead animal 4790bb9a-054a-419c-a30a-2e40aef6d59e...=====
# The Prey's Predator 50038426-1d14-4fde-a0e3-a4528f29f679 power became 4.
# Herbivorous 96b8486c-e1bc-4de9-8196-ff7401e0db6e is eating. Its power became 79.
# >>>>>The Predator 50038426-1d14-4fde-a0e3-a4528f29f679 is hunting the Prey c2ec45e3-0da2-48b7-a20c-9942848ccefa...<<<<<
# The Predator 50038426-1d14-4fde-a0e3-a4528f29f679 loses the fight and dies.
# =====Removing dead animal 50038426-1d14-4fde-a0e3-a4528f29f679...=====
# The Prey's Herbivorous c2ec45e3-0da2-48b7-a20c-9942848ccefa power became 52.
# Herbivorous 1094c043-fc6a-457b-b54d-ce96f63ab824 is eating. Its power became 26.
# >>>>>The Predator 1f979e15-5310-4e9c-8e74-8ab98cee009a is hunting the Prey 75ebe620-5598-4cf4-a2c3-124546249918...<<<<<
# The Predator 1f979e15-5310-4e9c-8e74-8ab98cee009a loses the fight and dies.
# =====Removing dead animal 1f979e15-5310-4e9c-8e74-8ab98cee009a...=====
# The Prey's Herbivorous 75ebe620-5598-4cf4-a2c3-124546249918 power became 45.
# Herbivorous c2ec45e3-0da2-48b7-a20c-9942848ccefa is eating. Its power became 75.
# Herbivorous cf52cd00-ed2c-467d-ab72-0ef43f4d3c3c is eating. Its power became 29.
# Herbivorous 073225a8-c7c5-40e7-8be4-65195826cdff is eating. Its power became 56.
# Herbivorous 75ebe620-5598-4cf4-a2c3-124546249918 is eating. Its power became 64.
# These animals survived in the forest: [Herbivorous 75ebe620-5598-4cf4-a2c3-124546249918,
#                                        Herbivorous 75ebe620-5598-4cf4-a2c3-124546249918,
#                                        Herbivorous 75ebe620-5598-4cf4-a2c3-124546249918,
#                                        Herbivorous 75ebe620-5598-4cf4-a2c3-124546249918,
#                                        Herbivorous 75ebe620-5598-4cf4-a2c3-124546249918,
#                                        Herbivorous 75ebe620-5598-4cf4-a2c3-124546249918]
#
# Process finished with exit code 0
