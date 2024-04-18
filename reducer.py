#!/usr/bin/env python3

import sys

def main():
    current_key = None
    total_price = 0
    total_rating = 0
    count = 0

    for line in sys.stdin:
        key, rating, price = line.strip().split('\t')
        rating = float(rating)
        price = float(price)

        if key != current_key:
            if current_key:
                avg_price = total_price / count
                avg_rating = total_rating / count
                print('%s\t%s\t%s' % (current_key, avg_rating, avg_price))
            current_key = key
            total_price = 0
            total_rating = 0
            count = 0

        total_price += price
        total_rating += rating
        count += 1

    if current_key:
        avg_price = total_price / count
        avg_rating = total_rating / count
        print('%s\t%s\t%s' % (current_key, avg_rating, avg_price))

if __name__ == "__main__":
    main()
