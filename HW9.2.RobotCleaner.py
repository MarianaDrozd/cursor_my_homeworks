import time
'''
Task 2
Напишіть клас робота пилососа
в ініт приймається заряд батареї, заповненість сміттєбака і кількість води

реалізуйте функцію move() - нескінченний цикл який на кожній ітерації "замерзає" на 1 сек
окрім цього на кожній ітерації викликаються функції "wash" і "vacuum cleaner"
(в цих функціях повинні стояти прніти "wash" і "vacuum cleaner" відповідно),
також на кожній ітерації прінтиться "move"
+ на кожній ітерації цикла заряд батареї і кількість води зменшується на певну кількість
(задайте в статік аргументах класу як конфіг пилососа, або в окремому конфіг файлі),
а кількість сміття збільшується

Напишіть власні ексепшини які кидаються коли заряд батареї менше ніж 20%, заряд батареї 0%, кількість води - 0,
 кількість сміття більша ніж певне число
опрацюйте ваші ексепшини (наприклад якщо заряд батареї менше 20% то цикл робить ще певну кількість ітерацій і 
зупиняється,
якщо вода закінчилась то пилосос тепер не миє підлогу а тільки пилососить,
0 відсотків заряду - пилосос кричить щоб його занесли на зарядку бо сам доїхати не може)

можете придумати ще свої ексепшини і як їх опрацьовувати
'''


class LowBattery(Exception):
    pass


class NoCharge(Exception):
    pass


class FullTrash(Exception):
    pass


class NoWater(Exception):
    pass


class RobotCleaner:
    work_energy = 5
    work_trash = 50
    work_water = 100

    def __init__(self, charge_battery, trash_can, water_quantity):
        self.charge_battery = charge_battery
        self.trash_can = trash_can
        self.water_quantity = water_quantity

    def wash(self):
        if self.water_quantity > self.work_water:
            self.water_quantity -= self.work_water
            print(f"I wash your floor! I have {self.water_quantity} ml of water in my stomach!")
        else:
            raise NoWater

    def vacuum_cleaner(self):
        if self.charge_battery > 10:
            self.charge_battery -= self.work_energy
            print(f"I move to clean your house! My charge is {self.charge_battery}!")
        elif 1 < self.charge_battery <= 10:
            self.charge_battery -= 1
            raise LowBattery
        else:
            raise NoCharge
        if self.trash_can < 500:
            self.trash_can += self.work_trash
            print(f"I clean your house from trash! I got {self.trash_can} ml trash in my stomach!")
        else:
            raise FullTrash

    def move(self):
        i = 0
        while True:
            print(f"//////{i}/////")
            try:
                self.vacuum_cleaner()
            except FullTrash:
                print("Help! I need to empty my stomach!")
                self.trash_can = 0
            except LowBattery:
                print(f"Hey, I'm running to charge myself! My charge is {self.charge_battery}!")
            except NoCharge:
                print("I can't get charging myself. Bring me to charging place!")
                exit()
            try:
                self.wash()
            except NoWater:
                print("My water is off. I only vacuum clean!")
            i += 1
            time.sleep(1)


zhorick = RobotCleaner(100, 0, 302)

zhorick.move()



