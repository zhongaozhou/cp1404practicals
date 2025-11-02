"""
CP1404/CP5632 Practical
Wimbledon Champions
Reads Wimbledon data, processes champions and their countries,
and displays results.
Estimate: 30 minutes
Actual: 35 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read file, process data, and display the result."""
    records = read_csv(FILENAME)
    champion_to_wins, countries = process_data(records)
    display_results(champion_to_wins, countries)


def read_csv(filename):
    """Read CSV file into a list of records"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip header
        records = []
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_data(records):
    """Process records to count champion wins and get countries."""
    champion_to_wins = {}
    countries = set()

    for record in records:
        country = record[1]
        champion = record[2]
        countries.add(country)
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins, countries


def display_results(champion_to_wins, countries):
    """Display the champions, win counts, and the countries."""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
