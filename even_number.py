#!/usr/bin/env python3

# Created by: Lucas DeBruyn
# Created on: Jan 2023
# This program checks how many even numbers are in a list

import random


def main():
    # Create a list of 10 random numbers
    random_nums = [random.randint(1, 10) for _ in range(10)]

    # Print the list of 10 random numbers
    print(random_nums)

    # Initialize the counter for even numbers
    even_count = 0

    # Iterate through the list of random numbers
    for num in random_nums:

        # Check if number is even
        if num % 2 == 0:
            even_count += 1

    # Print the number of even numbers
    print("The number of even numbers is: {}".format(even_count))

    print("\nDone.")


if __name__ == "__main__":
    main()
