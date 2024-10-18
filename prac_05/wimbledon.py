"""
Wimbledon
Estimate: 25 minutes
Actual:   36 minutes
"""
import csv
FILENAME = "wimbledon.csv"
def main():
    data = read_data(FILENAME)
    champion_count = count_champions(data)
    countries = get_unique_countries(data)
    print("Wimbledon Champions:")
    for champion, count in champion_count.items():
        print(f"{champion} {count}")
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

def read_data(FILENAME):
    """Reads the Wimbledon data file and returns list for each row."""
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            data.append(line.strip().split(","))
    return data

def count_champions(data):
    """Counts how many times each champion has won and returns a dictionary."""
    champion_count = {}
    for row in data:
        champion = row[2]
        if champion in champion_count:
            champion_count[champion] += 1
        else:
            champion_count[champion] = 1
    return champion_count

def get_unique_countries(data):
    """Returns a set of unique countries that have produced Wimbledon champions."""
    countries = set()
    for row in data:
        countries.add(row[1])
    return countries

main()
