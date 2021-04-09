# 2. Create a script with arguments:
#
# source_file_path; required: true;
# start_salary; required: false; help: starting point of salary;
# end_salary; required: false; help: the max point of salary;
# position; required: false; help: position role
# age; required: false; help: Age of person
# language; required: false; help; Programming language


# Based on this info generate a new report of average salary.
import argparse
import csv

parser = argparse.ArgumentParser(description="Homework. The script should read the .csv file and get the information "
                                             "based on your input and generate a new .csv file with that info")
parser.add_argument("--source_file_path", required=True)
parser.add_argument("--start_salary", required=False, help="Starting point of salary.")
parser.add_argument("--end_salary", required=False, help="The max point of salary.")
parser.add_argument("--position", required=False, help="Position role.")
parser.add_argument("--age", required=False, help="Age of person.")
parser.add_argument("--language", required=False, help="Programming language.")
args = parser.parse_args()


results = []
with open("2020_june_mini.csv", "r") as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    for row in reader:
        if row["Должность"] == args.position and row["Возраст"] == args.age\
           and row["Язык.программирования"] == args.language:
            results.append(row)
    print(results)

with open("2020_june_mini_my_file2.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    for line in results:
        writer.writerow(line)

# --position "Software Engineer" --age 21 --language Java --source_file_path .

start_sal = []
end_sal = []
with open("2020_june_mini_my_file2.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        a = row[2].split(",")
        b = row[3].split(",")
        start_sal.append(a)
        end_sal.append(b)
        start_sal1 = ' '.join([' '.join(strings) for strings in start_sal]).split()
        end_sal1 = ' '.join([' '.join(strings) for strings in end_sal]).split()
        for i, item in enumerate(start_sal1):
            start_sal1[i] = float(item)
        for i, item in enumerate(end_sal1):
            end_sal1[i] = float(item)
        start_salary = start_sal1
        end_salary = [x+y for x, y in zip(start_sal1, end_sal1)]
print(start_salary)
print(end_salary)

average_salary = (sum(start_salary)/len(start_salary) + sum(end_salary)/len(end_salary))//2

with open("2020_june_mini_my_file2.csv", "a") as f:
    f.write(f"Average salary is {str(average_salary)}")
