#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_min_price_so_far = prices[0]
    max_profit_so_far = 0
    for num in prices:
        if num > max_profit_so_far:
            max_profit_so_far = num
        elif num < current_min_price_so_far:
            current_min_price_so_far = num
    profit = max_profit_so_far - current_min_price_so_far
    return profit


find_max_profit([1050, 270, 1540, 3800, 2])
if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
