# In the homework directory you can find the directory arg_parser_homework where you can find 2020_june_mini.csv file.
#
# 1. Create a script with arguments:
#
# exp; required: false; default: min(exp)
# current_job_exp; required: false; default: max(current_job_exp)
# sex; required: false
# city; required: false
# position; required: false
# age; required: false
# path_to_source_files; required: true;
# destination_path; required: false; default: .
# destination_filename; required: false; default: f"2020_june_mini.csv".
# The script should read the .csv file and get the information based on your input and generate a new .csv
# file with that info
#
# Example of input:
# -exp 3 -sex female -position DevOps -city Kyiv --path_to_source_files . ...
import argparse
import csv

f_exp = []
f_current_job_exp = []

with open("2020_june_mini.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        a = row[5].split(',')
        b = row[6].split(",")
        f_exp.append(a)
        f_current_job_exp.append(b)
f_exp.pop(0)
f_current_job_exp.pop(0)
f_exp1 = ' '.join([' '.join(strings) for strings in f_exp]).split()
f_current_job_exp1 = ' '.join([' '.join(strings) for strings in f_current_job_exp]).split()
for i, item in enumerate(f_exp1):
    f_exp1[i] = float(item)
for i, item in enumerate(f_current_job_exp1):
    f_current_job_exp1[i] = float(item)

x = min(f_exp1)
y = max(f_current_job_exp1)
print(f"min(exp) = {x}, max(current_job_exp) = {y}")
# min(exp) = 0.0, max(current_job_exp) = 10.0

parser = argparse.ArgumentParser(description="Homework. The script should read the .csv file and get the information "
                                             "based on your input and generate a new .csv file with that info")

parser.add_argument("-exp", required=False, default=0)
parser.add_argument("-cj", "--current_job_exp", required=False, default=10)
parser.add_argument("-sex", required=False)
parser.add_argument("-city", required=False)
parser.add_argument("-position", "-p", required=False)
parser.add_argument("--age", required=False)
parser.add_argument("-sp", "--path_to_source_files", required=False)
parser.add_argument("-dp", "--destination_path", required=False, default=".")
parser.add_argument("-df", "--destination_filename", required=False, default=f"2020_june_mini.csv")

args = parser.parse_args()

exp = args.exp
current_job_exp = args.current_job_exp
sex = args.sex
city = args.city
position = args.position
age = args.age
path_to_source_files = args.path_to_source_files
destination_path = args.destination_path
destination_filename = args.destination_filename

if args.sex is None:
    args.sex = ""
if args.city is None:
    args.city = ""
if args.position is None:
    args.position = ""
if args.age is None:
    args.age = ""

results = []
with open("2020_june_mini.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        pass






# 2. Create a script with arguments:
#
# source_file_path; required: true;
# start_salary; required: false; help: starting point of salary;
# end_salary; required: false; help: the max point of salary;
# position; required: false; help: position role
# age; required: false; help: Age of person
# language; required: false; help; Programming language


# Based on this info generate a new report of average salary.
