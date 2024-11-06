"""
MyGuitar
Estimate: 30 minutes
Actual:   26 minutes
"""
import csv
from collections import namedtuple
from os import write

from guitar import Guitar

def main():
    guitars = []
    new_guitar = add_new_guitar()
    guitars.append(new_guitar)
    display_guitar = write_guitar(new_guitar)
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    for guitar in guitars:
        print(guitar)

def add_new_guitar():
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

def write_guitar(new_guitar):
    in_file = open("guitars.csv", "w")
    writer = csv.writer(in_file)
    for guitar in new_guitar:
        writer.writerow([guitar.name, guitar.year, guitar.cost])

main()

def using_csv():
    in_file = open('guitars.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
    in_file.close()