import csv


def read(filename, list):
    with open(filename, 'r', newline='',  encoding='utf-8') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            list.append(row)


def write(filename, members):
    with open(filename, 'w', newline='',  encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for line in members:
            writer.writerow(line)
