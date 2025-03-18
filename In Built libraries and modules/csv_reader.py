
# -> Write a Python script to read a CSV file and display its contents in a formatted manner.

import csv

with open("sample.csv", newline='', encoding='utf-8') as sample:
    reader = csv.reader(sample)
    
    header = next(reader)
    print(f"{header[0]:<12} {header[1]:<20} {header[2]:<15} {header[3]:<10} {header[4]:<12}")
    print("-" * 70)
    
    for row in reader:
        print(f"{row[0]:<12} {row[1]:<20} {row[2]:<15} {row[3]:<10} {row[4]:<12}")

