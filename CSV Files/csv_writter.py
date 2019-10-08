import csv

filename = "student_grades.csv"

fields = ["name", "grades"]
rows = [
    ["Percy", "A+"],
    ["John", "B"],
    ["Kelly", "C"],
    ["Michel", "A"]
]

with open(filename, "w") as csv_writer:

    # creating csv writer object
    csv_writer = csv.writer(csv_writer)

    # add fields
    csv_writer.writerow(fields)

    # write data
    csv_writer.writerows(rows)

print(f"{filename} file created")
