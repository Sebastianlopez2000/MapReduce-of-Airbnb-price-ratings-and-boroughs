#!/usr/bin/env python3

import sys
import csv

# Define the indices of the columns
neighbourhood_group_index = 5
price_index = 13
rating_index = 19

def main():
    # Input comes from STDIN (standard input)
    reader = csv.reader(sys.stdin)
    
    # Skip header
    next(reader)
    
    for row in reader:
        # Check if neighbourhood_group, price, and rating are not NA or empty
        if row[neighbourhood_group_index] == "NA" or row[neighbourhood_group_index] == "":
            continue  # Skip this row
        
        if row[price_index] == "NA" or row[price_index] == "":
            continue  # Skip this row
        
        if row[rating_index] == "NA" or row[rating_index] == "":
            continue  # Skip this row
        
        # Output neighbourhood_group, rating, and price
        print('%s\t%s\t%s' % (row[neighbourhood_group_index], row[rating_index], row[price_index]))

if __name__ == "__main__":
    main()
