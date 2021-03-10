import dataclasses
import collections


# 1.
class Laptop:
    """
    Make the class with composition.
    """

    def __init__(self, battery):
        self.battery = Battery(battery)

    def __str__(self):
        return f"This is a class Laptop with the battery {self.battery}."


class Battery:
    """
    Make the class with composition.
    """

    def __init__(self, name=0):
        self.name = name

    def __str__(self):
        return f"{self.name}"


laptop = Laptop("battery1")
print(laptop)
print(laptop.battery)


# Output:
# This is a class Laptop with the battery battery1.
# battery1

# 2.
class Guitar:
    """
    Make the class with aggregation
    """

    def __init__(self, strings):
        self.strings = strings

    def __str__(self):
        return f"My guitar has {self.strings} strings."


class GuitarString:
    """
    Make the class with aggregation
    """

    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"{self.num}"


string = GuitarString(6)
guitar = Guitar(string)
print(string)
print(guitar)


# Output:
# 6
# My guitar has 6 strings.

# 3
class Calc:
    """
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """

    @staticmethod
    def add_nums(a, b, c):
        return a + b + c


calc = Calc.add_nums(2, 3, 5)
print(calc)


# Output:
# 10


# 4*.
class Pasta:
    """
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(["tomato", "cucumber"])
pasta_2 = Pasta.bolognaise()

print(pasta_1.ingredients)
print(pasta_2.ingredients)


# Output:
# ['tomato', 'cucumber']
# ['bacon', 'parmesan', 'eggs']


# 5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self._visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, _visitors_count):
        if _visitors_count >= self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = _visitors_count


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)

# Output:
# 50


# 6.
@dataclasses.dataclass
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str),
    birthday (str), age (int)
    """
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


ad_book1 = AddressBookDataClass(1, "Mariana", "0123456789", "Lviv", "mymail@gmail.com", "12.03.1992", 28)
print(ad_book1)

# Output:
# AddressBookDataClass(key=1, name='Mariana', phone_number='0123456789', address='Lviv', email='mymail@gmail.com',
# birthday='12.03.1992', age=28)

# 7. Create the same class (6) but using NamedTuple
AddressBookDataClass1 = collections.namedtuple("AddressBookDataClass1", ["key", "name", "phone_number", "address",
                                                                         "email", "birthday", "age"])
ad_book2 = AddressBookDataClass1(2, "Anna", "0987654321", "Lviv", "annamail@gmail.com", "06.04.1997", 23)
print(ad_book2)


# Output:
# AddressBookDataClass1(key=2, name='Anna', phone_number='0987654321', address='Lviv', email='annamail@gmail.com',
# birthday='06.04.1997', age=23)

# 8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"{__class__.__name__}(key={self.key}, name={self.name}, phone_number={self.phone_number}, " \
               f"address={self.address}, email={self.email}, birthday={self.birthday}, age={self.age})"


maria = AddressBook(3, "Maria", "0369852147", "Kyiv", "mariamail@gmail.com", "28.06.1988", 32)
print(maria)


# Output:
# AddressBook(key=3, name=Maria, phone_number=0369852147, address=Kyiv, email=mariamail@gmail.com, birthday=28.06.1988,
# age=32)

# 9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


person = Person()
person.age = 38
print(person.age)


# Output:
# 38

# 10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(1, "Oleg")
setattr(student, "email", "oleg1k@gmail.com")
print(student.email)
student_email = student.__getattribute__("email")
print(getattr(student, "email"))
print(student_email)


# Output:
# oleg1k@gmail.com
# oleg1k@gmail.com
# oleg1k@gmail.com

# 11*.
class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return (self._temperature * 1.8) + 32


# create an object
convert = Celsius(35)

print(f"Conversion is done! The temperature is {convert.temperature} F!")


# Output:
# Conversion is done! The temperature is 95.0 F!
