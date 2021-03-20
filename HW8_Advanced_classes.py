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
# =====Added new animal Predator 31fcfbb0-f6dc-45ce-a9eb-d412f9796c31, power:64, speed: 78=====
# =====Added new animal Herbivorous 680b2e03-92e9-44e6-a910-a5e0d3f38057, power:82, speed: 37=====
# =====Added new animal Predator d85f5a96-fd05-48e8-8b89-878f31fc51d2, power:40, speed: 82=====
# =====Added new animal Predator 53bb97d5-88f6-4a31-9a41-e5b0210a8684, power:44, speed: 92=====
# =====Added new animal Herbivorous b1ce4a61-97e6-4e4e-8d31-223a3382712c, power:40, speed: 87=====
# =====Added new animal Predator 1165137a-ad03-486c-b67f-b2b00258d80a, power:51, speed: 81=====
# =====Added new animal Herbivorous 2d49ab52-8ae3-4c0b-868a-89e3b3d11158, power:65, speed: 44=====
# =====Added new animal Predator 537cd817-d8d4-4120-a8e4-28879adecc38, power:43, speed: 82=====
# =====Added new animal Predator f7f2823b-a52d-4988-9f01-048fe0c85de0, power:27, speed: 62=====
# =====Added new animal Predator ac3c217f-919a-4434-9be7-231c3b6a7477, power:80, speed: 80=====
# >>>>>The Predator 31fcfbb0-f6dc-45ce-a9eb-d412f9796c31 is hunting the Prey 53bb97d5-88f6-4a31-9a41-e5b0210a8684...<<<<<
# The Predator's 31fcfbb0-f6dc-45ce-a9eb-d412f9796c31 power became 45.
# The Prey's Predator 53bb97d5-88f6-4a31-9a41-e5b0210a8684 power became 31.
# Herbivorous 680b2e03-92e9-44e6-a910-a5e0d3f38057 is eating. Its power became 82.
# >>>>>The Predator d85f5a96-fd05-48e8-8b89-878f31fc51d2 is hunting the Prey 680b2e03-92e9-44e6-a910-a5e0d3f38057...<<<<<
# The Predator's d85f5a96-fd05-48e8-8b89-878f31fc51d2 power became 28.
# The Prey's Herbivorous 680b2e03-92e9-44e6-a910-a5e0d3f38057 power became 57.
# >>>>>The Predator 53bb97d5-88f6-4a31-9a41-e5b0210a8684 is hunting the Prey 680b2e03-92e9-44e6-a910-a5e0d3f38057...<<<<<
# The Predator's 53bb97d5-88f6-4a31-9a41-e5b0210a8684 power became 18.
# The Prey's Herbivorous 680b2e03-92e9-44e6-a910-a5e0d3f38057 power became 32.
# Herbivorous b1ce4a61-97e6-4e4e-8d31-223a3382712c is eating. Its power became 40.
# >>>>>The Predator 1165137a-ad03-486c-b67f-b2b00258d80a is hunting the Prey 31fcfbb0-f6dc-45ce-a9eb-d412f9796c31...<<<<<
# The Predator 1165137a-ad03-486c-b67f-b2b00258d80a kills the Prey 31fcfbb0-f6dc-45ce-a9eb-d412f9796c31. The Predator's power is 51
# =====Removing dead animal 31fcfbb0-f6dc-45ce-a9eb-d412f9796c31...=====
# Herbivorous 2d49ab52-8ae3-4c0b-868a-89e3b3d11158 is eating. Its power became 65.
# >>>>>The Predator 537cd817-d8d4-4120-a8e4-28879adecc38 is hunting the Prey 53bb97d5-88f6-4a31-9a41-e5b0210a8684...<<<<<
# The Predator's 537cd817-d8d4-4120-a8e4-28879adecc38 power became 30.
# The Prey's Predator 53bb97d5-88f6-4a31-9a41-e5b0210a8684 power became 5.
# >>>>>The Predator f7f2823b-a52d-4988-9f01-048fe0c85de0 is hunting the Prey d85f5a96-fd05-48e8-8b89-878f31fc51d2...<<<<<
# The Predator's f7f2823b-a52d-4988-9f01-048fe0c85de0 power became 19.
# The Prey's Predator d85f5a96-fd05-48e8-8b89-878f31fc51d2 power became 16.
# >>>>>The Predator ac3c217f-919a-4434-9be7-231c3b6a7477 is hunting the Prey 537cd817-d8d4-4120-a8e4-28879adecc38...<<<<<
# The Predator's ac3c217f-919a-4434-9be7-231c3b6a7477 power became 56.
# The Prey's Predator 537cd817-d8d4-4120-a8e4-28879adecc38 power became 17.
# Herbivorous 680b2e03-92e9-44e6-a910-a5e0d3f38057 is eating. Its power became 73.
# >>>>>The Predator d85f5a96-fd05-48e8-8b89-878f31fc51d2 is hunting the Prey 1165137a-ad03-486c-b67f-b2b00258d80a...<<<<<
# The Predator's d85f5a96-fd05-48e8-8b89-878f31fc51d2 power became 4.
# The Prey's Predator 1165137a-ad03-486c-b67f-b2b00258d80a power became 36.
# >>>>>The Predator 53bb97d5-88f6-4a31-9a41-e5b0210a8684 is hunting the Prey f7f2823b-a52d-4988-9f01-048fe0c85de0...<<<<<
# The Predator 53bb97d5-88f6-4a31-9a41-e5b0210a8684 loses the fight and dies.
# =====Removing dead animal 53bb97d5-88f6-4a31-9a41-e5b0210a8684...=====
# The Prey's Predator f7f2823b-a52d-4988-9f01-048fe0c85de0 power became 11.
# Herbivorous b1ce4a61-97e6-4e4e-8d31-223a3382712c is eating. Its power became 40.
# >>>>>The Predator 1165137a-ad03-486c-b67f-b2b00258d80a is hunting the Prey b1ce4a61-97e6-4e4e-8d31-223a3382712c...<<<<<
# The Predator's 1165137a-ad03-486c-b67f-b2b00258d80a power became 21.
# The Prey's Herbivorous b1ce4a61-97e6-4e4e-8d31-223a3382712c power became 28.
# Herbivorous 2d49ab52-8ae3-4c0b-868a-89e3b3d11158 is eating. Its power became 65.
# >>>>>The Predator 537cd817-d8d4-4120-a8e4-28879adecc38 is hunting the Prey f7f2823b-a52d-4988-9f01-048fe0c85de0...<<<<<
# The Predator 537cd817-d8d4-4120-a8e4-28879adecc38 kills the Prey f7f2823b-a52d-4988-9f01-048fe0c85de0. The Predator's power is 38
# =====Removing dead animal f7f2823b-a52d-4988-9f01-048fe0c85de0...=====
# >>>>>The Predator f7f2823b-a52d-4988-9f01-048fe0c85de0 is hunting the Prey 680b2e03-92e9-44e6-a910-a5e0d3f38057...<<<<<
# The Predator's f7f2823b-a52d-4988-9f01-048fe0c85de0 power became 3.
# The Prey's Herbivorous 680b2e03-92e9-44e6-a910-a5e0d3f38057 power became 48.
# >>>>>The Predator ac3c217f-919a-4434-9be7-231c3b6a7477 is hunting the Prey d85f5a96-fd05-48e8-8b89-878f31fc51d2...<<<<<
# The Predator's ac3c217f-919a-4434-9be7-231c3b6a7477 power became 32.
# =====Removing dead animal d85f5a96-fd05-48e8-8b89-878f31fc51d2...=====
# Herbivorous 680b2e03-92e9-44e6-a910-a5e0d3f38057 is eating. Its power became 82.
# Herbivorous b1ce4a61-97e6-4e4e-8d31-223a3382712c is eating. Its power became 40.
# >>>>>The Predator 1165137a-ad03-486c-b67f-b2b00258d80a is hunting the Prey b1ce4a61-97e6-4e4e-8d31-223a3382712c...<<<<<
# The Predator's 1165137a-ad03-486c-b67f-b2b00258d80a power became 6.
# The Prey's Herbivorous b1ce4a61-97e6-4e4e-8d31-223a3382712c power became 28.
# Herbivorous 2d49ab52-8ae3-4c0b-868a-89e3b3d11158 is eating. Its power became 65.
# >>>>>The Predator 537cd817-d8d4-4120-a8e4-28879adecc38 is hunting the Prey 2d49ab52-8ae3-4c0b-868a-89e3b3d11158...<<<<<
# The Predator's 537cd817-d8d4-4120-a8e4-28879adecc38 power became 25.
# The Prey's Herbivorous 2d49ab52-8ae3-4c0b-868a-89e3b3d11158 power became 46.
# >>>>>The Predator ac3c217f-919a-4434-9be7-231c3b6a7477 is hunting the Prey 2d49ab52-8ae3-4c0b-868a-89e3b3d11158...<<<<<
# The Predator's ac3c217f-919a-4434-9be7-231c3b6a7477 power became 8.
# The Prey's Herbivorous 2d49ab52-8ae3-4c0b-868a-89e3b3d11158 power became 26.
# Herbivorous 680b2e03-92e9-44e6-a910-a5e0d3f38057 is eating. Its power became 82.
# Herbivorous b1ce4a61-97e6-4e4e-8d31-223a3382712c is eating. Its power became 40.
# >>>>>The Predator 1165137a-ad03-486c-b67f-b2b00258d80a is hunting the Prey 537cd817-d8d4-4120-a8e4-28879adecc38...<<<<<
# The Predator 1165137a-ad03-486c-b67f-b2b00258d80a loses the fight and dies.
# =====Removing dead animal 1165137a-ad03-486c-b67f-b2b00258d80a...=====
# The Prey's Predator 537cd817-d8d4-4120-a8e4-28879adecc38 power became 12.
# Herbivorous 2d49ab52-8ae3-4c0b-868a-89e3b3d11158 is eating. Its power became 58.
# >>>>>The Predator 537cd817-d8d4-4120-a8e4-28879adecc38 is hunting the Prey 2d49ab52-8ae3-4c0b-868a-89e3b3d11158...<<<<<
# The Predator 537cd817-d8d4-4120-a8e4-28879adecc38 loses the fight and dies.
# =====Removing dead animal 537cd817-d8d4-4120-a8e4-28879adecc38...=====
# The Prey's Herbivorous 2d49ab52-8ae3-4c0b-868a-89e3b3d11158 power became 38.
# >>>>>The Predator ac3c217f-919a-4434-9be7-231c3b6a7477 is hunting...<<<<<
# The Predator ac3c217f-919a-4434-9be7-231c3b6a7477 was left without a dinner and its power is 4!
# Herbivorous 680b2e03-92e9-44e6-a910-a5e0d3f38057 is eating. Its power became 82.
# Herbivorous b1ce4a61-97e6-4e4e-8d31-223a3382712c is eating. Its power became 40.
# Herbivorous 2d49ab52-8ae3-4c0b-868a-89e3b3d11158 is eating. Its power became 65.
# >>>>>The Predator ac3c217f-919a-4434-9be7-231c3b6a7477 is hunting the Prey 680b2e03-92e9-44e6-a910-a5e0d3f38057...<<<<<
# The Predator ac3c217f-919a-4434-9be7-231c3b6a7477 loses the fight and dies.
# =====Removing dead animal ac3c217f-919a-4434-9be7-231c3b6a7477...=====
# The Prey's Herbivorous 680b2e03-92e9-44e6-a910-a5e0d3f38057 power became 57.
# These animals survived in the forest: [Herbivorous ac3c217f-919a-4434-9be7-231c3b6a7477, Herbivorous ac3c217f-919a-4434-9be7-231c3b6a7477, Herbivorous ac3c217f-919a-4434-9be7-231c3b6a7477]
#
# Process finished with exit code 0
