import logging
"""
Task 1
Напишіть калькулятор в якого будуть реалізовані операції додавання, віднімання, множення, ділення, піднесення в
степінь,
взяття з під кореня, пошук відсотку від числа
Огорніть в конструкцію try... except... потенційно "небезпечні" місця, наприклад отримання числа і приведення до типу
даних
або інструкції математичних операцій
заповніть ваш скрипт логами
Логи здебільшого інформаційні (викликали таку функцію з такими аргументами)
+ логи з помилками
причому логи повинні записуватись у файл, тому що в консолі ви будете взаємодіяти з калькулятором,
лог файл завжди відкриваєтсья в режимі дозапису.
так як ви працюєте з файлом не забудьте про те що це потенційне місце поломки
"""
log_template = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, filename='HW9.1.log', filemode='a', format=log_template)


logging.info("Start running calculator")
print("Welcome to Calculator!")
print("You should enter two numbers and then operation with them.\n"
      "Hint: if you need operation '%', enter a percent value in the 2-nd number\n"
      "Hint: if you need operation '^', enter a root value in the 2-nd number")
while True:
    str_a = input("Enter first number: ")
    try:
        a = float(str_a)
    except ValueError:
        print(f"{str_a} is not a number")
        continue
    logging.info(f'Entered the 1-st number {a}')
    str_b = input("Enter the 2-nd number: ")
    try:
        b = float(str_b)
    except ValueError:
        print(f"{str_b} is not a number")
        continue
    logging.info(f'Entered second number {b}')
    op = ["+", "-", "*", "/", "**", "^", "%"]
    operation = input("Enter your operation (+, -, *, /, **, ^, %): ")
    while operation not in op:
        print(f'Operation {operation} is unknown. Try again!')
        operation = input("Enter your operation (+, -, *, /, **, ^, %): ")
    logging.info(f"Entered operation: {operation}.")

    def calculator():
        if operation == "+":
            return a + b

        elif operation == "-":
            return a - b

        elif operation == "*":
            return a * b

        elif operation == "/":
            try:
                a / b
            except ZeroDivisionError:
                logging.error("ZeroDivisionError", exc_info=True)
                print("The divider cannot be Zero")
                return 0
            return a / b

        elif operation == "**":
            try:
                a ** b
            except ZeroDivisionError:
                logging.error("ZeroDivisionError", exc_info=True)
                print("Zero cannot be raised to a negative power")
                return 0
            return a ** b

        elif operation == "^":
            try:
                a ** (1 / b)
            except ZeroDivisionError:
                logging.error("ZeroDivisionError", exc_info=True)
                print("The divider cannot be Zero!")
                return 0
            return a ** (1 / b)
        else:
            return a * b / 100
    logging.info("")
    result = calculator()
    logging.info('Called function calculator')
    print(f'Result of {a} {operation} {b} is: ', result)
    logging.info(f'Result of operation {a} {operation} {b} is {result}')
    logging.info("The end of running calculator.")
    print("Thank you for using calculator!")
    break
